"""
Kurio kernel is based on Workflows not General purpose Kernel.
so he concept may b different from other kernel desings.
It's better to start from scratch and follow this checklist:

- [ ] Node is Resource.
- [ ] Resource can be Device or just a Node in a Workflow Pipeline.
- [ ] Kernel can run in the same thread (default) or in a new thread.
- [ ] Pipelines merge with existing ones seamlessly.
- [ ] Kernel bootstrap and Live configuraion are in files (YAML?)
- [ ] Kernel can stop, reload and resume worlflows as the config files changes seamlessly.
- [ ] Resouces does not store its internal status, just wave flows (state-less)
- [ ] But loop/context local vars are saved to be reloaded on resume, so looping continues from last saved execution.
- [ ] Resources and pipelines can be aborted at any time without any notificaction.
- [ ] Resources are always *ready*, do not have a *initial*, *loading*, etc status.
- [ ] Devices that connects with external-real-world may have this stages but are handler internally, not by kernel.


- [ ] minimal resource and Kernel support for Resources (Nodes) and Kernel async framework
- [ ] copy/mimic each interesting feature ONLY is when IMPROVE Kurio kernel.


"""
from __future__ import annotations

import functools
import inspect
import re
import socket
import os
import uuid

from collections import deque
from itertools import product
from time import time
from weakref import WeakValueDictionary

from ..tools import (
    build_uri,
    expandpath,
    fileiter,
    parse_uri,
    sitems,
    soft,
)
from ..tools.configurations import Config, merge, load_config, save_config
from ..tools.factory import iFactory
from ..tools.iterators import expand, Xiterator, Xexpand
from ..tools.units import timeframe2delta

from .resource import iResource

from curio import run, sleep, Queue, Event, TaskGroup, spawn
from curio.subprocess import Popen, run
from curio.file import aopen, anext, AsyncFile


# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger

log = logger(__name__)

# ------------------------------------------------
# Definitions
# ------------------------------------------------


# --------------------------------------------------
# Kernel
# --------------------------------------------------

RESOURCE_ATTACHED='<resource-attached>'
RESOURCE_DETACHED='<resource-detached>'

