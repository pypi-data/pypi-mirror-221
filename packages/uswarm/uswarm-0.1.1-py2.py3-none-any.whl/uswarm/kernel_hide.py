"""Kenel module.

# 0 register queues

- [ ] Detect cycles (bad nested timers, ...)

- [ ] register a queue function with uri and context: #q{**ctx}
- [ ] instrospection to get a,b,c,... arguments call.
- [ ] link #q.out --> #q.in{a|b|c...}
- [ ] kernel create *waves* that flows across links
- [ ] when a #q has all parameters completed for the same
      wave, kernel executes the queue function.

- [ ] the function ends and the returned values if fwd
      throught its links to complete input args of other
      functions in the same wave.

- [ ] waves must be monotone cresced.
- [ ] waves lower than last executed are ignored (echoes)
- [ ] check recursive dispatching approach vs event queue approach.
      speed vs other unexpected  side effects.
- [ ] no asyncio, just one shot calls.
- [ ] use multiprocess, fork, etc to create many host
     programs to support parallel execution of the same
     kernel

- [ ] use a decorator for handler functions
- [ ] speed test for direct call and call with **kw

  Wave stacks

            [-, b, ..., **ctx]
   --(+)--> [a, b, ..., **ctx]  (pending)
            [a, -, ..., **ctx]
            [-, b, ..., **ctx]
   --(+)--> [a, b, ..., **ctx] ---> exec()


# 1 bot
- [x] asyncio implementation, but keep as much generic possible.
- [x] queue abtraction
- [ ] protocol linked with queue
- [ ] dispatch
- [ ] event is inmutable, serializable.
- [ ] 1 bot, n tasks (input streams).
- [ ] connecting, sync, ready, term states
- [ ] kernel as resource provider.
- [ ] kernel provide ALL resources (isolation as dockers)
- [ ] use human names for naming bots instances
- [ ] check health.

# 2 pub/sub
- [ ] simple static DF

# 3 DF Template Rendering
- [ ] xxx
- [ ]

# 4 Dynamic Dataflows
- [ ] Session Concept
- [ ] Minimal Kernel support
- [ ] Fibonacci Examples
- [ ] Other Examples
- [ ] DO NO CONTINUE unitl feel safe with future uses.

# 5: Pause, Resume, Save, Stop
- [ ] bot internal state persistence by Kernel. (yaml, pickle)
- [ ] sync state implementation
- [ ] adding a Bot to existing running infrastructure
- [ ] Stream XZ support by Kernel.
- [ ] Market Stream simulator


# 6: Kernel bootstraping
- [ ] use *init* bot.
- [ ] Kernel monitoring: sync %, status, load, etc.
- [ ] DF progress (based on input key range when availble)

#7: kernel networking.
- [ ] many transport implementations.


# 8: Distributed Kernels
- [ ] Kernel interconnection.
- [ ] Kernel discovering.
- [ ] Sharing kernel stats.
- [ ] Moving a Dataflow to another hosts (non-stop).
  - [ ] vmware approach.
- [ ] Replicas, HA.


Synchronization:

A: source
B: target connected and synchroized
Z: new target out-of-sync.


1. Z create #Z.0 main port
2. Z connect #A.out <---- #Z.0, but no fiber is dispatching #Z.0 yet.
3. A send new data to #B.0 and #Z.0 ports (subscribed)
4. #Z.0 is filled with fresh data, but none is dispatching them yet.
5. if #Z.0 size > limit, Z disconnect #Z.0 from #A.out
5. Z checks the last known data: k0
6. Z create another #Z.1 port for Synchronization.
6. Z requires A a sync process from k0 to 'now' in #Z.1
7. a R (A replica) process is started getting data from k0 to current moment.
8. data received in #Z.1 is dispatched as normal flow.
9. R is finished and close the connection (disconnect wih #Z.1)
10. Z check if #Z.0 is disconnected.
11. if is disconnected means we need another sync process.
   - move all data from #Z.0 to #Z.1.
   - reuse #Z.0 port for the next sync process.
   - get the new k0 as the last data in #Z.0 during flushing.
   - goto point (2)
12. if is connected means we can finish the Synchronization and
    step forwards Transition and Live.
   - mark #Z.1 as *term*. Will be auto-killed when is empty.
   - #Z.1 fiber still will send all new data until empty.
   - when is finished, activate #Z.0 fiber and change status to 'Transition'
   - #Z.0 fiber will send all data until eventually get *empty*.
   - Then change status to *Live* and continue with normal flow.
   - A and Z are connected and synchroized, forwarding all data received.



We need:
- Fiber+Queue = FiberQueue dispatcher class (FQ).
- Create/Destroy FQ named as ports #X.n and registered in kernel.
- Connect/Disconnect port #Y.m --> #X.n (subscribed).
- Get other ports linked with a given port (publisher or subscriber).
- Data is placed in subscribed FQ automatically by publisher.
- Kernel will handle this under the hood (same process or networking).
- Activate or pause a FQ for dispatching its data.
- Hooks or notification when:
    - a port thar match some regexp is created, destroyed in kernel.
    - an existing port is linked or unlinked.
    - queue reach some size.
- Mark a FQ to self-destroy when is empty.
- Start a new FQ to get historical data and publish its data.




"""
import re
import ssl
import socket
import threading
import random
import traceback
import yaml
import functools
import inspect
import pickle
import gc
import sys
import ssl

