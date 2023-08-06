import inspect
import gc
import os
import pickle
import random
import re
import sys
import threading
import yaml

from weakref import WeakMethod, WeakSet, WeakValueDictionary
from collections import deque
from datetime import datetime
from select import select
from time import time, sleep


# from .channel import *
# from .dom import Dom
from .stats import Stats
from .request import (
    _signature,
    DELETE_AT,
    iRequester,
    REPLY_TO,
    REPLY_TO_REQUEST,
    REPLY_TO_WAVE,
    RID_HEADER,
    SERVER,
    EVENT_REQUEST,
    EVENT_RESPONSE,
    X_COMMAND,
    X_EVENT,
    X_WAVE,
)

from uswarm.tools import (
    build_uri,
    parse_uri,
    soft,
    get_calling_function,
    get_subclasses,
)

from uswarm.tools.containers import walk, flatdict, flatten
from uswarm.tools.files import load, get_newest_file

# from uswarm.kernel.pool import Pool

# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger, log_container

log = logger(__name__)

# ------------------------------------------------
# Definitions that musy be moved to a global
# shared definition file
# ------------------------------------------------

EVENT_TERM = "<term>"  # term alike
EVENT_QUIT = "<quit>"  # quit alike

# ------------------------------------------------
# Definitions
# ------------------------------------------------


BASE_TIMER = "each://localhost/secs/5.0/2/0"
BASE_TIMER_EVENT = "each://5"

LONG_TIMER = "each://localhost/secs/60.0/0/0"
LONG_TIMER_EVENT = "each://60"

SAVING_TIMER = "each://localhost/secs/30.0/0/0"
SAVING_TIMER_EVENT = "each://30"


EVENT_IDLE = "<idle>"
EVENT_SAVE = "<save>"

DOMESTIC_TIMER = "each://localhost/secs/10.0/0/0"
DOMESTIC_TIMER_EVENT = "each://10"
EVENT_DOMESTIC = "<domestic>"

# ------------------------------------------------
# Kernel internal notifications
# ------------------------------------------------
SYS_GENERAL_BUS = "sys://localhost/bus"

EVENT_STATUS_CHANGED = "<status-changed>"

EVENT_RESOURCE_ERROR = "<resource-error>"
EVENT_RESOURCE_WARNING = "<resource-warning>"
EVENT_RESOURCE_INFO = "<resource-info>"
EVENT_RESOURCE_PACING = "<resource-pacing>"


def f2s(value: float) -> str:
    """Print a float removing all right zeros and colon when possible."""
    return ("%.15f" % value).rstrip("0").rstrip(".")


