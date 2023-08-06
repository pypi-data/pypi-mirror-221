"""
TBD

"""
from __future__ import annotations

import functools
import os
import re
import uuid
import socket
import hashlib

from abc import abstractmethod

from ..tools import parse_uri, expandpath, sitems, soft
from ..tools.containers import merge, flatten
from ..tools.configurations import (
    Config,
    load_config,
    save_config,
    process_config,
    expand_config,
)
from ..tools.factory import iFactory
from ..tools.iterators import df_join, cpermutations
from ..tools.pubsub import iProcessor

from curio import run, sleep, Queue, Event, TaskGroup, spawn
from curio.meta import awaitable, asyncioable

# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger

log = logger(__name__)

# ------------------------------------------------
# Definitions
# ------------------------------------------------
def normalize_uri(uri, pattern="{scheme}/{host}/{port}{path}-{query}"):
    _uri = parse_uri(uri)

    used = ("scheme", "auth", "host", "port", "path", "query", "fragment")
    result = {}

    def clean(x):
        return x.replace(":", ".").replace("//", "").replace("/", "_")

    for key in used:
        result[key] = clean(_uri[key] or "x")

    return pattern.format_map(result)


def join_args(*args, **kw):
    tail = list(kw.items())
    tail.sort()
    tail = "/".join(list(flatten(tail)))
    path = os.path.join(*args, tail)
    return path


# --------------------------------------------------
# Resources
# --------------------------------------------------


class iResource(iFactory, iProcessor):
    config: Config

    def __init__(self, uri: str, kernel=None, config: Config = None, *args, **kw):
        super().__init__(uri=uri, kernel=kernel, config=config, *args, **kw)
        self.kernel = kernel
        config = Config() if config is None else config
        if not isinstance(config, Config):
            config = Config(config)
        self.config = config
        self.uid = hashlib.sha1(self.uri.encode('utf-8')).hexdigest()

        if self.kernel:
            self.kernel.attach(self)

    # --------------------------------------------------
    # Paths
    # --------------------------------------------------

    @property
    def root(self):
        """TBD"""
        kernel = self.kernel or self
        stats = {
            "kernel": kernel.uri,
            "hostid": f"{uuid._ip_getnode():x}",
            "hotname": socket.gethostname(),
        }

        workspace = kernel.config.g("/kernel/workspace")
        path = "{hotname}.{hostid}".format_map(stats)
        path = os.path.join(workspace, path)
        return path

    @property
    def config_file(self):
        """Get a normalized path for the config file of
        this particular resource.
        """
        uri = normalize_uri(self.uri)
        path = f"{self.root}/{uri}.yaml"
        return path

    @property
    def local_storage(self):
        """Get a normalized path for the config file of
        this particular resource.
        """
        uri = normalize_uri(self.uri)
        path = f"{self.root}/{uri}"
        return path

    def path(self, *args, local=False, **kw):
        root = self.local_storage if local else self.root
        root = expandpath(root)
        path = join_args(*args, **kw)
        path = os.path.join(root, path)
        return path

    # --------------------------------------------------
    # File config
    # --------------------------------------------------

    def load_config(self, path=None, default={}):
        """TBD"""
        path = path or self.config_file

        cfg = process_config(path)
        if cfg:
            self.config = merge(self.config, cfg)
        else:
            cfg = default
            self.config = merge(self.config, cfg)
            save_config(self.config, path)

        return self.config

    @abstractmethod
    def available(self, *what):
        """Return an iterator with the available items from configuration.
        Return cross-join of symbols and other config data.

        i.e. broker and its available subscriptions:

        >>> list(broker.available("symbols", "subscription"))
        [{'symbol': 'XS1', 'sub': '5s'},
         {'symbol': 'XS1', 'sub': 'ticks'},
         {'symbol': 'XS1', 'sub': 'depth'},
         {'symbol': 'XS2', 'sub': '5s'},
         {'symbol': 'XS2', 'sub': 'ticks'},
         {'symbol': 'XS2', 'sub': 'depth'}]
        """
        cfg = self.config
        df = None
        for key in what:
            df = df_join(df, {key: list(cfg.g(key))})

        # return join results
        for idx, row in df.iterrows():
            data = dict(row.items())
            yield data

    # --------------------------------------------------
    # Resource Bootstraping
    # --------------------------------------------------
    def _start_fiber(self, name, func, *args, **kw):
        """Fire a function in a *parallel-light-fiber* when is possible.
        Just execute function by default.
        """
        if self.kernel:
            self.kernel._start_fiber(name, func, *args, **kw)

    async def _bootstrap(self, extra_fibers=None, **kw):
        """Locate and launch all bootstrap task prior kernel main loop.

        These tasks can be defined by:

        - set missing default values
        - kernel._bootstrap_xxx() methods.
        - allocate resources described at boot configuration.
        - launch any other extra_fibers specified on boot time.

        """
        # 0. set missing default values
        for spec, value in sitems(
            {
                # 'main/root': expandpath('.'),
                "kernel/root": expandpath("."),
            }
        ):
            self.config.sd(spec, value)

        # 1. launch all _bootstrap_xxx tasks.
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

        # 2. allocate resources described at boot configuraion.
        cfg = self.config
        units = cfg.priority("/runlevel")
        for xpath in units:
            unit = cfg.g(xpath)
            uri, params = unit.get("uri"), unit.get("params")
            params["uri"] = uri
            soft(params, **cfg.sg("kernel"))
            log.info(f"Starting: {xpath}: uri: {uri}, config: {params}")
            self.allocate(uri, config=params)

        # 3. launch any other extra_fibers specified on boot time.
        for idx, func in enumerate(extra_fibers or []):
            name = f"extra_fiber_{idx}_{func.__name__}"
            self._start_fiber(name, func)

    def _launch_cross_fibers(self, *what, **kw):
        """Launch a bunch of fibers with the cross join of configuration
        elements from *what* tuple.

        This method IS NOT CALLED on resource startting, must be called
        by user.
        """
        log.info(f"Request {what} data:")
        for data in self.available(*what):
            kwargs = dict(kw)
            # msg = "{symbol}: {subscription}".format_map(data)
            # log.info(f"-----> {data}")
            iterable = list(flatten(data.items()))
            # search from more precise to less precise match
            for x in reversed(list(cpermutations(iterable))):
                # print(x)
                name = "_fib_" + "_".join(x)
                # print(name)
                func = getattr(self, name, None)
                if func:
                    soft(kwargs, **data)
                    self._start_fiber(name, func, **kwargs)
                    break
            else:
                log.warning(f"no _fib_xxxx found for: {data}")
                foo = 1

    # --------------------------------------------------
    # Main loop
    # --------------------------------------------------
    async def _preconfigure(self):
        log.debug(f"{self.uri} preconfigure ...")

    async def main(self, extra_fibers=None, *args, **kw):
        log.debug(f"{self.uri} starts ...")

        await self._preconfigure()
        await self._bootstrap(extra_fibers=extra_fibers)
        await self._loop()
        await self._term()

    async def _loop(self):
        log.debug(f"{self.uri} entering in loop ...")
        self._start_fiber("alive", self._monitor)

        while self.kernel.running:
            await sleep(1)

    async def _monitor(self):
        """Performs any supervision tasks."""
        log.debug(f"{self.uri} monitor ...")

    async def _term(self):
        """Performs any exit actions."""
        log.debug(f"{self.uri} ends ...")
    # --------------------------------------------------
    # iPubSub
    # --------------------------------------------------
    def getuid(self, target):
        if isinstance(target, iResource):
            return self.uid
        return super().getuid(target)