from time import time, sleep

from collections import deque
from datetime import datetime
from select import select

from weakref import WeakValueDictionary as wvdick

# HTTP ----------
import lzma as xz
import gzip as gz
import bz2
import zlib

# ----------
from uswarm.tools import parse_uri, build_uri, soft

from uswarm.tools.logs import logger

log = logger(__name__)

# ------------------------------------------------
# Nuevo kernel
# ------------------------------------------------
class Stats(dict):
    def push(self, t0, data):
        self.setdefault(t0, {}).update(data)

    def compute(self, historical=100):
        keys = list(self.keys())
        keys.sort()
        while len(self) > historical:
            self.pop(keys.pop(0))

        self.means = {}
        for wave, data in self.items():
            for k, v in data.items():
                self.means.setdefault(k, []).append(v)

        for key, values in list(self.means.items()):
            self.means[key] = sum(values) / len(values)


STATE_OFF = "off"
STATE_INIT = "init"
STATE_SYNC = "sync"
STATE_TRANSITION = "transition"
STATE_LIVE = "live"
STATE_TERM = "term"

NEXT_STATE = {
    STATE_OFF: STATE_INIT,
    STATE_INIT: STATE_SYNC,
    STATE_SYNC: STATE_TRANSITION,
    STATE_TRANSITION: STATE_LIVE,
    STATE_LIVE: STATE_TERM,
}


class Protocol:
    @classmethod
    def ssl_wrap(cls, sock, host, **kw):
        context = ssl.create_default_context()
        ssock = context.wrap_socket(sock, server_hostname=host)
        return ssock

    def __init__(self, uri, kernel):
        """
        - build initial state for start synchronization process.
        """
        self.uri = uri
        self._uri = parse_uri(uri)
        assert any(self._uri.values()), f"Bad URI '{uri}'"

        self.kernel = kernel
        self.state = STATE_OFF

        kernel and kernel.register_queue(self)
        self.next_state()

    def __repr__(self):
        return f"<{self.uri}>"

    def connection_made(self, *args):
        """Called when a connection is made."""

    def connection_lost(self, *args):
        """Called when the connection is lost or closed."""

    # STM states alike
    def next_state(self):
        self.change_state(NEXT_STATE[self.state])

    def change_state(self, state):
        func = getattr(self, f"_exit_{self.state}", None)
        func and func()

        self.state = state

        func = getattr(self, f"_enter_{self.state}", None)
        func and func()

    def _enter_init(self):
        self.next_state()

    def _enter_sync(self):
        self.next_state()

    def _enter_transition(self):
        self.next_state()

    def _enter_live(self):
        foo = 1

    def _enter_term(self):
        foo = 1


ALL_GROUPS = "*"


class Publisher(Protocol):
    """REVIEW: ..."""

    def __init__(self, uri, kernel, *args, **kw):
        super().__init__(uri, kernel)

    def data_received(self, provider, name, item, wave, *route):
        """a new data is received from provider.
        check if we can fire handle to make a step.

        Default implementation just forwards all data received.
        """
        deferred = super().data_received(provider, name, item, wave, *route)
        if not deferred:
            # check if all in-data has been received
            assert (
                name not in self.in_args
            ), f"overwriting incoming arg '{name}' before have been processed."

            self.in_args[name] = item
            if set(self.inputs.keys()).issubset(self.in_args):
                # all inputs are completed
                result = self.compute()
                # TODO: implement filter for FWD
                fqscheme = self._fwd_group(result)
                self.forward(fqscheme, wave, result, *route)
                self.clean_inputs()
        return deferred

    def compute(self):
        """Compute the condensation of received data.

        - modify internal state (wip outcome)
        - flush outcome result when is completed.

        FWD everithing
        """
        return self.in_args

    def _fwd_group(self, result):
        """Compute FWD groups.
        ALL by default.
        """
        return ALL_GROUPS

    def forward(self, fqscheme, wave, item, *route):
        """Push processed data into output provider.

        - send data to out provider.
        - start a fresh new inputs for compute the next outcome.
        """
        for regexp, holder in self.flows.items():
            if fqscheme == ALL_GROUPS or regexp.match(fqscheme):
                for actor, name in holder.values():
                    actor.data_received(self, name, item, wave, *route)

    def replay(self, target, wzero):
        """Resend all known waves from wzero to current wave."""
        # TODO: a 2nd connection is necessary?
        raise NotImplementedError()


