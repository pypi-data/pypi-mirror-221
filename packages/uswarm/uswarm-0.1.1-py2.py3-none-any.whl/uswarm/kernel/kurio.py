from curio import run, sleep, Queue, Event, TaskGroup


class XQueue(Queue):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._ev_empty = Event()

    def extend(self, iterable):
        self._queue.extend(iterable)

    async def get(self):
        result = super().get()
        if self.empty():
            self._ev_empty.set()
        return result

    async def put(self, item):
        super().put(item)
        self._ev_empty.clear()


# ---------------------------------------------
# Multi Pub/Sub with Synchronization
# ---------------------------------------------

STATE_LIVE = "live"
STATE_SYNC = "sync"


class Port:
    def __init__(self):
        self._queue = {
            STATE_LIVE: Queue(),
        }
        self._subscribers = {
            STATE_LIVE: {},
        }

    async def main(self, state=STATE_LIVE):
        while True:
            msg = await self._queue[state].get()
            for name, q in self._subscribers[state].items():
                await q.put(msg)

    def push(self, data, state=STATE_LIVE):
        self._queue[state].put(data)

    pass
