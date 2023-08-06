from abc import abstractmethod

from ..definitions import timeframe2delta
from .resource import iResource, Queue
from .resource import awaitable, asyncioable
from ..tools.pubsub import iPubSub

# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger

log = logger(__name__)


class ePubSub(iPubSub, iResource):
    """Implementation using iResources."""

    # --------------------------------------------------
    # instance support
    # --------------------------------------------------

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._queue = Queue()

    async def main(self):
        queue = self._queue
        while self.kernel.running:
            wave = await queue.get()
            await self._dispatch(wave)
            # note: we never use queue.task_done() for faster execution
            # so publisher will never wait for queue.join()
            # as side effect, queue._task_count shows the number of
            # executions by the queue
            # if publisher needs to wait can poll directly
            # the number of items in queue.

    # --------------------------------------------------
    # instance abstract methods
    # TODO: unify in base class with @awaitable
    # --------------------------------------------------
    async def _dispatch(self, message, _port=None, _sender=None, *args, **kw):
        """In the same function we *dispatch* the message:

        - get the results of the incoming message.
        - optionally delegate handle result locally (NOP by default)
        - forwards results to its children (listeners)
        """

        result = self._process(message, _port, _sender, *args, **kw)
        # handle result locally (is any)
        self._handle_results(result, _port, _sender, *args, **kw)

        # fwd data to subscribed nodes
        self._forwards(result, *args, **kw)


class iWaver(ePubSub):
    """PubSub based on coherents waves of information.
    - Information flows in waves that share same key (wkey)
    - wkey is monotonal and an be predicted what is the next one from a particular one.
    - wave-parta data is assembled and yieled in order as 'next-key' is completed.
    - other wave-parts are waiting to be completed and fired in the right moment.


    _push and _dispatch methods are splitted from base class.
    """

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._incompleted_waves = {}
        self._last_wave = None

    async def _push(self, message, _port_=None, _sender_=None):
        """Check for completeness of message/wave"""
        # add partial-wave to waves database
        wave = self._get_wave(message)
        wmsg = self._incompleted_waves.setdefault(wave, {})
        wmsg[_port_] = message  # keep port origen to easy wave completeness

        # check for completeness of the next wave to be processed
        wmsg = self._wave_ready()
        while wmsg is not None:
            # rebuild message from its parts
            message = {}
            for part in wmsg.values():
                message.update(part)
            # and deliver it to be processed
            # await self._put(message)
            await self._queue.put(message)  # faster

            # continue if the next wave ir also ready
            wmsg = self._wave_ready()

    def _get_wave(self, message):
        wave = message.get("_wave_", None)
        if self._last_wave is None:
            self._last_wave = wave
        return wave

    def _wave_ready(self):
        """try to get the next-order wave that must be processed."""
        wmsg = self._incompleted_waves.get(self._last_wave)
        if wmsg is not None and self._is_completed(wmsg):
            wmsg = self._incompleted_waves.pop(self._last_wave)
            self._next_wave()
            return wmsg

    def _is_completed(self, wmsg):
        return len(wmsg) > 0  # 1+ ports has placed its data into wave

    def _next_wave(self):
        # self._last_wave += 1
        raise NotImplementedError()

    async def _put(self, message):
        await self._queue.put(message)

    async def _dispatch(self, message):
        print(f"message: {message}")
        foo = 1


class iTimeWaver(iWaver):
    def __init__(self, tf: str = "1s", *args, **kw):
        super().__init__(*args, **kw)
        self.tf = tf
        self._delta = timeframe2delta(self.tf)

    def _next_wave(self):
        """try to get the next-order wave that must be processed."""
        self._last_wave = self._last_wave + self._delta