class Timer(Publisher):
    value: float

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.value = float(self._uri["path"].split("/")[-1])
        foo = 1


def find_by_regexp(source, key, default_key="<default>"):
    for regexp, params in source.items():
        if re.match(regexp, key):
            return params
    return source.get(default_key)


class Message(dict):
    """"""
    def decode(self):
        pass



class Channel(Publisher):
    """socket alike protocol"""

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
            Protocol.ssl_wrap,
        ],
        "<default>": [],
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

    message: Message

    def __init__(self, uri, kernel, factory=Message, *args, **kw):
        self.reconnect = True
        self._outgoing = deque()
        self._incoming = deque()
        self._raw = b""
        self.factory = factory
        self.message = None

        super().__init__(uri, kernel)

    def _new_message(self) -> Message:
        return self.factory()

    def _enter_init(self):
        scheme = self._uri["scheme"]
        host = self._uri["host"]
        direction = self._uri["direction"]
        address = self._uri["address"]

        params = find_by_regexp(self.SOCKS_PARAMS, scheme)

        sock = socket.socket(*params)
        for option, value in find_by_regexp(self.SOCKS_OPTIONS, scheme):
            sock.setsockopt(socket.SOL_SOCKET, option, value)

        for wrapper in find_by_regexp(self.SOCKS_WRAPPERS, scheme):
            sock = wrapper(sock, **self._uri)

        self.sock = sock

        # TODO: extend with all host interfaces, ...
        if host in ("<broadcast>") or direction in ("<",):
            sock.bind(address)
        elif scheme in ("tcp", "http", "https") and direction in (
            None,
            ">",
        ):
            try:
                sock.connect(address)
                log.info(f"-- sock: {sock} --")
            except ConnectionRefusedError as why:
                self.connection_lost()
                raise
        else:
            print(f"????: {uri}")

        self.message = self._new_message()
        super()._enter_init()

    # handshaking and rx/tx methods
    def change_state(self, state):
        super().change_state(state)
        self._change_rxtx()

    def _change_rxtx(self):
        # change rx/tx methods when are defined
        for t in "rx", "tx":
            name = f"{t}_{self.state}"
            func = getattr(self, name, None)
            if func:
                log.debug(f"set {name} -> {t}")
                setattr(self, t, func)

    def rx(self):
        raise NotImplementedError(f"missing rx_{self.state} method")

    def tx(self):
        raise NotImplementedError(f"missing tx_{self.state} method")

    # pause-resume rx/tx
    def pause_rx(self):
        self.kernel.fds_rx.pop(self.sock, None)

    def resume_rx(self):
        self.kernel.fds_rx[self.sock] = self

    def pause_tx(self):
        self.kernel.fds_tx.pop(self.sock, None)

    def resume_tx(self):
        if self._outgoing:
            self.kernel.fds_tx[self.sock] = self

    # I/O
    def _dispatch(self, msg):
        msg.decode()
        log.debug(f"dispatching: {msg}")

    def push(self, data):
        self._outgoing.append(data)
        self.resume_tx()

    def connection_lost(self, *args):
        self.kernel.delete(self.uri)
        if self.reconnect:
            self.kernel.retry(self.uri)


class UDPChannel(Channel):
    """UDP Support"""

    def rx_sync(self):
        raw, addr = self.sock.recvfrom(0x8000)
        # if not raw and addr is None:
        # self.connection_lost()

        log.debug(f"received {raw} from {addr}")

    def tx_sync(self):
        raise RuntimeError("pending of include 'address' for every message")


class BroadcasChannel(UDPChannel):
    """UDP Support"""

    def tx_sync(self):
        data = self._outgoing.popleft()
        print(f">> {data}")
        raw = pickle.dumps(data)
        address = self.sock.getsockname()
        self.sock.sendto(raw, address)
        not self._outgoing and self.pause_tx()