# --------------------------------------------------
# Resources
# --------------------------------------------------
class Resource:
    """Base class for any resource or alive element in Kernel."""

    KERNEL_URI_REGISTERING = None
    KERNEL_URI_HOLDER = dict

    # --------------------------------------------------
    # Generic Allocation
    # --------------------------------------------------
    @classmethod
    def kernel_registering(cls, kernel):
        """Basic Register Timer factories.
        Override for more complex resgisterings.
        """
        uri = cls.KERNEL_URI_REGISTERING
        if not uri:
            log.warning(f"Can not auto-register: {cls}")
            return

        log.debug(f">> registering {cls} with: {uri}")
        kernel.register_factory(
            uri,
            cls._allocate_resource,
            cls._deallocate_resource,
        )
        # create holders for these schemes
        for fscheme in re.findall("[\w+]+", parse_uri(uri)["fscheme"]):
            log.debug(f" -- allocating {fscheme} : {cls.KERNEL_URI_HOLDER} ")
            kernel.resources.setdefault(fscheme, cls.KERNEL_URI_HOLDER())
        log.debug(f"<< registering {cls}")

    @classmethod
    def _allocate_resource(cls, kernel, _uri, **kw):
        """Generic allocation resource."""
        uri = build_uri(**_uri)
        holder = kernel.resources.setdefault(_uri["fscheme"], {})
        resource = holder.get(uri)

        if not resource:
            try:
                soft(kw, **_uri.get("query_", {}))
                resource = cls(uri, kernel, **kw)
                holder[uri] = resource
                log.debug(f"Allocating: <{uri}> ")

            except Exception as why:
                log.exception(why)
                resource = None

        return resource

    @classmethod
    def _deallocate_resource(cls, kernel, _uri, **kw):
        """Generic deallocation resource."""
        args = _uri["host"]
        m = re.match(r".*$", args)
        if m:
            d = m.groupdict()
            holder = kernel.resources.setdefault(_uri["fscheme"], {})
            soft(_uri, **d)
            uri = build_uri(**_uri)
            resource = holder.pop(uri, None)
            if resource:
                pass
            return resource

    def __init__(self, uri, kernel, parents=[], *args, **kw):
        self.uri = uri
        self._uri = parse_uri(uri)
        assert any(self._uri.values()), f"Bad URI '{uri}'"
        soft(self._uri, **kw)
        soft(self._uri, **self._uri.get("query_", {}))

        self.load()

        self.kernel = kernel
        self.family = (
            WeakValueDictionary()
        )  # resources that are *family* (parent and siblins)

        self.event_handler = {}
        self._handler_error_code = {}
        self._populate_event_handlers()

        self._handler_idle_task = {}
        self._populate_idle_handlers()

        # --------------------------------------------------
        # Persistence support
        # --------------------------------------------------
        self._saving_in_progress = False

        # --------------------------------------------------
        # Parent / Child relationship
        # --------------------------------------------------
        self.children = WeakSet()
        self.parents = WeakSet(parents)
        for parent in parents:
            parent.children.add(self)

    def get_family(self, down=2, up=2, result=None):
        if result is None:
            result = self.family

        result[self.uri] = self

        if down > 0:
            for child in self.children:
                if child.uri not in result:  # avoid any cycles anyhow
                    result.update(child.get_family(down - 1, up, result))

        if up > 0:
            for parent in self.parents:
                if parent.uri not in result:  # avoid any cycles anyhow
                    result.update(parent.get_family(down, up - 1, result))

        return result

    def find_resource(self, uri):
        if not self.family:
            self.get_family()

        return self.family.get(uri)

    def find_resources(self, pattern, down=2, up=2):
        if not self.family:
            self.get_family(down, up)
        for resource in self.family.values():
            if re.match(pattern, resource.uri):
                yield resource

    def allocate(self, uri):
        family = self.get_family()
        if uri not in family:
            self.kernel.allocate(uri)
        else:
            log.warning(f"uri: {uri} is already allocated")

    # --------------------------------------------------
    # Event Listening / Dispatching
    # --------------------------------------------------

    def subscribe(self, port):
        if port in self.kernel.ports:
            self.kernel.subscribers.setdefault(port, {})[self.uri] = self
        else:
            log.error(f"unkwon {event} for subscribing to ...")

    def dispatch(self, event, data, wave=None, *args, **kw):
        """Basic implementation or Resource event dispatching."""
        func = self.event_handler.get(event)
        func and func(event, data, wave, *args, **kw)

    # --------------------------------------------------
    # Persistence support
    # --------------------------------------------------

    @property
    def storage_path(self):
        name = "var/data/{scheme}/{host}".format_map(self._uri)
        path = self._uri["path"]
        if path and path != "/":
            name += path
        return name

    # def __getstate__(self):
    # """User need to override this method"""

    # def __setstate__(self, state):
    # """User need to override this method"""

    def load(self):
        name = self.storage_path
        func = getattr(self, "__setstate__", None)
        if inspect.ismethod(func):
            # check if yaml is modified after pickle one
            # then means user has change manually someething
            # so I'd rather looad the YAML file.
            path = get_newest_file(
                name,
            )  # [".pickle"])
            log.debug(f"loading from {path} ...")

            try:
                state = load(path)
                func(state)
                log.debug(f"state recovered from {path}")
            except Exception as why:
                log.error(f"trying loading: {why}")

    def save(self):
        """Create a snapshot and save in pickle and yaml format in background"""
        # get an isolate memory representation of resource
        func = getattr(self, "__getstate__", None)
        if inspect.ismethod(func):
            snapshot = func()
            snapshot = pickle.dumps(snapshot)

            name = self.storage_path

            def save_pickle():
                # log.debug(f"saving {name}.pickle ...")
                os.makedirs(os.path.dirname(name), exist_ok=True)
                with open(f"{name}.pickle", "wb") as f:
                    f.write(snapshot)
                # log.debug(f"done {name}.pickle")

            def save_yaml():
                try:
                    # log.debug(f"saving {name}.yaml ...")
                    os.makedirs(os.path.dirname(name), exist_ok=True)
                    data = pickle.loads(snapshot)
                    yaml.dump(data, open(f"{name}.yaml", "w"), default_flow_style=False)
                    # log.debug(f"done {name}.yaml")

                    threading.Thread(target=save_pickle).start()
                finally:
                    self._saving_in_progress = False

            save_pickle()  # mke a "fast" dump

            # save in YAML and finally "touch" file
            self._saving_in_progress = True
            threading.Thread(target=save_yaml).start()

    def save_state(self, event, data, wave, *args, **kw):
        if self._saving_in_progress:
            log.debug(f"A saving process is still running !!!, skipping")
            return
        self.save()

    # --------------------------------------------------
    # Handlers
    # --------------------------------------------------

    def _populate_event_handlers(self):
        """Populate incoming messages handlers."""

        self.event_handler[EVENT_SAVE] = self.save_state
        self.event_handler[EVENT_TERM] = self.on_term
        self.event_handler[EVENT_QUIT] = self.on_quit

        # populate error codes handlers
        rexp = re.compile(r"_handler_code_(?P<code>\d+)(_(?P<text>.*)$)?")
        for name in dir(self):
            m = rexp.match(name)
            if m:
                d = m.groupdict()
                code, text = int(d["code"]), d["text"]
                if text:
                    text = text.replace("_", "\s+")

                # print(f" + handle [{code}]({text})")
                handlers = self._handler_error_code.setdefault(code, dict())
                handlers[text] = getattr(self, name)

    def _populate_idle_handlers(self):
        """Populate idle tasks handlers."""

        self.event_handler[EVENT_IDLE] = self.on_idle

        # populate error codes handlers
        rexp = re.compile(r"_idle_(?P<priority>\d+)(_(?P<text>.*)$)?")
        for name in dir(self):
            m = rexp.match(name)
            if m:
                d = m.groupdict()
                priority, text = int(d["priority"]), d["text"]
                text = text or name
                self._handler_idle_task[text] = [0, int(priority), getattr(self, name)]

    def on_idle(self, event, data, wave=None, *args, **kw):
        # log.debug(f"on_idle : [{self.uri}] ...")
        tasks = list(self._handler_idle_task)
        tasks.sort()  # allowing some *execution order*
        for name in tasks:
            handler = self._handler_idle_task[name]
            handler[0] -= 1
            if handler[0] < 0:
                handler[0] = handler[1]
                handler[2](event, data, wave, *args, **kw)

    def on_term(self, event, data, wave=None, *args, **kw):
        """Resources must do nothing on term. They are state-less
        elements that can dye at any moment."""
        delay = 5
        when = self.kernel.time + delay
        self.kernel.at(when, self.uri, EVENT_QUIT, None)

    def on_quit(self, event, data, wave=None, *args, **kw):
        """Detach from Kernel"""

        if self.kernel:
            self.save()
            self.kernel.delete(self.uri)


