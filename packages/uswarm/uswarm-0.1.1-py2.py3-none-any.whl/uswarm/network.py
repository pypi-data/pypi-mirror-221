"""Network module.

- [ ] remove finished rid from signature _cache

"""
import re
import ssl
import time
import traceback
import yaml

from datetime import datetime
from asyncio import sleep, get_running_loop, Protocol, Future
from asyncio import gather, sleep, wait_for, TimeoutError

from weakref import WeakValueDictionary as wvdick

#from .tools.containers import Dom, Dict
from .reactor import Worker, Reactor, Executor, Message, Encoder, Decoder
from .reactor import parse_uri, build_uri, soft
from .pools import TBDPool
from .parsers import dict_decode


class TransportExecutor(Executor):
    """Encapsulate a Transort as remote executor"""

    def __init__(self, transport, **env):
        self.transport = transport
        pass


class StreamMessage(Message):
    def __init__(self, api, **kw):
        super().__init__(api, **kw)
        self.header_completed = False
        self.length = -1
        self.raw = b""

    def feed(self, raw):
        pass  # raise NotImplementedError("override")


class Api(Worker, Protocol):
    """An active Protocol.

    Notes:

    - event can use datagrams the design is oriented
      to streamed api like HTTP.

    - undelaying datagram transport can be used as
      stream protocol like RTBL.


    """

    def __init__(self, reactor, persistence=None, **env):
        Worker.__init__(self, **env)
        Protocol.__init__(self)

        # Protocol init
        self.transport = None

        # TODO: review attributes
        self._next_rid = 100
        self._cache = {}

        self.encoder = Encoder()
        self.decoder = Decoder()

        self.env["api"] = self  # for messages accesing api

        # function handlers
        self.handler = {}
        self._populate_handlers()

        # persistence = persistence or f'{self.__class__.__name__}.yml'
        self.persistence = persistence

        # Handshaking
        self.handshaking = None  # self.loop.create_future()  # TODO: datagram peers?
        self._handshaking_flags = {}

        # Disconnection
        self.disconnection = None  # self.loop.create_future()

        # add Worker to reactor
        reactor.attach(self)

    def save_dom(self):
        if self.persistence:
            yaml.dump(
                self.dom, stream=open(self.persistence, "wt"), default_flow_style=False
            )

    async def _enter(self):
        assert not isinstance(self, Reactor)
        await super()._enter()

        # TODO: review when save DOM
        # self.attach(self._do_save())  # TODO: remove from protocols...!

    async def _do_save(self):
        """TODO: remove from protocols"""
        while self.running:
            await sleep(5)
            # yaml.dump(self.dom, stream=open(f'{self.name}.yml', 'wt'), default_flow_style=False)
            self.save_dom()
            foo = 1

    # ----------------------------------
    # Protocol
    # ----------------------------------
    def connection_made(self, transport):
        """Called when a connection is made.

        - store transport.
        - prepare future flags for: handshaking, disconnection
        - prepare all flags needed for handshaking.
        - launch async handshaking procedure.

        The results will be:

        1. all handshaking requirements completed, so
           handshaking flag will be set to True.
           The open() method will be awaken and
           process will continue.

        2. timeout:
           handshaking flag will be set to False
           transport will be closed.
           disconnection flag will be set to True by
           connection_lost() deferred call.

        """
        # print("connection!")

        # start handshaking
        self.transport = transport

        # set the deferred handshaking
        # and disconnection futures creation
        # ('loop' now exists)
        for name in "handshaking", "disconnection":
            assert getattr(self, name) is None, "must be defined prior set"
            setattr(self, name, self.loop.create_future())

        # set handshaking pre-requisites
        self._set_handshaking_requirements()

        # launch handshaking procedure
        self.attach(self._do_handshaking())

    def data_received(self, data):
        pass  # raise NotImplementedError("Must be overriden")

    def connection_lost(self, exc):
        """Called when the connection is lost or closed.
        It also call self.stop()

        """
        super().connection_lost(exc)
        self.disconnection.set_result(True)

        self.stop()

    # ----------------------------------
    # Protocol Extended
    # ----------------------------------
    async def _do_handshaking(self, timeout=5):
        """Wait until all handshaking *flags* has been set.

        TODO: If timeout case ...
        """
        try:
            await wait_for(self.handshaking_completed(), timeout)
            self.handshaking.set_result(True)
            return
        except TimeoutError as why:
            print("-" * 100)
            print(why)
            print("-" * 100)

        except Exception as why:
            print("-" * 100)
            print(why)
            print("-" * 100)

        self.handshaking.set_result(False)
        self.transport.close()

    def _set_handshaking_requirements(self):
        """Set the futures needed *flags* for a completed handshaking.

        Example:

            self._handshaking_add_flags(
                IN.NEXT_VALID_ID,
                IN.MANAGED_ACCTS)
            super()._set_handshaking_requirements()

        """
        foo = 1

    def _handshaking_add_flags(self, *flags):
        """Create all future flags needed in handshaking"""
        for f in flags:
            # self._handshaking_flags[TWSMessage.in_mapping[f]] = self.loop.create_future()
            self._handshaking_flags[f] = self.loop.create_future()

    async def handshaking_completed(self):
        """Wait until all required handshaking *flags* have been set.

        When a protocol requires some handshaking it must implement these
        requirements as a list of *flags* that must be set before we condiser
        the protocol is in a ready-to-use state.

        This is implemented by *_set_handshaking_requirements()* function.

        """
        await gather(*self._handshaking_flags.values())
        foo = 1

    def _write(self, raw):
        """Low level transport writting."""
        # print(f' >>> Data send: {raw[:30]} ... : {len(raw)}')
        self.transport.write(raw)

    # ----------------------------------
    # Dispatcher
    # ----------------------------------
    def _dispatch(self, msg):
        """Try to dispatch a completed incoming message.
        A waiting response may need several messages to
        be 100% complete (e.g. HTTP 206 partials)
        """
        return super()._dispatch(msg)

    def _populate_handlers(self):
        """Populate incoming messages handlers"""
        super()._populate_handlers()

    def parse(self, msg):
        """Parse raw and generaty a body (payload)"""
        assert False, "retire"
        path = self.in_mapping.get(msg.get_handler_code())
        types = self.extract.get(path) or self.extract["default"]
        dom = msg.parse(types)
        # print(f"  - result: {dom}")

    # ----------------------------------
    # Sequencer
    # ----------------------------------
    def stop(self):
        """Stop the API worker"""
        if self.running:
            # assert self.transport._sock
            try:
                self.transport.close()
            except Exception as why:
                print(f"eerroorr: {why}: {why.__class__}")
                time.sleep(5)
                foo = 1

            foo = 1
        else:
            foo = 1
        super().stop()

    # ----------------------------------
    # Worker ?
    # ----------------------------------

    # ----------------------------------
    # Api
    # ----------------------------------
    async def _watch_dom(self, path, timeout=5):
        t1 = time.time() + timeout
        while path not in self.dom:
            await sleep(0.51)
            if time.time() > t1:
                self.handshaking.set_exception(
                    RuntimeError("timeout waiting for next_id")
                )


