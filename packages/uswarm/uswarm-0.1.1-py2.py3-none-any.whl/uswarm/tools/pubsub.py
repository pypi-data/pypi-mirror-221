from weakref import WeakSet, WeakValueDictionary

from curio.meta import awaitable, asyncioable


from uswarm.definitions import timeframe2delta
from uswarm.tools.abc import Any
from uswarm.tools.calls import scall
from uswarm.tools.containers import walk

# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger

log = logger(__name__)


# --------------------------------------------------
# iPubSub
# --------------------------------------------------
SET = set
DICT = dict


class iPubSub(Any):
    """Base interface for Publication / Subscription paradigm.

    This class only manages :

    - add/remove subcriptor instances to a "port".
    - push a message to a "port".
    - deliver the message to each listener queue.
    - a "port" can be anything hashable: uri, str, int, etc.

    This class assume all subcriptors are classes that support
    "push" mechanism.

    There is no assumption on how the messages will be processed.

    (quues, threading, curio, etc)

    - as ports are stored in a dict, there is no lack of performance
    sharing all ports for the whole process space, that means we can
    share ports across different threads.

    - class methods provide broker/publisher support.
    - instance methods provide target support.

    """

    # --------------------------------------------------
    # Listener support (shared among class instances)
    # --------------------------------------------------

    PORTS = DICT()

    # --------------------------------------------------
    # topology
    # --------------------------------------------------
    def subscribe(self, *ports, since=None):
        """subscribe self instance to a port."""
        # TODO: check WeakSet() speed vs set() speed
        for target in ports:
            port = self.getuid(target)
            subs = self.PORTS.setdefault(port, SET())
            subs.add(self)

    def unsubscribe(self, *ports, since=None):
        """remove self instance for listening in some ports.
        pass nothing for unsubscribe to all listening ports.
        """
        ports = ports or list(self.PORTS.keys())
        for target in ports:
            port = self.getuid(target)
            subs = self.PORTS.get(port) or WeakSet()
            subs.discard(self)
            if not self.PORTS.get(port):
                self.PORTS.pop(port, None)

    def getuid(self, target):
        if isinstance(target, iPubSub):
            return f"{id(target):x}"
        return target

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    # --------------------------------------------------
    # sender
    # --------------------------------------------------
    def publish(self, data, *ports):
        """publish a message to a port."""
        for port in ports:
            subs = self.PORTS.get(port) or set()
            for target in subs:
                # sender = self
                target.push(data, _port_=port, _sender_=self)

    # --------------------------------------------------
    # Receiver
    # --------------------------------------------------
    def push(self, data, _port=None, _sender=None, *args, **kw):
        """Receive a message from external source, mainly from
        calls to publish() in another connected instance.

        - This method is synchronous
        """
        self._forwards(data, _port=_port, _sender=_sender, *args, **kw)

    @awaitable(push)
    async def push(self, data, _port=None, _sender=None, *args, **kw):
        """Receive a message from external source, mainly from
        calls to publish() in another connected instance.

        - This method is synchronous
        - TODO: use @awaitable for async Implementation
        """
        self._forwards(data, _port=_port, _sender=_sender, *args, **kw)

    def _forwards(self, result, channel="live", *args, **kw):
        """Forwards output delta to subscribed nodes."""
        default_port = self.getuid(self)
        self.publish(result, default_port)


# --------------------------------------------------
# iSync interface
# --------------------------------------------------


class iProcessor(iPubSub):
    """A Pub/Sub node that process the received data and maybe generate a
    rerults which will be then forwarded to next nodes.

    This class can be used as a base for:

    - filtering or transforming data before being sent to following nodes.
        i.e convolution, valiable condesation, etc.

    - received data from multiples nodes and wait until some pieces are
      complete before forwarding to next nodes.
        i.e. join partial waves to create an unified stream.

    """

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    # ----------------------------------------------------------------
    # Receiver
    # ----------------------------------------------------------------
    def push(self, data, *args, **kw):
        """Push a partial wave-data through the pipeline.

        When a data-wave is completed, then data is dispatched
        and its result are (optionally) stored in the dataframe
        repository.
        """
        for wave in self._analyze(data, *args, **kw):
            self._dispatch(wave, *args, **kw)

    @awaitable(push)
    async def push(self, data, *args, **kw):
        """Push a partial wave-data through the pipeline.

        When a data-wave is completed, then data is dispatched
        and its result are (optionally) stored in the dataframe
        repository.
        """
        for wave in await self._analyze(data, *args, **kw):
            await self._dispatch(wave, *args, **kw)

    # --------------------------------------------------
    # Waves
    # --------------------------------------------------
    def _analyze(self, message, *args, **kw):
        """Analyze incoming message and return what processors really want
        to be processed (i.e, consolidated data, parial wave, filtered data, etc)
        """
        return [message]

    @awaitable(_analyze)
    async def _analyze(self, message, *args, **kw):
        """Analyze incoming message and return what processors really want
        to be processed (i.e, consolidated data, parial wave, filtered data, etc)
        """
        return [message]

    # --------------------------------------------------
    # Data procesing
    # --------------------------------------------------
    def _dispatch(self, wave, *args, **kw):
        """In the same function we *dispatch* the message:

        - get the results of the incoming message.
        - optionally delegate handle result locally (NOP by default)
        - forwards results to its children (listeners)
        """
        result = self._process(wave, *args, **kw)

        # handle result locally (is any)
        # in addition results may change before forwarding to next nodes
        result = self._handle_results(result, *args, **kw)

        # fwd data to subscribed nodes
        self._forwards(result, *args, **kw)

    @awaitable(_dispatch)
    async def _dispatch(self, wave, *args, **kw):
        """In the same function we *dispatch* the message:

        - get the results of the incoming message.
        - optionally delegate handle result locally (NOP by default)
        - forwards results to its children (listeners)
        """
        result = await self._process(wave, *args, **kw)

        # handle result locally (is any)
        # in addition results may change before forwarding to next nodes
        result = await self._handle_results(result, *args, **kw)

        # fwd data to subscribed nodes
        self._forwards(result, *args, **kw)

    def _process(self, wave, *args, **kw):
        """Process incoming message"""
        return wave

    @awaitable(_process)
    async def _process(self, wave, *args, **kw):
        """Process incoming message"""
        # curio trick
        return self._process._syncfunc(self, wave, *args, **kw)

    def _handle_results(self, result, *args, **kw):
        """handle result locally (is any).
        do nothing by default.
        """
        return result

    @awaitable(_handle_results)
    async def _handle_results(self, result, *args, **kw):
        """handle result locally (is any).
        do nothing by default.
        """
        return self._handle_results._syncfunc(self, result, *args, **kw)


class iPersistentProcessor(iProcessor):
    """A processor that may save its results into a storage
    before sending to next nodes.

    """

    def __init__(self, storage=None, _method_="write", *args, **kw):
        super().__init__( *args, **kw)

        self._storage = storage
        self._dumper = getattr(storage, _method_, None)
        foo = 1

    # --------------------------------------------------
    # Data procesing
    # --------------------------------------------------
    def _handle_results(self, result, *args, **kw):
        """update the output mem-holder (i.e. dataframe, etc).
        Doing this DOES NOT implies *edge* will be moved.

        Default option for iSync is trying to flush data into repository

        """
        self._dumper and self._dumper(result)
        return result

    @awaitable(_handle_results)
    async def _handle_results(self, result, *args, **kw):
        return self._handle_results._syncfunc(self, result)