class Timer(Resource):
    """Encapsulate Timer resource data for kernel.
    Timer can never receive an event, just holds the information
    for kernel to handle timers.

    TODO: remove as Resource and let it handle timers lists?
    """

    KERNEL_URI_REGISTERING = "timer://"
    KERNEL_URI_HOLDER = list  #: special ordering case for timers

    @classmethod
    def _allocate_resource(cls, kernel, _uri, **kw):
        klasses = {"each": Each, "timer": Timer}

        args = _uri["path"]
        m = re.match(
            r"/(?P<unit>([^/]+))/(?P<restart>[^/]+)(/(?P<begin>[^/]+))?(/(?P<cycles>[^/]+))?$",
            args,
        )
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
            soft(d, restart=1.0, begin=0, cycles=0)

            d["unit"] = "secs"
            for key, func in Timer.ATTRS.items():
                d[key] = func(d[key]) * muliplier[d["unit"]]

            # search if timer already exists
            # holder = kernel.resources.setdefault(_uri["fscheme"], {})
            holder = kernel.resources[_uri["fscheme"]]
            for t0, timer in holder:
                for key in Timer.ATTRS:
                    if getattr(timer, key) != d[key]:
                        break
                else:
                    break
            else:
                # particular implementation
                uri = "each://localhost/{unit}/{restart}/{begin}/{cycles}".format_map(d)
                event = f"each://{f2s(d['restart'])}"

                # use int(time() for easy debugging
                # simple constructor. Do not add more params but uri
                timer = klasses[_uri["fscheme"]](uri, kernel, event)

                # insert timer in the right position
                t00 = int(time() + timer.begin)
                for i, (t2, timer2) in list(enumerate(holder)):
                    if t2 > t00:
                        holder.insert(i, (t00, timer))
                        break
                else:
                    holder.append((t00, timer))

                log.debug(f"Allocating: <{uri}> ")

            return timer

    @classmethod
    def _deallocate_resource(cls, kernel, _uri, **kw):
        # TODO: remove data from timer list
        pass

    restart: float
    begin: int
    cycles: int
    ATTRS = {"restart": float, "begin": int, "cycles": int}
    event: str

    def __init__(self, uri, kernel, event=None, *args, **kw):
        super().__init__(uri, kernel, *args, **kw)

        self.restart = 0
        self.begin = 0
        self.cycles = 0

        values = self._uri["path"].split("/")[2:]

        for k, f in self.ATTRS.items():
            if values:
                value = values.pop(0)
                setattr(self, k, f(value))

        self.event = event or f"{self._uri['scheme']}:{f2s(self.restart)}"

        self.kernel.create_port(self.event)


