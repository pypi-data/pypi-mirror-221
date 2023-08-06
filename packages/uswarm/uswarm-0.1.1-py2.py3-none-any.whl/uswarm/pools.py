import types
import inspect
from asyncio import gather
from itertools import chain

from .tools.calls import scall
from .tools.containers import BASIC_TYPES_EXT, ITERATOR_TYPES_EXT
from .reactor import Worker

# --------------------------------------------------------------------
# Proxy / Pool
# --------------------------------------------------------------------


class Proxy:
    """Use Magic methods for proxing a delegate instance."""

    def __init__(self, target, parent=None, _async_=False):
        super().__setattr__("_target_", target)
        super().__setattr__("_parent_", parent)
        if _async_:
            super().__setattr__("__call__", self.__async_call__)

    def __getattr__(self, name):
        print(f"get {name}")
        item = getattr(self._target_, name)
        if isinstance(item, types.MethodType):
            _async_ = item.__code__.co_flags & inspect.CO_COROUTINE
            item = self.__class__(item, _async_=_async_)

        return item

    def __setattr__(self, name, value):
        print(f"set {name} = {value}")
        self._target_.__setattr__(name, value)

    def __delattr__(self, name):
        print(f"del {name}")
        self._target_.__delattr__(name)

    def __call__(self, *args, **kw):
        print(f"call {args}, {kw}")
        return scall(self._target_, *args, **kw)

    async def __async_call__(self, *args, **kw):
        print(f"call {args}, {kw}")
        return await scall(self._target_, *args, **kw)


class DEFAULT_TARGETS:
    """Used to apply to the default targets for each Pool type."""


class Pool:
    """
    Pool of proxies.

    TODO: Inherit from Proxy ?
    """

    def __init__(self, target=None, parent=None, _async_=False, _ctx_=None):
        if isinstance(target, dict):
            pass
        elif target is None:
            target = {}
        elif isinstance(target, (list, tuple, set)):
            target = {i: vars for i, v in enumerate(target)}
        else:
            target = {0: target}

        self.__dict__["_target_"] = target
        self.__dict__["_ctx_"] = _ctx_ or {}

        if _async_:
            super().__setattr__("__call__", self.__async_call__)

    def add_target(self, *args, **kw):
        """Add some target to the Pool.

        - kw: add using its keys
        - args. add using an auto-increment value
        """
        N = len(self._target_)
        for i, item in enumerate(args):
            i += N
            while i in kw:
                N += 1
                i += 1
            kw[i] = item

        self._target_.update(kw)

    def __getattr__(self, name):
        """Called when a function or attribute is requesed.

        NOTE: Geting here means default target POLICY has been applied.
        """
        print(f"get {name}")
        barrier = {}
        asyncs = []
        call = None
        wrap = None

        for key, t in self._target_.items():
            item = getattr(t, name)
            if isinstance(item, types.MethodType):
                # wrap methods
                assert call in (None, True)
                _async_ = item.__code__.co_flags & inspect.CO_COROUTINE
                call = True
            elif isinstance(item, BASIC_TYPES_EXT):
                # return basic types
                assert call in (None, False)
                _async_ = None
                call = False
            else:
                assert wrap in (None, True)
                _async_ = None
                wrap = True

            barrier[key] = item
            asyncs.append(_async_)

        if barrier:
            assert all(
                [a == _async_ for a in asyncs]
            ), f"all {name} methods must be sync or async at the same time."
        else:
            _async_ = None

        if call or wrap:
            barrier = self.__class__(target=barrier, _async_=_async_, _ctx_=self._ctx_)

        return barrier

    def __setattr__(self, name, value):
        print(f"set {name} = {value}")
        for t in self._target_.values():
            t.__setattr__(name, value)

    def __delattr__(self, name):
        print(f"del {name}")
        for t in self._target_.values():
            t.__delattr__(name)

    def __call__(self, *args, **kw):
        """Make a func call to every target in Pool.

        NOTE: we use default _policy() to select the
        final targets (ALL by base class Pool).

        RoundRobinPoll or others Pools will apply a different
        Policy.

        """
        print(f"call {args}, {kw}")
        result = {}

        for key, t in self._policy().items():
            try:
                result[key] = scall(t, *args, **kw)
            except Exception as why:
                print(why)
                raise

        # I don't know why, asyncio call the original call
        # even we patch, so we need to handle this issue here
        if self.__call__ == self.__async_call__:
            result = self._gather(result)
        return result

    async def _gather(self, targets):
        """Wait for a list of coro's results and return
        results in the same order.
        """
        keys = []
        aws = []
        for k, coro in targets.items():
            keys.append(k)
            aws.append(coro)

        r = await gather(*aws)

        result = {}
        for i, value in enumerate(r):
            result[keys[i]] = value

        # return await gather(*targets.values())
        return result

    async def __async_call__(self, *args, **kw):
        print(f"call {args}, {kw}")
        print(f"call {args}, {kw}")
        result = []
        for t in self._target_:
            try:
                r = await scall(t, *args, **kw)
                result.append(r)
            except Exception as why:
                foo = 1

        return result

    # slices for accessing specific items
    def __getitem__(self, key):
        """I decide to hide [] operator from proxied items.
        TODO: extend key to be a keys iterator, beside slices.
        """
        target = self._policy(key)
        if len(target) > 1:
            return self.__class__(target=target)
        return Proxy(target=target.popitem()[1])

    def _policy(self, targets=None):
        """DEFAULT Pool policy.

        Just select ALL elements when no argument is pased or
        select some targets based on key: index, keys, slices, iterators, etc.

        Overrige this method to implement different default
        policies for selecting targets based on key: ROUND_ROBIN, etc.

        Note: a target can be in many Pools, but Pools do not share
        activity information (by now) so PACING policies should be
        implemented in target side.
        """
        target = {}
        targets = self._target_.keys() if targets is None else targets

        if isinstance(targets, slice):
            # selected by slice
            keys = []
            idx = targets.start
            while idx < targets.stop:
                keys.append(idx)
                start, idx, step = targets.indices(idx)
                idx = idx + step
            targets = keys

        if isinstance(targets, ITERATOR_TYPES_EXT):
            # single object as targets
            targets = set(chain(targets))
        else:
            targets = set([targets])

        if isinstance(targets, (set,)):
            # selected by sequence
            # is targets is not found, then use the next target
            # for building the target sub-pool.
            # targets = set(targets)
            available = list(self._target_.keys())
            available.sort()
            while targets and available:
                k = targets.pop()
                if k not in self._target_:
                    k2 = available.pop(0)
                    target[k] = self._target_[k2]
                else:
                    target[k] = self._target_[k]

        return target

    def __setitem__(self, key, item):
        raise NotImplementedError()

    def __getslice__(self, key1, key2):
        raise NotImplementedError()

    def __setslice__(self, key1, key2, value):
        raise NotImplementedError()