class TCPChannel(Channel):
    """TCP Support"""

    def rx_sync(self):
        raw = self.sock.recv(0x8000)
        if not raw:
            self.connection_lost()

        log.debug(f"received {raw}")
        self._raw += raw

    def tx_sync(self):
        raw = self._outgoing.popleft()
        print(f">> {raw}")
        self.sock.send(raw)
        not self._outgoing and self.pause_tx()


HTTP_HEADER_CUT = b"\r\n\r\n"
CONTENT_LENGTH = "Content-Length"

# https://www.geeksforgeeks.org/http-headers-content-encoding/?ref=lbp
CONTENT_ENCODING = "Content-Encoding"
HTTP_ENCODING = {
    "gzip": gz.decompress,  # It uses Lempel-Ziv coding (LZ77), with a 32-bit CRC format. It is the original format of UNIX gzip program.
    "compress": xz.decompress,  # It uses Lempel-Ziv-Welch (LZW) algorithm. Due to patent issue, many modern browsers don’t support this type of content-encoding.
    "deflate": zlib.decompress,  # This format uses zlib structure with deflate compression algorithm.
    #'br': 4, # It is a compression format using the Brotli algorithm.
    "identity": lambda x: x,  # no compression
    None: lambda x: x,  # no compression
}

# https://www.geeksforgeeks.org/http-headers-content-type/
CONTENT_TYPE = "Content-Type"
HTTP_TYPE_REG = {
    r'chartset': r'charset=(?P<charset>[\w\-]+)',

}

HTTP_TYPE_FUNC = {
    r'chartset': lambda body, charset, **kw: body.decode(charset),

}

class HTTPMessage(Message):
    """HTTP response messages"""
    def decode(self):
        body = self["body"]

        # decompress
        encoding = self.get(CONTENT_ENCODING)
        body = HTTP_ENCODING.get(encoding, HTTP_ENCODING["identity"])(body)

        # decode
        content_type = self.get(CONTENT_TYPE, '')
        for encoding, pattern in HTTP_TYPE_REG.items():
            m = re.search(pattern, content_type)
            if m:
                d = m.groupdict()
                func = HTTP_TYPE_FUNC.get(encoding)
                if func:
                    body = func(body, **d)

        self["body"] = body


class HTTPChannel(TCPChannel):
    HTTP_REQ = """GET {path} HTTP/1.1
Host: {host}
User-Agent: curl/7.54.0
Accept-Encoding: gzip, deflate


"""

    def __init__(self, *args, **kw):
        kw.setdefault("factory", HTTPMessage)
        super().__init__(*args, **kw)
        foo = 1

    # STATE_SYNC
    def _enter_sync(self):
        log.debug(f"1. sock: {self.sock}")
        log.info(f"GET {self.uri}")

        soft(self._uri, path="/")

        request = self.HTTP_REQ.format_map(self._uri)

        request = request.replace("\n", "\r\n")
        raw = bytes(request, "utf-8")
        log.debug(f"2. sock: {self.sock}")
        self.push(raw)
        # sleep(0.5)
        log.debug(f"3. sock: {self.sock}")

    def rx_sync(self):
        super().rx_sync()
        msg = self.message

        body_len = msg.get(CONTENT_LENGTH, False)
        if body_len:
            if len(self._raw) >= body_len:
                msg['body'] = self._raw[:body_len]
                self._raw = self._raw[body_len:]
                self._dispatch(msg)

            # read body
            foo = 1
        else:
            header = self._raw.split(HTTP_HEADER_CUT, 1)
            self._raw = header[-1]
            lines = header[0].splitlines()

            if not msg.get("status", False):
                line = lines.pop(0).split(b" ")
                msg["protocol"], msg["status"] = line[:2]

            # redirects = []
            # while True:
            # if self._raw[:4] == b"HTTP":
            ## TODO: what to do with redirects
            # redirects.append(header)
            # continue
            # break

            for line in lines:
                if line:
                    key, value = [
                        x.decode("ISO-8859-1").strip() for x in line.split(b":", 1)
                    ]
                    msg[key] = value
                else:
                    foo = 1

            if CONTENT_LENGTH in msg:
                msg[CONTENT_LENGTH] = int(msg[CONTENT_LENGTH])

            foo = 1

    # STATE_LIVE


class Subscripter(Protocol):
    def subscribe(self, uri, name=None):
        kernel = self.kernel
        source = kernel.allocate(uri)
        kernel.link(source, self, name)


