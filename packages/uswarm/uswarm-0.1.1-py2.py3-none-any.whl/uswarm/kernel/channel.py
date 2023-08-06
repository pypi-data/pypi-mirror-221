import hashlib
import pickle
import re
import ssl
import socket
import errno

from collections import deque

from .stm import *
from .userver import uServer

from uswarm.tools import (
    parse_uri,
    build_uri,
    soft,
    get_calling_function,
    find_by_regexp,
)

from uswarm.parsers import dict_decode

# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger

log = logger(__name__)


class XMessage(Message):
    """"""

    def decode(self):
        pass

    def parse(self, dec):
        """Decode Message:
        Example:
        self.dom = dict_decode(list(dec), list(self.body))
        return self.dom

        """
        self.dom = dict_decode(list(dec), self["body"])
        self.update(self.dom)
        return self.dom

    def get_rid(self):
        assert False
        return self.header.get(RID_HEADER)

    def get_handler_code(self):
        """return the mid seaching in self._fields"""
        assert False
        return self.header["code"]


def ssl_wrap(sock, host, **kw):
    context = ssl.create_default_context()
    ssock = context.wrap_socket(sock, server_hostname=host)
    return ssock


EVENT_RX = "<rx>"
EVENT_TX = "<tx>"


class Channel(uServer):
    @classmethod
    def _allocate_resource(cls, kernel, _uri, **kw):
        uri = build_uri(**_uri)
        holder = kernel.resources.setdefault(_uri["fscheme"], {})
        channel = holder.get(uri)

        if not channel:
            try:
                channel = cls(uri, kernel, **kw)
                # log.debug(f"0. sock: {channel.sock}")
                # assert timer.value == value
                holder[uri] = channel
                # kernel.resources["fds"][channel.sock] = channel
                log.debug(f"Allocating: <{uri}> ")

            except Exception as why:
                log.exception(why)
                channel = None
        return channel

    @classmethod
    def _deallocate_resource(cls, kernel, _uri, **kw):
        args = _uri["host"]
        m = re.match(r".*$", args)
        if m:
            d = m.groupdict()
            holder = kernel.resources.setdefault(_uri["fscheme"], {})

            uri = build_uri(**_uri)
            channel = holder.pop(uri, None)
            if channel:
                channel.pause_rx()
                channel.pause_tx()
                channel.sock.close()

            return channel

    """socket alike protocol

    - [ ] assert on creating a new clean message after dispatching received one.
    - [ ] review handlers, callbacks, etc inside channel (before publishing).
    - [x] more clear send, dispatch, etc function names.
    - [ ] clear req/res mechanism.
    - [ ] unify how to make requests (get, etc) and wait responses.

    - [ ] detect TWS hangout on connecting (does not receive server version). Use timeout

    """

    MAX_READ = 0x8000

    SOCKS_PARAMS = {
        "udp": (socket.AF_INET, socket.SOCK_DGRAM, socket.SOL_UDP),
        "tcp|http|ssl|https": (socket.AF_INET, socket.SOCK_STREAM, socket.SOL_TCP),
        "<default>": (socket.AF_INET, socket.SOCK_STREAM, socket.SOL_TCP),
    }
    SOCKS_OPTIONS = {
        "udp": [
            (socket.SO_BROADCAST, 1),
            (socket.SO_REUSEADDR, 1),
            (socket.SO_REUSEPORT, 1),
        ],
        "tcp|http|https": [
            (socket.SO_KEEPALIVE, 1),
            (socket.SO_REUSEADDR, 1),
            (socket.SO_REUSEPORT, 1),
        ],
        "<default>": [
            (socket.SO_REUSEADDR, 1),
            (socket.SO_REUSEPORT, 1),
        ],
    }
    SOCKS_WRAPPERS = {
        "ssl|https": [
            ssl_wrap,
        ],
        "<default>": [],
    }
    SCHEME_DEFAULTS = {
        "http": {"port": 80},
        "https": {"port": 443},
        "<default>": {},
    }
    CHANNELS = {
        "broadcast": {
            "options": [
                (socket.SO_BROADCAST, 1),
                (socket.SO_REUSEADDR, 1),
            ],
            "bind": ("", 9999),
        },
        "direct": {
            "options": [
                (socket.SO_BROADCAST, 1),
                (socket.SO_REUSEADDR, 1),
            ],
        },
    }

    # ----------------------------------------------------------------
    # Generic Render and Parsing messages support
    # ----------------------------------------------------------------

    #: render tenplates for outgoing messages
    #: key: render path
    #: - reponse_type: RESPONSE_NONE, RESPONSE_SINGLE, RESPONSE_MULTIPLE
    #:                 RESPONSE_SUBSCRIPTION, RESPONSE_NO_DATA
    #: - container klass: dict, list, ...
    #: - render keywords pattern for raw output
    #: - keywords default values if missing
    #: - callbacks: tuple of callbacks when message is received
    #: - tracking: keywords map for tracking long requests process
    META_REQUEST = {  # TODO: change to "render"
        "default": (
            RESPONSE_NONE,
            None,
            """No templates has been defined""",
            {},
            (),
            {"current": "end"},
        ),
        # "/account/position": (
        # RESPONSE_MULTIPLE,
        # dict,
        # "{idx}\0{version}\0{rid}\0" "{account}\0{model_code}\0",
        # {
        # "idx": OUT.REQ_POSITIONS_MULTI,
        # "version": 1,
        # "rid": 0,
        # "account": "",  # TODO: checks if can be blank
        # "model_code": "",
        # },
        # (),
        # {"current": "end"},
        # ),
    }

    RESPONSE_KLASS = XMessage

    message: XMessage

    def __init__(self, uri, kernel, factory=Message, *args, **kw):
        self.reconnect = True
        self._outgoing = deque()
        self._incoming = deque()
        self._raw = b""
        self.factory = factory
        self.message = None

        super().__init__(uri, kernel, *args, **kw)

        self._next_rid = 2000

        self.allowed_deferred[EVENT_RX] = True
        self.allowed_deferred[EVENT_TX] = True

    def _setup_020_rx(self):
        """Set TERM and QUIT logic for the base layer."""
        states = {}

        transitions = {
            EVENT_RX: {
                STATE_SYNC: [
                    [STATE_SYNC, [], ["dispatch_sync"]],
                ],
                STATE_TRAN: [
                    [STATE_TRAN, [], ["dispatch_tran"]],
                ],
                STATE_LIVE: [
                    [STATE_LIVE, [], ["dispatch_live"]],
                ],
            },
        }

        return states, transitions, MERGE_ADD

    def _setup_025_term_nicely(self):
        """Control which events must be attended in STATE_TERM state."""
        states = {}

        transitions = {
            EVENT_RX: {
                STATE_TERM: [
                    [STATE_TERM, [], ["dispatch_live"]],
                ],
            },
        }

        return states, transitions, MERGE_ADD

    # ----------------------------------------------------------------
    # STM callbacks methods
    # ----------------------------------------------------------------

    def off_2_init(self, event, data, wave, *args, **kw):
        """Analyze uri and create a the socket with all
        the configuration needed for operation.
        """
        self.message = self._new_message()
        self._raw = b""  # needed on reconnection
        super().off_2_init(event, data, wave, *args, **kw)

    def init_2_conn(self, event, data, wave, *args, **kw):
        scheme = self._uri["scheme"]
        host = self._uri["host"]
        direction = self._uri["direction"]

        params = find_by_regexp(self.SCHEME_DEFAULTS, scheme)
        soft(self._uri, **params)

        params = find_by_regexp(self.SOCKS_PARAMS, scheme)

        sock = socket.socket(*params)
        for option, value in find_by_regexp(self.SOCKS_OPTIONS, scheme):
            sock.setsockopt(socket.SOL_SOCKET, option, value)

        for wrapper in find_by_regexp(self.SOCKS_WRAPPERS, scheme):
            sock = wrapper(sock, **self._uri)

        self.sock = sock

        address = self._uri.get("address", (self._uri["host"], self._uri["port"]))

        # TODO: extend with all host interfaces, ...
        if host in ("<broadcast>") or direction in ("<",):
            sock.bind(address)
        else:
            try:
                # SSL Non-Blocking:
                # https://cppsecrets.com/users/1370011211510411798104971101069712164103109971051084699111109/Python-ssl-non-blocking-sockets.php
                # while True:
                # try:
                # sock.do_handshake()
                # break
                # except ssl.SSLWantReadError:
                # select.select([sock], [], [])
                # except ssl.SSLWantWriteError:
                # select.select([], [sock], [])
                if self._uri["fscheme"] not in ("https",):
                    sock.setblocking(False)
                    log.warning(
                        f"[{self.uri:20}][{self.state}] -- connecting ASYNC: {address} ..."
                    )
                else:
                    log.debug(
                        f"[{self.uri:20}][{self.state}] -- connecting: {address} ..."
                    )

                sock.connect(address)
                log.debug(f"-- sock: {sock} --")

            except OSError as exc:
                if exc.errno != errno.EINPROGRESS:  # EINPROGRESS
                    raise
                log.debug(
                    f"[{self.uri:20}][{self.state}] -- connecting: asyncronous mode: EINPROGRESS"
                )
            except ConnectionRefusedError as why:
                self.connection_lost()
                raise

        self.resume_rx()

        super().init_2_conn(event, data, wave, *args, **kw)

    def dispatch_sync(self, event, data, wave, *args, **kw):
        self.dispatch_live(event, data, wave, *args, **kw)
        self.asap(EVENT_NEXT)

    def dispatch_tran(self, event, data, wave, *args, **kw):
        self.dispatch_live(event, data, wave, *args, **kw)
        self.asap(EVENT_NEXT)

    def dispatch_live(self, event, data, wave, *args, **kw):
        raise NotImplementedError()

    # ----------------------------------------------------------------
    # High I/O
    # ----------------------------------------------------------------

    def _render_request(self, req, debug=False):
        """Render the request based on template protocol definition."""
        # raw = super()._render_request(req, template)
        # self._expand_request(req)
        self._expand_special_fields(req)

        meta = self.META_REQUEST.get(req["path"]) or self.META_REQUEST["default"]
        wait, body, template, extra, callbacks, tracking = meta

        raw = self._encoder(template.format(**req))
        req["raw"] = raw
        return raw

    def _expand_special_fields(self, req):
        pass

    def _encoder(self, *message):
        """Encode data to be sent to server"""
        raw = "".join([f"{v}" for v in message])
        # size = len(raw)
        # raw = pack(f"!I{size}s", size, str.encode(raw))
        return raw

    # --------------------------------------------------
    # Events
    # --------------------------------------------------
    def term(self, event, data, wave, *args, **kw):
        """Execute in every received event while state = STATE_TERM.

        Channels do not quit, just keep I/O working until EVEN_QUIT
        is received, so other STM can received events that finaly
        will move them to EVENT_QUIT / STOP state.

        """
        log.debug(f"[{self.uri:20}][{self.state}] -- term 2 ...")
        # if not self.pending_responses:
        # super().term(event, data, wave, *args, **kw)

    # ----------------------------------------------------------------
    # rx/tx mechanism
    # ----------------------------------------------------------------

    def rx(self):
        """Process RX incoming socket activity."""
        raise NotImplementedError()

    def tx(self):
        """Send TX outgoing data."""
        raise NotImplementedError()

    # pause-resume rx/tx
    def pause_rx(self):
        """Pause this channel for attending incoming data."""
        log.debug(f"[{self.uri:20}][{self.state}] -- pause_rx")
        self.kernel.fds_rx.pop(self.sock, None)

    def resume_rx(self):
        """Set channel for attending incoming data."""
        log.debug(f"[{self.uri:20}][{self.state}] -- resume_rx")
        self.kernel.fds_rx[self.sock] = self

    def pause_tx(self):
        """Pause this channel for sending outgoing data."""
        log.debug(f"[{self.uri:20}][{self.state}] -- pause_tx")
        self.kernel.fds_tx.pop(self.sock, None)

    def resume_tx(self):
        """Set channel for sending outgoing data."""
        if self._outgoing:
            log.debug(f"[{self.uri:20}][{self.state}] -- resume_tx")
            self.kernel.fds_tx[self.sock] = self

    # ----- ??? -----------------

    def _new_message(self) -> Message:
        """Create a new Response message."""
        return self.factory()

    # ----------------------------------------------------------------
    # low I/O
    # ----------------------------------------------------------------

    def _dispatch(self, msg):  # TODO: delete
        """Attend an incoming message.
        At this level:
        - decode body/payload data based on headers.
        - create a new incoming response message to be filled on next reads.
        """
        msg.decode()
        log.debug(f"dispatching: {msg}")
        # create a new incoming message
        self.message = self._new_message()

    def _write(self, data):
        """Append data in the outgoing queue.
        It also request kernel to wakeup writing ASAP.
        """
        assert isinstance(data, bytes)
        self._outgoing.append(data)
        log.debug(f"[{self.uri:20}][{self.state}] -- send: {data}")
        self.resume_tx()

    def connection_lost(self, *args):
        """Called when peer is 'disconnected' somehow.

        Typically used by stream channels but is also
        be called by datagram protocols depending on
        channel desing / goals.

        If 'reconnect' is set kernel will try to reconnect
        a new channel with the same uri.

        - remove channel from kernel.
        - schedule uri to be reconnect in the future.
        """
        self.kernel.delete(self.uri)
        if self.reconnect:
            self.kernel.retry(self.uri)

    def _track_request(self, req, meta):
        pass


