"""Kenel module.

# misc

- [ ] print uri resource maps
- [ ]

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

import random
import traceback
import yaml
import functools
import inspect
import gc
import sys
import hashlib

from time import time, sleep

from collections import deque
from datetime import datetime
from select import select


# --------------------------------------------------
# TODO: unify/split some parts of reactor.py and kernel.py?


# --------------------------------------------------
from uswarm.tools import (
    parse_uri,
    build_uri,
    soft,
    get_calling_function,
    find_by_regexp,
)

from .stats import Stats
from .node import *
from .channel import *
from .dom import *

from uswarm.tools.logs import logger

log = logger(__name__)


# ------------------------------------------------
# Timer Events
# ------------------------------------------------
class Timer(Publisher):
    value: float

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.value = float(self._uri["path"].split("/")[-1])
        foo = 1


# ------------------------------------------------
# Base Kernel
# ------------------------------------------------


class Kernel(Node):
    """Base of any Kernel:

    - handle I/O events.
    - handle timers.
    - handle CPU bound processes.


    """

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        # self.scheduler = {}

        self.stats = Stats()
        self.t0 = 0
        self.time = 0
        self.date = None

        # resources and factories
        self.factory = {}
        self.resources = {}
        self.alias = {}
        self._retry_allocate = deque()

        # main dom
        self.dom = None

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
                if resource is None:
                    assert resource.state in (
                        STATE_INIT,
                        STATE_SYNC,
                        STATE_TRANSITION,
                        STATE_LIVE,
                    )
                    # resource.next_state()
                else:
                    log.warn(f"Allocating Failled, uri: <{uri}>")

                self.alias[alias] = uri  # None means the last uri allocated
                return resource
        raise RuntimeError(f"missing function for allocating '{uri}' resource")

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
        """Add uri to reallocation scheduler.

        TODO: implement a delay POLICY (i.e mail server delivering)
        """
        self._retry_allocate.append(uri)

    # bootstraping

    def _bootstrap_005_factory_dom(self):
        log.debug(">> _bootstrap_005_factory_dom")
        self.register_factory(
            "(dom)://",
            self._allocate_dom,
            self._deallocate_dom,
            klass=Dom,
        )

        log.debug("<< _bootstrap_005_factory_dom")

    def _bootstrap_025_dom(self):
        log.debug(">> _bootstrap_025_dom")
        # cfg = {"port": 53000}
        cfg = {}
        uri = "dom://localhost/".format_map(cfg)
        self.dom = self.allocate(uri, alias="dom")

        log.debug("<< _bootstrap_025_dom")

    def _allocate_dom(self, _uri, klass, **kw):
        uri = build_uri(**_uri)
        holder = self.resources.setdefault(_uri["fscheme"], {})
        channel = holder.get(uri)

        if not channel:
            try:
                channel = klass(uri, self, **kw)
                # log.debug(f"0. sock: {channel.sock}")
                # assert timer.value == value
                holder[uri] = channel
                # self.resources["fds"][channel.sock] = channel

                log.debug(f"Allocating: <{uri}> ")

            except Exception as why:
                print(why)
                channel = None

            # self.resources["min_clock"] = min(0.5, *holder.keys())

        return channel

    def _deallocate_dom(self, _uri, **kw):
        args = _uri["host"]
        m = re.match(r".*$", args)
        if m:
            d = m.groupdict()
            holder = self.resources.setdefault(_uri["fscheme"], {})
            # uri = "timer://localhost/{unit}/{value}".format_map(d)

            uri = build_uri(**_uri)
            channel = holder.pop(uri, None)
            if channel:
                channel.sock.close()

            return True


# ------------------------------------------------
# Wave Kernel
# ------------------------------------------------


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


class WKernel(Kernel):
    """
    There is no other event that I/O activity and timers, so:

    - Channels that have fd descriptors.
    - use select() for fd activity.
    - timer for pusing time to any Node instance.

    # TODO: move down workflow and links between nodes.

    """

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.queues = {}
        self.links = {}

        self.fds_rx = {}
        self.fds_tx = {}

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
                self.time = time()
                self.date = datetime.fromtimestamp(self.time)
                remain = timers[0][0] - self.time
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

    def _bootstrap_005_factory_timer(self):
        log.debug(">> _bootstrap_005_factory_timer")
        self.register_factory(
            "timer://",
            self._allocate_timer,
            self._deallocate_timer,
        )

        log.debug("<< _bootstrap_005_factory_timer")

    def __bootstrap_005_factory_IO(self):
        log.debug(">> _bootstrap_005_factory_IO")
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
        log.debug("<< _bootstrap_005_factory_IO")

    def _bootstrap_011_timers(self):
        log.debug(">> _bootstrap_011_timers")
        self.resources.setdefault("timer", [])
        log.debug("<< _bootstrap_011_timers")

    def _bootstrap_015_rxtx(self):
        log.debug(">> _bootstrap_015_rxtx")
        self.resources.setdefault("fds", {})
        log.debug("<< _bootstrap_015_rxtx")

    def __bootstrap_025_netbase(self):
        log.debug(">> _bootstrap_025_netbase")
        cfg = {"port": 53000}
        uri = "udp://<broadcast>:{port}".format_map(cfg)
        channel = self.allocate(uri, alias="broadcast")
        log.debug("<< _bootstrap_025_netbase")

    def __bootstrap_040_monitor(self):
        # while self.scheduler or self.running:
        # print(f"load: {len(self.scheduler)}")
        # data = {"scheduler": [len(q) for q in self.scheduler]}
        # t0 = int(self.elapsed)
        # self.stats.push(t0, data)
        # time.sleep(1)
        log.debug(">> _bootstrap_040_monitor")

        self.free_time = 0

        handler = WQueue("watchdog://default", self, self._watchdog_monitor)
        handler.subscribe("timer://localhost/secs/1")

        log.debug("<< _bootstrap_040_monitor")

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

                log.debug("Allocating: <{fscheme}://{host}{path}> ".format_map(_uri))

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
                # log.debug(f"0. sock: {channel.sock}")
                # assert timer.value == value
                holder[uri] = channel
                # self.resources["fds"][channel.sock] = channel

                log.debug(f"Allocating: <{uri}> ")

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