class RoundRobinPoll(Pool):
    def __init__(self, _ctx_=None, *args, **kw):
        _ctx = _ctx_ or {'idx': -1}

        super().__init__(_ctx_=_ctx, *args, **kw)

    def _policy(self, targets=None):

        idx = self._ctx_['idx'] + 1

        if idx >= len(self._target_):
            idx = 0
        if idx < len(self._target_):
            target = super()._policy(idx)
        else:
            target = {}

        self._ctx_['idx'] = idx
        return target


# ------------------------------------
# TBDPoolPools: # TODO: review ...
# ------------------------------------


class TBDPool(Worker):
    """"""

    # Pool policy
    ROUND_ROBIN = "round-robin"
    RANDOM = "random"

    # status
    DISABLED = "disabled"
    DOWN = "down"
    INIT = "init"
    READY = "ready"

    """A elements pool.

    Hide server selection details to any client.

    Differnte POLICIES can be applied:
    - general round-robin.
    - specific round-robin.
    - based on url
    - random
    - etc

    """
    PACING = 10

    def __init__(self, items, policy=ROUND_ROBIN):
        self.items = items or []
        self.status = {}
        self.delay = 5

    async def _enter(self):
        await super()._enter()
        for item in self.items:
            self._update(item, self.DOWN, None, -1)

    def _update(self, item, status, result=None, when=0):
        when = when or self.time
        data = self.status.get(item)
        if not data:
            self.status[item] = [self.time, status, result]
        else:
            data[0:2] = self.time, status
            data[2] = data[2] or result

    async def _do(self):
        """Handle the servers pool:"""
        while self.running:
            await sleep(1)
            t1 = self.time
            for item, (t0, status) in self.items.items():
                if status in (self.DOWN,) and (t1 - t0) > self.PACING:
                    # reconnect one by one. Better not in parallel
                    # it will be faster enougth
                    status = await self._activate(item)

    async def _activate(self, item):
        self._update(item, self.INIT)

    def next(self):
        raise NotImplementedError()