class UDPChannel(Channel):
    """UDP Support"""

    # TODO: pending use udp channels for anythng (but broadcasting)
    # KERNEL_URI_REGISTERING="(udp)://<broadcast>"
    def rx(self):
        raw, addr = self.sock.recvfrom(0x8000)
        # if not raw and addr is None:
        # self.connection_lost()

        log.debug(f"received {raw} from {addr}")

    def tx(self):
        raise RuntimeError("pending of include 'address' for every message")


class BroadcasChannel(UDPChannel):
    """UDP Support"""

    KERNEL_URI_REGISTERING = "(udp)://<broadcast>"

    def tx(self):
        data = self._outgoing.popleft()
        print(f">> {data}")
        raw = pickle.dumps(data)
        address = self.sock.getsockname()
        self.sock.sendto(raw, address)
        not self._outgoing and self.pause_tx()


class TCPChannel(Channel):
    """TCP Support"""

    KERNEL_URI_REGISTERING = "(tcp)://"

    def rx(self):
        raw = self.sock.recv(0x8000)
        if raw:
            log.debug(f"received {len(raw)} bytes, {raw[:40]} ... ")
            self._raw += raw
            return

        log.warning(f"connection reset {self.uri}[{self.state}]")
        self.connection_lost()

    def tx(self):
        raw = self._outgoing.popleft()
        log.debug("->--------------------------------------------")
        log.debug(f">>>> [{self.uri}][{self.state}] {raw}")
        log.debug("-<--------------------------------------------")
        self.sock.send(raw)
        not self._outgoing and self.pause_tx()