class iKernel(iResource):
    """Base of any Kernel:

    - handle I/O events.
    - handle timers.
    - handle CPU bound processes.

    """
    # TODO: remove and make it configurable
    URI_MATCH =  {
        r"(?P<fsqueme>.*\-sync)://localhost/(?P<kind>bars).*(?P<q1>(?P<symbol_>symbol)=(?P<symbol>\w+))": {
            #"_kind_": ['ab5', 'ab8', 'ab10', 'ab15'],
            "_price_": 'range(4, 20, 3)',
            "fscheme": "atlas-bar",
            "query_keys": ["symb.*"],
            "uri": r"{fscheme}://{host}/{kind}?{q1}&p={price}&parent={parent}",

        }
    }


    URI_REGISTERING = r"kernel://(?P<host>[^:/]+)(:(?P<port>\d+))?(?P<path>.*?)$"

    def __init__(
        self,
        uri: str,
        kernel: iKernel = None,
        config: Config = None,
        *args,
        **kw,
    ):
        super().__init__(uri=uri, kernel=kernel, config=config, *args, **kw)

        # self.stats = Stats()
        self.t0 = 0  #: time when kernel starts
        self.time = 0  #: current (ansd shared) kernel time
        self.date = None

    # --------------------------------------------------
    # Properties
    # --------------------------------------------------
    @property
    def elapsed(self):
        """Elapsed time since kernel started."""
        return self.time - self.t0

    # --------------------------------------------------
    # Running Loop
    # --------------------------------------------------

    def start(
        self,
        path: str = None,
        config: Config = None,
        extra_fibers: list = None,
        extra_config: dict = None,
        **kw,
    ):
        """Start the kernel using a configuraion and/or additinal extra fibers.

        - setup base attributes from base class: running, time, etc
        - call specific init method (derived method that implements the loop technology)
        - stop the kernel when *init* (loop) ends.
        """
        log.warning("=" * 80)
        log.warning(
            f">> Kernel {self.uri} of type: '{self.__class__.__name__}' starting!"
        )
        log.warning("=" * 80)
        self.running = True
        self.time = self.t0 = time()

        # finish the kernel config before starting.
        self.configure(path, config)
        for key, value in sitems(extra_config or {}):
            self.config.assign(key, value)

        # start the main loop
        self.init(path, config, extra_fibers, **kw)

        # a chance for any additional shutdown tasks
        self.stop()

        log.debug("<< start")

    def init(
        self, path: str = None, config: Config = None, extra_fibers: list = None, **kw
    ):
        """Base init features"""

    def configure(self, path: str = None, config: Config = None):
        """Merge kernel configuration with a new configuraion *layer*."""
        config = config or {}
        config = Config(config)
        if path and os.access(path, os.F_OK):
            cfg = load_config(path)
            config = merge(config, cfg)

        self.config = merge(self.config, config)
        return self.config

    def stop(self):
        self.running = False

    # --------------------------------------------------
    # Kernel Bootstraping
    # --------------------------------------------------


    # --------------------------------------------------
    # allocate / deallocate
    # --------------------------------------------------
    def allocate(self, uri, alias=None, **kwargs):
        instance = super().allocate(uri=uri, alias=alias, kernel=self, **kwargs)

        kwargs['parent'] = instance.uid
        # allocate related instances too
        for pattern, info in self.URI_MATCH.items():
            m = re.match(pattern, uri)
            if m:
                d = m.groupdict()
                d.update(info)
                d.update(kwargs)

                soft(d, **instance._uri)
                # expand
                params = {}
                for k in info:
                    m = re.match("_(?P<k>\w+)_", k)
                    if m:
                        params[m.group(1)] = expand(info[k])

                for p in Xexpand(params):
                    d.update(p)
                    _uri = info['uri'].format_map(d)
                    print(f"_uri: {_uri}")
                    self.allocate(_uri)

                foo = 1

        return instance

    def attach(self, resource):
        """Start the main fiber of a iResource."""
        assert isinstance(resource, iResource)
        name = f"{resource.uri}.main"
        self._start_fiber(name, resource.main)

        # publish the just attahed resource
        self.publish(resource, RESOURCE_ATTACHED)
        foo = 1

    # --------------------------------------------------
    # Monitors
    # --------------------------------------------------
    def stats(self) -> dict:
        """Return info from running fibers"""
        return {"running": set()}  # not implemented

    # -----------------------------------------------
    # Exiting methods
    # -----------------------------------------------

    def shutdown(self):  # TODO: implement
        """Performs an ordered shutdown of kernel.

        1. send EVENT_TERM
        2. schedule an EVENT_QUIT in delay + 1 secs
        """
        delay = 5
        when = self.time + delay

        log.warn(f"[{self.uri:20}][ -- shutdown in {delay} secs !! ...")
        for resource in self.find_resources("."):
            # self.at(when, resource.uri, event, None)
            pass  # do whatever was necessary


# --------------------------------------------------
# HeartBeat device
# --------------------------------------------------


class HeartBeat(iResource):
    "A HeartBeat device"

    def __init__(
        self, uri: str, kernel: iKernel = None, config: Config = None, *args, **kw
    ):
        super().__init__(uri, kernel, config, *args, **kw)
        foo = 1

    async def main(self, *args, **kw):
        seconds = timeframe2delta(self.config.sd("freq", "10s")).total_seconds()
        log.debug(f"{self.uri} starts ...")
        kernel = self.kernel

        stats = {
            "kernel": kernel.uri,
            "hostid": f"{uuid.getnode():x}",
            "hotname": socket.gethostname(),
        }

        # TODO: normalize uri
        root = kernel.config.g("/kernel/root")
        uri = normalize_uri(self.uri)

        path = "{hotname}.{hostid}".format_map(stats)
        path = f"{path}.{uri}.yaml"
        path = os.path.join(root, path)

        while kernel.running:
            # timestamp
            stats["timestamp"] = time()

            # tasks
            stats.update(kernel.stats())
            for tid in stats["running"]:
                pass

            # publish HeartBeat
            log.warning(f"MODIFY HeartBeat FILE -----------------------------------")
            save_config(stats, path)

            await sleep(seconds)
        log.debug(f"{self.uri} ends ...")
        foo = 1