class Each(Timer):
    """Relative timer"""

    KERNEL_URI_REGISTERING = "each://"


class Monitor(Resource):
    KERNEL_URI_REGISTERING = "watchdog://"

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.idle_last = dict()
        self.idle_pending = list()
        self.idle_load = 0.4  #: max load to execute idle tasks
        self.idle_max = 50  #: max idle task each time
        self.idle_pacing = 1  # 60  #: min secs before retry the same idle task

        self.event_handler[BASE_TIMER_EVENT] = self.watchdog_monitor

    def watchdog_monitor(self, event, data, wave, *args, **kw):
        t0, cycles = data

        # log.debug(f" -- _watchdog_monitor: {t0}, {cycles}")

        kernel = self.kernel
        now = time()

        # ----------------------------------------
        # Idle Tasks
        # ----------------------------------------
        elapsed = now - kernel.busy_time_mark
        load = kernel.busy_time_elapsed / elapsed

        # quant = 0.01

        # log.warning(
        # f"kernel load: b:{kernel.busy_time_elapsed}, e:{elapsed} = {busy}-> {load} %: busy_time_mark: {kernel.busy_time_mark}"
        # )
        # log.warning(f"kernel load: {load:.2%}")

        # reset time marks
        kernel.busy_time_mark = now
        kernel.busy_time_elapsed = 0

        load0 = kernel.stats.means.get("load", 0)
        kernel.stats.push(t0, {"load": load})
        kernel.stats.compute()
        load1 = kernel.stats.means["load"]

        if load1 < load0 and load0 < self.idle_load:
            # kernel is idle now
            self.select_idle_task()

        # ----------------------------------------
        # Retry Allocations
        # ----------------------------------------
        while kernel._retry_allocate:
            uri = kernel._retry_allocate.popleft()
            log.info(f"Retry: {uri} : pending: {len(kernel._retry_allocate)}")
            kernel.allocate(uri)

        means = kernel.stats.means
        # log.debug(f"Kernel means: {means}")
        # gc.collect()

        # ----------------------------------------
        # Send "At" events
        # ----------------------------------------
        while kernel._enqueue_at and kernel._enqueue_at[0][0] < now:
            _, params = kernel._enqueue_at.popleft()
            kernel.enqueue(*params)

        # do some other maintenance tasks
        # fire TIMEOUT_AT
        # remove DELETE_AT done responses

    def select_idle_task(self):
        # log.debug(f"Doing IDLE tasks ...")
        kernel = self.kernel
        now = kernel.time
        if not self.idle_pending:
            # TODO: gather only real Resources, not timers, etc
            # TODO: that are loaded by bootstraping methods
            self.idle_pending = list(kernel.ports)

        i = self.idle_max
        while self.idle_pending:
            port = self.idle_pending.pop()
            if not port in kernel.ports:
                continue

            if now - self.idle_last.get(port, 0) > self.idle_pacing:
                self.idle_last[port] = now
                kernel.enqueue(port, EVENT_IDLE, None)
                kernel.enqueue(port, EVENT_SAVE, None)
                # log.debug(f" [{port}] --> {EVENT_IDLE}")
                i -= 1
                if i <= 0:
                    break

        foo = 1

    def _idle_003_garbage_collection(self, event, data, wave=None, *args, **kw):
        """Do some cleaning activities such:

        - memory garbage collection
        - (...)
        """
        super().on_idle(event, data, wave, *args, **kw)
        # log.info(f"GARBAGE COLLECTOR ...")
        gc.collect()
        foo = 1

    def _idle_003_watch_waiting_responses(self, event, data, wave=None, *args, **kw):
        stats = {}
        kernel = self.kernel
        for scheme, resources in kernel.resources.items():
            if isinstance(resources, dict):
                for uri, resource in resources.items():
                    if isinstance(resource, iRequester):
                        assert hasattr(resource, "waiting")
                        # analyze waiting responses
                        size = len(resource.waiting)
                        st = stats[resource.uri] = {
                            "size": size,
                            "pending": 0,
                            "done": 0,
                        }
                        for res in resource.waiting.values():
                            if res.get(DELETE_AT):
                                st["done"] += 1
                            else:
                                st["pending"] += 1

        log_container(log, stats, fmt="{done}/{size} done res", lines=10**6)
        return stats

    def _idle_001_watch_pool_load(self, event, data, wave=None, *args, **kw):
        stats = {}
        kernel = self.kernel
        for scheme, resources in kernel.resources.items():
            if isinstance(resources, dict):
                for uri, resource in resources.items():
                    if "pool" in resource._uri["fscheme"]:
                        assert hasattr(resource, "pacing")
                        # analyze waiting responses
                        for uri, samples in resource.pacing.items():
                            stats[uri] = len(samples)
        log_container(log, stats, fmt="{size}", lines=10**6)
        return stats

    def on_quit(self, event, data, wave=None, *args, **kw):
        """Detach from Kernel and Stop kernel itself."""
        super().on_quit(event, data, wave, *args, **kw)
        if self.kernel:
            self.kernel.stop()