class StreamedApi(Api):
    def __init__(self, reactor, **env):
        super().__init__(reactor, **env)
        self._buffer = b""  # binary
        # streamed protocols can have only one single
        # incoming message in progress
        self._wip_message = self.INCOMING_KLASS(self)

    # ----------------------------------
    # Protocol
    # ----------------------------------
    def connection_made(self, transport):
        super().connection_made(transport)

    def data_received(self, data):
        """Real data received when handshaking is done"""
        self._buffer += data
        # print(f' <<< Data received: {data[:99]} ... : {len(data)}')

        # try to complete the incoming message
        while self._buffer:
            incoming = self._wip_message
            self._buffer = incoming.feed(self._buffer)

            if incoming.body:  # is completed
                self._dispatch(incoming)
                self._wip_message = self.INCOMING_KLASS(self)
            else:
                break

            # print(f"- Retire rid: {rid}")
            # TODO: use relative paths for updating DOM...
            # TODO review: self.dom.update(**res.result())

    def connection_lost(self, exc):
        super().connection_lost(exc)

    # ----------------------------------
    # Protocol Extended
    # ----------------------------------

    # ----------------------------------
    # Worker
    # ----------------------------------
    def _change_message_klass(self, klass):
        super()._change_message_klass(klass)
        if self._wip_message.raw:
            raise NotImplementedError(
                "you can not change the message klass in the"
                "middle of an incoming message"
            )
        self._wip_message = self.INCOMING_KLASS(self)