# --------------------------------------------------
# Sync FS device
# --------------------------------------------------


class SyncFS(iResource):
    """A SyncFS device

    To reduce number of SSH handshakes due to constant rsyncing between Local and Remote, enable SSH sockets on the local isntance

    mkdir /home/user/.ssh/sockets
    vim /home/user/.ssh/config

    Host <remote>
      TCPKeepAlive yes
      ServerAliveInterval 120
      Compression yes
      ControlMaster auto
      ControlPath ~/.ssh/sockets/%r@%h:%p
      ControlPersist yes
      ControlPersist 480m

    chmod 600 /home/user/.ssh/config
    chmod 770 /home/user/.ssh/sockets

    """

    URI_REGISTERING = r"sync-fs://(?P<host>[^:/]+)(:(?P<port>\d+))?(?P<path>.*?)$"

    def __init__(
        self, uri: str, kernel: iKernel = None, config: Config = None, *args, **kw
    ):
        super().__init__(uri, kernel, config, *args, **kw)

        self._modified = {}
        self._cache = {}

        self._file_list = f"/tmp/{normalize_uri(uri)}.file.list"

        self._ignore_list = f"/tmp/{normalize_uri(uri)}.ignore.list"
        ignored = [".sync", ""]
        open(self._ignore_list, "w").write("\n".join(ignored))

        self._last_sync = 0
        self._min_full_sync = 20
        self._drop_form_cache = 120
        self._pool_interval = 1.0
        self._explore_delta = 20

        root = kernel.config.g("/kernel/root")

        self._source = expandpath(root) + "/"
        self._target = [
            "dvb@vdream:~/workspace/demo-kurio/",
            "agp@vdream:~/workspace/demo-kurio/",
            "agp@vmnt:~/workspace/demo-kurio/",
            "pi@kodi:/media/pi/kingston/workspace/demo-kurio/",
        ]

    async def hide_future_main(self, *args, **kw):
        seconds = timeframe2delta(self.config.sd("freq", "15s")).total_seconds()
        log.debug(f"{self.uri}.main starts ...")
        kernel = self.kernel
        kernel._start_fiber(f"{self.uri}.explore", self.explore())
        kernel._start_fiber(f"{self.uri}.fast_check", self.fast_check())

        last = time()
        # TODO: make a 1st full sync

        # sync incremental modifications
        root = kernel.config.g("/kernel/root")
        root = expandpath(root)

        # TODO: create a AsyncDir class to monitorize Folders
        while kernel.running:
            fd = os.open(root, os.O_RDONLY)
            file = os.fdopen(fd)
            async with AsyncFile(file, "r") as f:
                data = await f.read()
                foo = 1

    async def main(self, *args, **kw):
        seconds = timeframe2delta(self.config.sd("freq", "25s")).total_seconds()
        self._min_full_sync = seconds
        seconds /= 2

        log.debug(f"{self.uri}.main starts ...")
        kernel = self.kernel
        kernel._start_fiber(f"{self.uri}.explore", self.explore())
        kernel._start_fiber(f"{self.uri}.fast_check", self.fast_check())

        # TODO: make a 1st full sync

        # sync incremental modifications
        root = kernel.config.g("/kernel/root")

        while kernel.running:
            # timestamp
            await self.full_sync()
            await sleep(seconds)

            foo = 1

        log.debug(f"{self.uri} ends ...")
        foo = 1

    async def explore(self, *args, **kw):
        seconds = timeframe2delta(self.config.sd("freq", "10s")).total_seconds()
        log.debug(f"{self.uri}.explore starts ...")
        kernel = self.kernel

        last = time()
        # TODO: make a 1st full sync

        # sync incremental modifications
        root = kernel.config.g("/kernel/root")
        root = expandpath(root)

        include = r".*"
        exclude = r"\.sync"

        while kernel.running:
            pause = self._pool_interval * 5  #: pause when no file ha been modified
            n = self._explore_delta
            for path, status in fileiter(
                root, regexp=include, info="s", exclude=exclude, relative=True
            ):
                if (mtime := status["mtime"]) > self._modified.get(path, 0):
                    log.warning(
                        f"New MODIFICATION {path}: {mtime} -------------------------------------"
                    )
                    self._modified[path] = mtime
                    self._cache[path] = self._last_sync
                    pause = self._pool_interval  # reduce pause
                n -= 1
                if n <= 0:
                    n = self._explore_delta
                    await sleep(self._pool_interval)
            await sleep(pause)

        log.debug(f"{self.uri} ends ...")
        foo = 1

    async def fast_check(self, *args, **kw):
        kernel = self.kernel
        root = kernel.config.g("/kernel/root")
        root = expandpath(root)

        deleted = {}  #: keep track of last deleted files to avoid innecessary full_sync
        while kernel.running:
            old = time() - self._drop_form_cache
            files = []
            drop_sync = []
            for path, mtime0 in list(self._cache.items()):
                fqpath = os.path.join(root, path)
                if os.access(fqpath, os.F_OK):
                    deleted.pop(path, None)
                    mtime = os.stat(fqpath).st_mtime
                    if mtime > mtime0:
                        self._cache[path] = mtime0 = time()
                        self._modified[path] = mtime0
                        files.append(path)
                        log.debug(f"FAST CHECK: {path}")
                else:
                    if path not in deleted:
                        drop_sync.append(path)
                    deleted[path] = True

                if mtime0 < old:
                    log.debug(f"DROP 1 file: {path}")
                    self._cache.pop(path)
                    deleted.pop(path, None)

            if drop_sync:
                log.debug(f"FULL SYN because drop {drop_sync} files")
                self._last_sync = 0  # force
                await self.full_sync()
            elif files:
                log.debug(f"FAST SYNC: {files}")
                self._build_file_list(files)
                await self.sync(include=self._file_list)
                foo = 1

            await sleep(self._pool_interval)

    def _build_file_list(self, files):
        if isinstance(files, dict):
            files = [path for path, mtime in files.items() if mtime > self._last_sync]
        open(self._file_list, "w").write("\n".join(files))
        return files

    async def full_sync(self):
        now = time()
        if now - self._last_sync > self._min_full_sync:
            self._last_sync = now
            log.warning(f"Full Sync -------------------------------------")
            await self.sync()

    async def sync(self, source=None, target=None, include=None, exclude=None):
        """

          rsync -azvP --times --delete-during \
          --exclude-from=sync.exclude \
          demo-kurio/
          dvb@vdream:/home/dvb/workspace/demo-kurio/

        """
        args = [
            "rsync",
            "-azvP",
            "--times",
            "--delete-during",
        ]

        include and args.append(f"--include-from={include}")

        if exclude is None:  # pass exclude='' to skip this option
            exclude = self._ignore_list
        exclude and args.append(f"--exclude-from={exclude}")

        args.append(source or self._source)

        if isinstance(target, str):
            target = [target]

        result = []
        for tar in target or self._target:
            aux = list(args)
            aux.append(tar)
            log.debug(f">>> Sync with: {tar}")
            task = await spawn(run(aux))
            result.append(task)

        while result:
            log.debug(f"remain rsync processes {len(result)} ...")
            await result[0].join()
            result.pop(0)

        log.debug(f"rsync process DONe")


# --------------------------------------------------
# TODO: review!!
# --------------------------------------------------


class _hide_iFactory:
    def __init__(self, *args, **kw):
        # resources and factories
        self.factory = {}
        self.resources = {}
        self.alias = {}  # TODO: weak dict against same queues?
        self.rev_alias = {}  # TODO: weak dict against same queues?

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
                    if isinstance(parent, iResource) and parent != self:
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

    def _detach(self, resource):
        """Remove resource dedicated port and remove subscribers port."""
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


if __name__ == "__main__":
    foo = 1
# End