class WQueue(dict, Subscripter):

    """The basic event handler for kernel."""

    def __init__(self, uri, kernel, handler, *args, **kwargs):
        self.last_wave = None
        self.handler = handler

        Subscripter.__init__(self, uri, kernel, *args, **kwargs)

        # signature
        # getfullargspec
        # sig = inspect.signature(handler)
        self.specs = inspect.getfullargspec(handler)
        if inspect.ismethod(handler):
            # is bounded, so remove 'self' parameter
            assert (
                self.specs.args[0] == "self"
            ), "bad convenience 'self' bound parameter?"
            self.specs.args.pop(0)

        self.n_inputs = len(self.specs.args)

    def __repr__(self):
        return f"<~{self.last_wave} : {self.uri}:{self.handler.__code__.co_name} [{len(self)}]>"

    def push(self, wave, inputs):
        """necesita conocer quienes alimentan a la cola.
        si hay parametros por defecto, ya que la funcion
        se puede completar solo con los que no tiene valor
        por defecto o hay que esperar si se asigna un flujo
        de entrada a una variable que tiene un valor por
        defecto.

            def func1(a, b, z=1):
                c = a + b

        si no se especifica flijo para "z", con a y b es suficiente.
        si se especifica un flujo para "z", entonces hay que esperar
        para tener las tres entradas.


        """
        # get the holder of the wave
        if wave not in self:
            assert self.last_wave is None or self.last_wave < wave
            self[wave] = holder = inputs
            self.last_wave = wave
        else:
            holder = self[wave]
            holder.update(inputs)

        if len(holder) == self.n_inputs:
            result = self.handler(**holder)
            self.pop(wave)
            if result is not None:
                self.kernel.push(wave, self, result)


class Kernel(Protocol):
    """Base of any Kernel:

    - handle I/O events.
    - handle timers
    - handle CPU bound processes.
    """

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        # self.scheduler = {}

        self.stats = Stats()
        self.t0 = 0
        self.time = 0

        # resources and factories
        self.factory = {}
        self.resources = {}
        self.alias = {}
        self._retry_allocate = deque()

    # runing loop
    def start(self):
        log.debug(">> start")
        self.state = STATE_INIT
        self.time = self.t0 = time()
        # time.process_time
        self._bootstrap()
        self.main()
        self.stop()

        log.debug("<< start")

    def main(self):
        raise NotImplementedError()

    def stop(self):
        pass

    def _bootstrap(self):
        keys = list(dir(self))
        keys.sort()
        for key in keys:
            # print(f" ---- {key} -----")
            func = getattr(self, key)
            m = re.match(f"(?P<fqname>_bootstrap_(?P<name>.+))", key)
            if m:
                d = m.groupdict()
                self._start_fiber(d["fqname"], func)

            m = re.match(
                f"(?P<fqname>(?P<basename>_pool_(?P<name>.+))(_(?P<number>\d+)?))", key
            )
            if m:
                d = m.groupdict()
                number = d["number"]
                if number:
                    for i in range(int(number)):
                        name = f"{d['basename']}-{i:02}"
                        wrap = functools.partial(func, name=name)
                        self._start_fiber(name, wrap)

    @property
    def elapsed(self):
        return self.time - self.t0

    def _start_fiber(self, name, func):
        log.debug(f"Starting fiber: '{name}'")
        func()

    # resource allocation
    def register_factory(self, pattern, allocator, deallocator, **defaults):
        self.factory[pattern] = allocator, deallocator, defaults

    def allocate(self, uri, alias=None):
        """Allocate a resource for this queue.

        uri determine the nature of the resource.

        clock:// ...
        tcp://....
        ssl://....
        ssh://....
        tws://....

        Kernel must implement this events based on its technology.

        - unix select + sockets
        - asyncio
        - curio
        - trio
        - ...

        But is transparent for all actors and providers as they
        will receive a data_received() call.

        """
        if uri in self.alias:
            return self.allocate(self.alias[uri])

        for pattern, (allocator, deallocator, defaults) in self.factory.items():
            m = re.match(pattern, uri)
            if m:
                kw = m.groupdict()
                _uri = parse_uri(uri)
                soft(kw, **defaults)
                resource = allocator(_uri, **kw)
                if resource:
                    assert resource.state in (
                        STATE_INIT,
                        STATE_SYNC,
                        STATE_TRANSITION,
                        STATE_LIVE,
                    )
                    # resource.next_state()
                else:
                    log.warn(f"Allocating Failled, uri: {uri}")

                self.alias[alias] = uri  # None means the last uri allocated
                return resource
        raise RuntimeError(
            "missing function for allocating '{scheme}' resource types".format_map(_uri)
        )

    def delete(self, uri):
        if uri in self.alias:
            return self.allocate(self.alias[uri])

        for pattern, (allocator, deallocator, defaults) in self.factory.items():
            m = re.match(pattern, uri)
            if m:
                kw = m.groupdict()
                _uri = parse_uri(uri)
                soft(kw, **defaults)
                result = deallocator(_uri, **kw)
                if not result:
                    log.warn(f"Deallocating Failled, uri: {uri}")
                for alias in list(self.alias):
                    if self.alias[alias] == uri:
                        self.alias.pop(alias)
                        break
                return result
        raise RuntimeError(
            "missing function for deallocating '{scheme}' resource types".format_map(
                _uri
            )
        )

    # retry allocation later on
    def retry(self, uri):
        self._retry_allocate.append(uri)


