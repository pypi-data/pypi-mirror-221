"""

Kurio Kenel:

- [x] Is based on curio asynchronous library.
- [ ] uses a YAML configuration file for bootstrap.
- [ ] YAML configuration describes the resources URI to be created on startup.
- [ ] kernel keep track of YAML configuration and restart itself when is needed.
- [ ] kernel basically launch main entry points from different plugings (aka modules)
- [ ] these modules are responsible for prepare and launch all other *fibers* that performs the work.
- [ ] Keep a rollback YAML configuration before starting the new one.
- [ ] Every resource needs to implement a sanity check method to be polled by kernel.
- [ ] Response wil be ok, warning, critical, shutdown.

Future:

- Differential YAML checking to stop/restart only the plugings affected.


- [ ] extend dataframe for creating devices.
- [ ] Create *devices* that exposes its own functionality in a df
- [ ] create a synthetic broker
- [ ] use curio async to connect synbroker
- [ ] symbroker stores its own auto-generated data in a internal df
- [ ] create

TODO: merge into kurio/kernel ?

"""
import inspect
from time import time
from weakref import WeakSet

from .kernel import iKernel, Config, sleep, spawn, run, Queue, Event

from curio import Kernel as curio_kernel
from curio.meta import instantiate_coroutine

# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger

log = logger(__name__)

# ------------------------------------------------
# Definitions
# ------------------------------------------------
async def until(
    expression,
    _globals=None,
    _locals=None,
    timeout=float("inf"),
    _raise: bool = True,
    max_polling=1,
):
    """Awaits until a condition is True.

    cond = await until('klass.HITS == S * N or not kernel.running')

    """

    exp = compile(expression, "<string>", "eval")
    _globals = globals() if _globals is None else _globals
    if _locals is None:
        frame = inspect.stack()[1][0]
        _locals = frame.f_locals

    seconds = 0
    t1 = time() + timeout
    cond = eval(exp, _globals, _locals)
    while not cond:
        # print(f"until: {seconds} ....")
        await sleep(seconds)
        seconds += (max_polling - seconds) * 0.01
        if time() > t1:
            if _raise:
                raise TimeoutError()
            else:
                break
        cond = eval(exp, _globals, _locals)
    return cond


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


EVENTS = set(["new", "update", "resurected", "deleted"])


class Node:  # TODO: delete?
    """Basic node"""

    def __init__(self, *args, **kw):
        self._f = {
            "new": self._new_,
            "update": self._update_,
            "resurrected": self._resurrect_,
            "deleted": self._delete_,
        }

    async def g(self):
        raise NotImplementedError()

    def _new_(self, delta):
        raise NotImplementedError()

    def _update_(self, delta):
        raise NotImplementedError()

    def _resurrect_(self, delta):
        raise NotImplementedError()

    def _delete_(self, delta):
        raise NotImplementedError()


class Device(Node):  # TODO: delete?
    """Basic node"""

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)


# --------------------------------------------------
# Kernel
# --------------------------------------------------
class Kernel(iKernel):
    def __init__(
        self, uri: str, kernel: iKernel = None, config: Config = None, *args, **kw
    ):
        super().__init__(uri=uri, kernel=kernel, config=config, *args, **kw)
        self._kernel = None
        self._pending_fibers = []
        self._running_tasks = {}
        self._outside_tasks = set()

    def init(
        self, path: str = None, config: Config = None, extra_fibers: list = None, **kw
    ):
        """main entry point for kernel loop.

        - let base class prepare all starting fibers.
        - star a cuiro kernel and run async main loop.
        """
        super().init(path, config, extra_fibers, **kw)

        self._kernel = curio_kernel()
        with self._kernel as kernel:
            kernel.run(self.main(extra_fibers=extra_fibers))

    # --------------------------------------------------
    # Kernel
    # --------------------------------------------------
    def _start_fiber(self, name, func, *args, **kw):
        """Fire a function in a *parallel-light-fiber* when is possible.
        Just execute function by default.
        """
        log.debug(f"Starting fiber: '{name}': {args}, {kw}")
        coro = instantiate_coroutine(func, *args, **kw)
        self._pending_fibers.append(coro)

    # --------------------------------------------------
    # Main Loop
    # --------------------------------------------------
    async def _preconfigure(self):
        await super()._preconfigure()
        self._running_tasks = self._kernel._tasks
        self._outside_tasks = set(self._running_tasks)

        self.running = True


    async def _loop(self):
        """
        Shutting down kernel means wait for task to end

        In order to avoid duplicate memory, we can find the
        needed information in curio kernel:

        >>> self._kernel._tasks
        {1: Task(id=1, name='Kernel._make_kernel_runtime.<locals>._kernel_task', state='READ_WAIT'),
         2: Task(id=2, name='Kernel.main', state='RUNNING'),
         3: Task(id=3, name='DemoBroker.main', state='TIME_SLEEP'),
         4: Task(id=4, name='HeartBeat.main', state='TIME_SLEEP'),
         5: Task(id=5, name='Kernel._bootstrap_101_network', state='TIME_SLEEP'),
         6: Task(id=6, name='Kernel._bootstrap_101_heartbeat', state='TIME_SLEEP')}

         1: the curio runnner itself
         2: this 'main' function (the only in RUNNING state)
         3-6: tasks launched AFTER main (aka fibers)

        """
        #self._preconfigure()
        #self._bootstrap(extra_fibers=extra_fibers)

        # enters in main loop
        seconds = 0.1
        end = self.config.sg("main/shutdown", float("inf"))
        log.info(f"Kernel will ends in {end} secs")
        end += self.time
        while self.running == True and self.time < end:
            self.time = time()
            # launch all pending fibers
            while self._pending_fibers:
                fiber = self._pending_fibers.pop()
                task = await spawn(fiber, daemon=True)  # False: can be joined
                seconds = 0
            await sleep(seconds)
            seconds += (1 - seconds) * 0.1
        log.info(f"Kernel: {self.uri} ends nicelly")
        self.running = False
        # TODO: wait until all launched fibers ends too

    async def _term(self):
        last_msg = ""
        # timeout waiting task to end
        t1 = time() + self.config.sg("main/term-timeout", 10)
        while (pending := self.stats()["running"]) and (remain := t1 - time()) > 0:
            msg = f"waiting running: {pending} fibers"
            msg != last_msg and log.info(
                (last_msg := msg) + f", kill timeout in : {remain:0.1f} s"
            )
            await sleep(0.5)
        log.info(f"Kernel: {self.uri} is stopped")

    # --------------------------------------------------
    # Monitors
    # --------------------------------------------------
    def stats(self) -> dict:
        """Return info from running fibers"""
        tasks = self._kernel._tasks
        running = {}

        for tid in self._outside_tasks.symmetric_difference(self._running_tasks):
            task = tasks[tid]
            running[tid] = (
                task.parentid,
                task.cycles,
                task.state,
                task.name,
                task.where(),
            )

        return {"running": running}

    # --------------------------------------------------
    # Kernel Bootstraping
    # --------------------------------------------------
    async def _bootstrap_101_heartbeat(self):
        log.debug(f"Staring Heartbeat...")
        while self.running:
            log.debug(f"heartbeat: {self.time}")
            await sleep(5)

    async def _bootstrap_101_network(self):
        log.debug(f"Staring Networking...")
        while self.running:
            log.debug(f"net      : {self.time}")
            await sleep(3)