class DatagramApi(Api):
    def __init__(self, reactor, dom=None, **env):
        super().__init__(reactor, dom, **env)
        # datagram protocols may have multiples incoming messages
        # at the same time (e.g. RTBL protocol)
        self.incoming = {}  # messages in progress from remote peer

    def data_received(self, data):
        """Real data received when handshaking is done"""
        pass  # raise NotImplementedError("need to be overriden")


class NetWorker(Reactor):
    protocols = {
        # 'http': {'klass': HTTPClient, 'port': 80},
        # 'https': {'klass': HTTPSClient, 'port': 443}
    }

    @classmethod
    def register(cls, scheme, data):
        cls.protocols[scheme] = data

    async def open(self, urls, dom=None, klass=None, _quiet_=True, _timeout_=5, **req):
        """Open a generic URL with associated protocol."""
        if isinstance(urls, str):
            urls = [urls]

        loop = get_running_loop()
        for url in urls:
            try:
                info = parse_uri(url)
                if req:
                    #: need to parse args and merge together
                    _req = dict(req)
                    _req.update(info["query_"] or {})

                    # args = "&".join([f"{k}={v}" for k, v in _req.items()])
                    _req.update(info)
                    url = build_uri(**_req)
                    # if args:
                    # url = f"{url}?{args}"

                if not _quiet_:
                    print(f"> Trying to connect to: {url}")

                if not klass:
                    d = dict(self.protocols[info["scheme"]])
                    soft(info, **d)
                    klass = info["klass"]

                info["port"] = int(info["port"])

                if info["scheme"] in ("https",):
                    sc = ssl.create_default_context()
                else:
                    sc = None

                transport, proto = await loop.create_connection(
                    lambda: klass(self, dom=dom, name=url, loop=self.loop, **info),
                    info["host"],
                    info["port"],
                    ssl=sc,
                )
                # wait until handshaking is done
                # print("haciendo handshaking...")
                try:
                    # TODO: review 115 secs?
                    await wait_for(proto.handshaking, _timeout_)
                    return transport, proto

                except Exception as why:
                    print("=" * 100)
                    print(f"{why.__class__}: {why}")
                    print("=" * 100)
                    proto = None  # TODO: review
                    transport.close()

            except Exception as why:
                if not _quiet_:
                    self.error(f" Error: {why}", _raise_=None)
                    traceback_output = traceback.format_exc()
                    # Now you can print it, or send it, or save it in a file
                    self.error(traceback_output, _raise_=None)
                raise

        raise ConnectionError(f"Unable to connect to {urls}")


# ------------------------------------
# Pools
# ------------------------------------


class TBDServerPool(TBDPool):
    async def _enter(self):
        await super()._enter()
        assert isinstance(self.reactor, NetWorker), "needed for opening connections"

    async def _activate(self, item):
        super()._activate(item)

        # try to connect to a server
        async with timeout(self.delay) as cm:
            transport, protocol = self.reactor.open(item)

        if cm.expired:
            self._update(item, self.DOWN, None, self.time + 10 * self.PACING)
        else:
            self._update(item, self.READY, protocol)

        return self.status[item][1]