# ------------------------------------------------
# Wave Kernel
# ------------------------------------------------


class WKernel(Kernel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.queues = {}
        self.links = {}

        self.fds_rx = {}
        self.fds_tx = {}

        self.register_factory("timer://", self._allocate_timer, self._deallocate_timer)
        self.register_factory(
            "(udp)://<broadcast>",
            self._allocate_channel,
            self._deallocate_channel,
            klass=BroadcasChannel,
        )
        self.register_factory(
            "(tcp)://",
            self._allocate_channel,
            self._deallocate_channel,
            klass=TCPChannel,
        )
        self.register_factory(
            "(http|https)://",
            self._allocate_channel,
            self._deallocate_channel,
            klass=HTTPChannel,
        )

    # queues
    def register_queue(self, queue: WQueue):
        self.queues[queue.uri] = queue

    def main(self):
        """Main loop.

        - There is always 1 o more timers running (watchdog, etc)
        - timers rearms is always absolute (to preserve same waves across system)
        - timers waves starts are always on integer seconds time.
        -

        """
        log.debug(">> main")

        # RX handlers
        fds_rx = self.fds_rx
        fds_tx = self.fds_tx
        # Timers
        timers = self.resources["timer"]
        self.free_time = 0
        try:
            while self.state != STATE_TERM:
                remain = timers[0][0] - time()
                self.free_time += remain
                # log.debug(f" --- select for : {remain}")
                rx, tx, ex = select(fds_rx, fds_tx, fds_rx, remain if remain > 0 else 0)

                # check I/O
                for fd in ex:
                    print(f"error on : {fd}")
                    foo = 1

                for fd in tx:
                    fds_tx[fd].tx()

                for fd in rx:
                    fds_rx[fd].rx()

                # check timers
                t1 = time()
                while True:
                    t0, timer0 = timers[0]
                    if t0 > t1:
                        break

                    # rearm timer
                    timers.pop(0)
                    t00 = t0 + timer0.value
                    for i, (t2, timer2) in list(enumerate(timers)):
                        if t2 > t00:
                            timers.insert(i, (t00, timer0))
                            break
                    else:
                        timers.append((t00, timer0))

                    # handle timer after rearm, so
                    # kernel load can be better meassured
                    # timer0.push(t1)  # faster following implementation
                    self.push(t0, timer0, t0)  # direct using kernel

            # teardown ...
            # ...
        except Exception as why:
            exc_type, exc_value, exc_tb = sys.exc_info()
            tb = traceback.format_exception(exc_type, exc_value, exc_tb)
            tb = "".join(tb)
            # trace(message=tb, level=logging.ERROR, frames=2)

            log.exception(tb)
            self.state = STATE_TERM

        self.state = STATE_OFF
        log.debug("<< main")

    def _bootstrap_01_timers(self):
        log.debug(">> _bootstrap_timers")
        self.resources.setdefault("timer", [])
        log.debug("<< _bootstrap_timers")

    def _bootstrap_05_rxtx(self):
        log.debug(">> _bootstrap_rxtx")
        self.resources.setdefault("fds", {})
        log.debug("<< _bootstrap_rxtx")

    def _bootstrap_15_netbase(self):
        log.debug(">> _bootstrap_05_netbase")
        cfg = {"port": 53000}
        uri = "udp://<broadcast>:{port}".format_map(cfg)
        channel = self.allocate(uri, alias="broadcast")

        log.debug("<< _bootstrap_05_netbase")

    def _bootstrap_40_monitor(self):
        # while self.scheduler or self.running:
        # print(f"load: {len(self.scheduler)}")
        # data = {"scheduler": [len(q) for q in self.scheduler]}
        # t0 = int(self.elapsed)
        # self.stats.push(t0, data)
        # time.sleep(1)
        log.debug(">> _bootstrap_monitor")

        self.free_time = 0

        handler = WQueue("watchdog://default", self, self._watchdog_monitor)
        handler.subscribe("timer://localhost/secs/1")

        log.debug("<< _bootstrap_monitor")

    def _watchdog_monitor(self, t0):
        # log.debug(f" -- _watchdog_monitor: {t0}")

        busy = 1 - self.free_time

        quant = 0.01
        kernel_load = busy // quant

        # log.info(f"kernel load: {kernel_load}: free_time: {self.free_time}")
        self.free_time = 0
        self.stats.push(t0, {"load": kernel_load})
        self.stats.compute()

        if self._retry_allocate:
            uri = self._retry_allocate.popleft()
            log.info(f"Retry: {uri} : size: {len(self._retry_allocate)}")
            self.allocate(uri)

        # log.info(f"kernel means: {self.stats.means}")

    def push(self, wave, queue, result):
        # print(f"push: ~{wave} : {queue} : r={result}")
        holder = self.links.get(queue.uri, {})
        for target, param in holder.items():
            target_ = self.queues[target]
            target_.push(wave, {param: result})
        foo = 1

    def link(self, source, target, param=None):
        holder = self.links.setdefault(source.uri, dict())

        if param is None and target.specs.args:
            param = target.specs.args[0]

        holder[target.uri] = param

    # resource allocation
    def _allocate_timer(self, _uri):

        args = _uri["path"]
        m = re.match(r"/(?P<unit>([^/]+))/(?P<value>[^/]+)$", args)
        if m:
            d = m.groupdict()
            # prepare clock state
            muliplier = {
                "sec": 1,
                "secs": 1,
                "seconds": 1,
                "min": 60,
                "mins": 60,
                "minutes": 60,
                "hour": 3600,
                "hours": 3600,
            }
            assert d["unit"] in muliplier, "unknown clock unit {unit}".format_map(d)

            d["value"] = value = float(d["value"]) * muliplier[d["unit"]]
            d["unit"] = "sec"

            # search if timer already exists
            # holder = self.resources.setdefault(_uri["fscheme"], {})
            holder = self.resources[_uri["fscheme"]]
            for t0, timer in holder:
                if timer.value == value:
                    break
            else:
                # particular implementation
                uri = "timer://localhost/{unit}/{value}".format_map(d)
                # use int(time() for easy debugging
                # simple constructor. Do not add more params but uri
                timer = Timer(uri, self)
                assert timer.value == value
                holder.insert(0, (int(time()), timer))

                log.debug("Allocating: {fscheme}://{host}{path} ".format_map(_uri))

                # self.resources["min_clock"] = min(0.5, *holder.keys())

            # 1. connect()
            # state = {}
            # actor.connect(self, state)

            # 2. add a fwd link between kernel and actor
            # holder = self.by_scheme.setdefault(actor._uri["fscheme"], {})

            # holder.setdefault(value, []).append(actor)
            # self.link(source, target)

            return timer

    def _deallocate_timer(self, uri, **kw):
        raise NotImplementedError()

    def _allocate_channel(self, _uri, klass, **kw):
        uri = build_uri(**_uri)
        holder = self.resources.setdefault(_uri["fscheme"], {})
        channel = holder.get(uri)

        if not channel:
            try:
                channel = klass(uri, self, **kw)
                log.debug(f"0. sock: {channel.sock}")
                # assert timer.value == value
                holder[uri] = channel
                channel.resume_rx()
                # self.resources["fds"][channel.sock] = channel

                log.debug("Allocating: {fscheme}://{host}{path} ".format_map(_uri))

            except Exception as why:
                print(why)
                channel = None

            # self.resources["min_clock"] = min(0.5, *holder.keys())

        return channel

    def _deallocate_channel(self, _uri, **kw):
        args = _uri["host"]
        m = re.match(r".*$", args)
        if m:
            d = m.groupdict()
            holder = self.resources.setdefault(_uri["fscheme"], {})
            # uri = "timer://localhost/{unit}/{value}".format_map(d)

            uri = build_uri(**_uri)
            channel = holder.pop(uri, None)
            if channel:
                channel.pause_rx()
                channel.pause_tx()
                channel.sock.close()

            return True


class DemoKernel(WKernel):
    def __init__(self, uri="kernel://demo", kernel=None, *args, **kw):
        super().__init__(uri, kernel, *args, **kw)

    def _bootstrap_demo(self):
        log.debug(">> _bootstrap_demo")

        def func1(a, b):
            c = a + b
            return c

        def func2(a):
            return 2 * a

        def func3(x):
            log.info(x)
            # sleep(random.random() / 10)

        kernel = self
        q1 = WQueue("demo://demo/1", kernel, func2)
        q2 = WQueue("demo://demo/2", kernel, func2)
        q3 = WQueue("console://demo/1", kernel, func3)

        # build workflow
        q1.subscribe("timer://localhost/secs/5", "a")
        kernel.link(q1, q2)
        kernel.link(q2, q3)

        log.debug("<< _bootstrap_demo")

    def __bootstrap_tcp_client(self):
        log.debug(">> _bootstrap_tcp_client")
        cfg = {"port": 52000}
        uri = "tcp://localhost:{port}".format_map(cfg)
        channel = self.allocate(uri)

        log.debug("<< _bootstrap_tcp_client")

    def __bootstrap_udp_time_server(self):
        log.debug(">> _bootstrap_udp_time_server")
        cfg = {"port": 52000}

        def func1(t):
            channel = self.allocate("broadcast")
            log.info(f"time-server: {channel.uri}: {t}")
            channel.push(t)

        kernel = self
        q1 = WQueue("beacon://localhost/time-server", kernel, func1)
        q1.subscribe("timer://localhost/secs/2", "t")

        log.debug("<< _bootstrap_udp_time_server")

    def _bootstrap_http_pages(self):
        log.debug(">> _bootstrap_http_pages")

        for uri in [
            # "http://mnt:4080",
            #"https://www.python.org:443",  #
            "https://www.debian.org:443",  # 20 secs inactivity closing
        ]:
            channel = self.allocate(uri)
            foo = 1

        log.debug("<< _bootstrap_http_pages")


# ------------------------------------------------
# Antiguo kernel
# ------------------------------------------------
class NOQUEUE:
    pass


class DemoKernel_old(WKernel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.fibers = {}  # the running fibers (if any)

    def _start_fiber(self, name, func):
        th = threading.Thread(name=name, target=func)
        self.debug(f"Starting fiber: '{name}'")
        th.start()
        self.fibers[name] = th

    def stop(self):
        self.running = False
        # wait all fibers stop
        remain = True
        while remain:
            time.sleep(0.1)
            remain = [th.is_alive() for th in self.fibers.values()]
            remain = any(remain)

    def put(self, url, event):  # TODO: review
        queue = self.queues.get(url)
        if queue is None:
            pass
        else:
            queue.put(event)
            self.scheduler.add(queue)

    def get(self, url):  # TODO: review
        queue = self.queues.get(url)
        if queue is None:
            event = NOQUEUE
        else:
            event = queue.get()
        return event

    def _pool_workers_3(self, name):
        log.debug(f">> {name}")
        n = 0
        while self.scheduler or self.running:
            # try to get a queue to dispatch an event
            try:
                # TODO: use queues instead deque
                queue = self.scheduler.pop()
                while True:
                    event = queue.get()
                    # print(f"{name}: got {event}")
                    if not n % 500:
                        log.debug(f"- {name}: {n} done.")
                    # do the 'task'
                    time.sleep(event * 0.005)
                    n += 1
            except IndexError as why:
                time.sleep(random.random() * 0.2)
                foo = 1

        log.debug(f"<< {name}: {n} works done!")

    def _loop_bootstrap(self):
        log.debug(">> loop_bootstrap")

        queue = TQueue(url="A")
        self.register_queue(queue)

        queue = TQueue(url="B")
        self.register_queue(queue)

        self._start_fiber("demo", self._demo)

        while self.running:
            # log.debug("---")
            time.sleep(1)
        log.debug("<< loop_bootstrap")

    def _demo(self):
        self.put("A", 3.1415)
        self.put("A", 1.4142)

        log.debug(self.get("A"))
        log.debug(self.get("A"))

        while self.running:
            time.sleep(random.random() * 0.002)
            self.put("B", random.random())
        foo = 1


if __name__ == "__main__":
    # no merece la pena usar decoradores para intentar pasarle
    # un contexto a la funcion de ejecucion.
    # mejor hacerlo en cada llamada. no nos vamos a ahorrar tiempo.
    ctx = dict(b=1)

    def handler(func):
        def wrapper(*args, **kw):
            # code = func.__code__
            # for missing in code.co_varnames[len(args):code.co_argcount]:
            # kw[missing] = ctx[missing]
            return func(*args, **kw)

        return wrapper

    @handler
    def func00(a, b):
        c = a + b
        return c

    z = func00(1, 2)

    foo = 1
# End