# --------------------------------------------------
# Kernel
# --------------------------------------------------
class Kernel(Resource):
    """Base of any Kernel:

    - handle I/O events.
    - handle timers.
    - handle CPU bound processes.

    """

    def __init__(self, uri, kernel=None, config={}, *args, **kw):
        super().__init__(uri, kernel, *args, **kw)

        self.config = config

        self.stats = Stats()
        self.t0 = 0
        self.time = 0
        self.date = None

        # resources and factories
        self.factory = {}
        self.resources = {}
        self.alias = {}  # TODO: weak dict against same queues?
        self.rev_alias = {}  # TODO: weak dict against same queues?

        # scheduler / planner / subscribers
        self.subscribers = {}  #: #port, #stm
        self.ports = {}  #: #port, deque
        self.port_activity = dict()
        self.priority = []  #: priority for each existing port

        self._retry_allocate = deque()
        self._enqueue_at = deque()

        # main dom
        self.dom = None

    # --------------------------------------------------
    # Pub/Sub ports
    # --------------------------------------------------

    def create_port(self, port):
        if port in self.ports:
            log.warning(f"port '{port}' is already created")
        else:
            log.info(f"new '{port}' created")
            self.ports[port] = deque()

            alias = _signature(port)
            self.rev_alias[port] = alias
            self.alias[alias] = port

            self.priority.append(port)
            self.priority.sort()  # TODO: use priorities for planner

            # notify port creation
            self.enqueue(
                SYS_GENERAL_BUS,
                EVENT_STATUS_CHANGED,
                {"port": port, "status": "new"},
            )

    def delete_port(self, port):
        if port not in self.ports:
            log.warning(f"'{port}' not found for deletion")
        else:
            log.info(f"deleted '{port}'")
            self.ports.pop(port)
            self.port_activity.pop(port, None)

            alias = _signature(port)
            self.alias.pop(alias, None)
            self.rev_alias.pop(port, None)

            self.priority.remove(port)
            # self.priority.sort()  # TODO: use priorities for planner

            # notify port creation
            self.enqueue(
                SYS_GENERAL_BUS,
                EVENT_STATUS_CHANGED,
                {"port": port, "status": "delete"},
            )

    def enqueue(self, port, event, data, wave=None):
        """Override for more complex parallel implementations."""
        port = self.alias.get(port, port)
        if port in self.ports:
            self.ports[port].append((event, data, wave))
            self.port_activity[port] = True
        else:
            log.error(f"port: {port} is missing in kernel")

    def oob(self, port, event, data, wave=None):
        """Override for more complex parallel implementations."""
        port = self.alias.get(port, port)
        if port in self.ports:
            self.ports[port].appendleft((event, data, wave))
            self.port_activity[port] = True
        else:
            log.error(f"port: {port} is missing in kernel")

    def at(self, when, port, event, data, wave=None):
        """enqueue an event at specific time.
        Domestic in Monitor check outdated events to enqueue.

        # TODO: use a special Timer "At" to fire event more preciselly
        """
        timers = self._enqueue_at
        params = port, event, data, wave
        for i, (t2, _) in list(enumerate(timers)):
            if t2 > when:
                timers.insert(i, (when, params))
                break
        else:
            timers.append((when, params))

    # --------------------------------------------------
    # Running Loop
    # --------------------------------------------------

    def start(self):
        log.warning("=" * 80)
        log.warning(f">> Kernel {self.__class__.__name__} starting!")
        log.warning("=" * 80)
        self.running = True
        self.time = self.t0 = time()
        # time.process_time
        self._bootstrap()
        self.main()
        self.stop()

        log.debug("<< start")

    def main(self):
        raise NotImplementedError()

    def stop(self):
        self.running = False

    @property
    def elapsed(self):
        return self.time - self.t0

    # --------------------------------------------------
    # Resource Factories and Allocation
    # --------------------------------------------------

    def register_factory(self, pattern, allocator, deallocator, **defaults):
        # need to translate some chars from pattern
        # pattern = pattern.replace(..,..)  NO!, change in KERNEL_URI_REGISTERING

        self.factory[pattern] = allocator, deallocator, defaults

    def allocate(self, uri, alias=None):
        """Allocate a resource based on uri.

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

        But is transparent for all resourced as they implement dispatch() method.

        """
        if uri in self.alias:
            return self.allocate(self.alias[uri])

        for pattern, (allocator, deallocator, defaults) in self.factory.items():
            m = re.match(pattern, uri)
            if m:
                kw = m.groupdict()
                _uri = parse_uri(uri)
                soft(kw, **defaults)

                # auto include parents
                if "parents" not in kw:
                    frame = inspect.stack()[1][0]
                    parent = frame.f_locals.get("self")
                    if isinstance(parent, Resource) and parent != self:
                        kw["parents"] = [parent]

                # allocator must:
                # 1. find resource holder container in kernel.resource (usually by fscheme).
                # 2. holders may be dict (default case index by uri) or lists (i.e. timers).
                # 3. check if resource is already allocated.
                # 4. create and initialize the resource to be ready to receive kernel events.
                # 5. place the resource in holder

                resource = allocator(self, _uri, **kw)
                if resource is None:
                    log.error(f"Allocating Failled, uri: <{uri}>")
                else:
                    self.alias[alias] = uri  # None means the last uri allocated
                    self._attach(resource)

                return resource
        raise RuntimeError(f"missing function for allocating '{uri}' resource")

    def _attach(self, resource):
        """Create a dedicated port based on resource uri and subscribe
        the resource to listen events in its dedicated port.
        """
        # assert resource.state in (
        # STATE_OFF,
        ## STATE_INIT,
        ## STATE_SYNC,
        ## STATE_TRAN,
        ## STATE_LIVE,
        # )
        assert resource.kernel == self
        # create its own "private" port
        self.create_port(resource.uri)
        self.subscribers.setdefault(resource.uri, {})[resource.uri] = resource

        # resource.asap(EVENT_NEXT)

    def _detach(self, resource):
        """Remove resource dedicated port and rmove subscribers port."""
        # assert resource.state in (
        # STATE_OFF,
        # STATE_INIT,
        # STATE_SYNC,
        # STATE_TRAN,
        # STATE_LIVE,
        # )
        assert resource.kernel == self
        # create its own "private" port
        self.delete_port(resource.uri)
        self.subscribers.pop(resource.uri, None)
        # resource.asap(EVENT_NEXT)

    def delete(self, uri):
        if uri in self.alias:
            return self.delete(self.alias[uri])

        for pattern, (allocator, deallocator, defaults) in self.factory.items():
            m = re.match(pattern, uri)
            if m:
                kw = m.groupdict()
                _uri = parse_uri(uri)
                soft(kw, **defaults)
                resource = deallocator(self, _uri, **kw)
                if resource is None:
                    log.warn(f"Deallocating Failled, uri: {uri}")
                else:
                    # TODO: use watchdog for cleaning non-used ports / sub
                    self._detach(resource)
                    pass

                for alias in list(self.alias):
                    if self.alias[alias] == uri:
                        self.alias.pop(alias)
                        break
                return resource
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

    def find_resource(self, uri):
        fscheme = parse_uri(uri)["fscheme"]
        holder = self.resources.get(fscheme)
        if isinstance(holder, dict):
            holder = holder.items()
        for _, resource in holder:
            if uri == resource.uri:
                return resource

    def find_resources(self, pattern):
        for fscheme, holder in self.resources.items():
            if isinstance(holder, dict):
                holder = holder.items()
            for _, resource in holder:
                if re.match(pattern, resource.uri):
                    yield resource

    # --------------------------------------------------
    # Kernel Bootstraping
    # --------------------------------------------------
    def _start_fiber(self, name, func):
        """Fire a function in a *parallel-light-fiber* when is possible.
        Just execute function by default.
        """
        log.debug(f"Starting fiber: '{name}'")
        func()

    def _bootstrap(self):
        """Locate and launch all bootstrap task prior kernel start running."""
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

    def _bootstrap_009_factory_automatic(self):
        # print(get_subclasses(Resource))

        for klass in get_subclasses(Resource):
            print(klass)
            func = getattr(klass, "kernel_registering", None)
            # if "Dumper" in str(klass):
            # foo = 1
            # if not func:
            # print(f" - BAD: {klass} has kernel_registering()")
            # foo = 1
            func and func(self)

        foo = 1

    # --------------------------------------------------
    # Timers
    # --------------------------------------------------
    def _bootstrap_004_sys_notification(self):
        log.debug(">> _bootstrap_004_sys_notification")
        self.create_port(SYS_GENERAL_BUS)
        self.create_port(SYS_GENERAL_BUS)
        log.debug("<< _bootstrap_004_sys_notification")

    def _bootstrap_011_timers(self):
        log.debug(">> _bootstrap_011_timers")
        self.allocate(BASE_TIMER)
        self.allocate(LONG_TIMER)
        # self.allocate(SAVING_TIMER)
        self.allocate(DOMESTIC_TIMER)
        log.debug("<< _bootstrap_011_timers")

    # --------------------------------------------------
    # Monitors
    # --------------------------------------------------
    # def _bootstrap_009_factory_monitor(self):
    # """Register Timer factories."""
    # log.debug(">> _bootstrap_009_factory_monitor")
    # self.register_factory(
    # "watchdog://",
    # self._allocate_each,
    # self._deallocate_each,
    # )
    # self.resources.setdefault("each", [])
    # log.debug("<< _bootstrap_009_factory_monitor")

    def _bootstrap_040_monitor(self):
        log.debug(">> _bootstrap_040_monitor")

        self.busy_time_mark = 0

        # launch moitor withou need to be registered first
        handler = Monitor(f"watchdog://default", kernel=self)
        handler.subscribe(BASE_TIMER)

        log.debug("<< _bootstrap_040_monitor")

    # --------------------------------------------------
    # TODO: review these resources
    # --------------------------------------------------

    def _bootstrap_025_dom(self):
        log.debug(">> _bootstrap_025_dom")
        # cfg = {"port": 53000}
        cfg = {}
        uri = "dom://localhost/".format_map(cfg)
        self.dom = self.allocate(uri, alias="dom")

        log.debug("<< _bootstrap_025_dom")

    # -----------------------------------------------
    # Exiting methods
    # -----------------------------------------------

    def on_term(self, event, data, wave, *args, **kw):
        """Send a EVENT_TERM to every resource in Kernel"""
        self.shutdown()

    def shutdown(self, event=EVENT_TERM):
        """Performs an ordered shutdown of kernel.

        1. send EVENT_TERM
        2. schedule an EVENT_QUIT in delay + 1 secs
        """
        delay = 5
        when = self.time + delay

        log.warn(f"[{self.uri:20}][ -- shutdown in {delay} secs !! ...")
        for resource in self.find_resources("."):
            self.at(when, resource.uri, event, None)


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
