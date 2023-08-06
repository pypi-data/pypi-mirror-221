"""

## Workflow Template

- [ ] task definition (cajitas)
- [ ] data flow links
- [ ] handler funcion (resolved in Template loading by pluging search)
- [ ] hander funcion arguments are mapped as task in-parameters.
- [ ] handler out is only a single value (can be a dict or whatever)
- [ ] WF is also a Task: in-parameters, out results

## Wave concept

- [ ] wave key monotonic
- [ ] schedule must try to finish older waves that new ones.
- [ ] all data needed are in wave context and in the links (task-in-parameters).
- [ ] wave can be saved on disk to preserve state.
- [ ] on connection we need synchronizatoin.
- [ ] one wave runs in a single python process.
- [ ] you can connect several waves and use external REQ/res scheme (rid).

## Wave execution

- [ ] Tasks are created from template definition as wave flow comes.
- [ ] timeout from 1st data or last data update.
- [ ] schedule: finish 1


"""

# ------------------------------------------------
# In Memory Template definition
# ------------------------------------------------
# NOTE: is a Graph and can be defined, plotted,
# and saved using Standar Nodes & Edges
import re
import select
import time
import threading

from collections import deque

from uswarm.kernel import *


# ------------------------------------------------
# WF
# ------------------------------------------------


WAVE_CONNECT = "connect"
WAVE_ZERO = "zero"
WAVE_LAST = "last"


class Protocol:
    """General provider interface.

    ALL elements in WF are considered Providers.
    """

    kernel = None
    MAX_DEFERRED_WAVES = 10 ** 4
    MAX_REPLAYED_WAVES = 10 ** 2

    @classmethod
    def set_kernel(cls, kernel):
        cls.kernel = kernel

    def __init__(self, uri, **inputs):
        """
        - build initial state for start synchronization process.
        """
        self.uri = uri
        self._uri = parse_uri(uri)
        assert any(self._uri.values()), f"Bad URI '{uri}'"

        self.state = STATE_OFF

        self.inputs = inputs
        self.in_args = {}
        self.rev_inputs = {}
        for name, pub in inputs.items():
            if isinstance(pub, dict):
                pub.subscribe(self, name, **pub)
            elif isinstance(pub, Publisher):
                pub.subscribe(self, name)
            else:
                raise TypeError(f"bad subctiption data: {src} = {pub}")
            self.rev_inputs[pub] = name
        self.clean_inputs()

        # wave synchronization
        self.deferred = {}
        self.waves = {}
        # self.kernel and self.kernel.register(self)

    def clean_inputs(self):
        self.in_args = {}  # <---- (fwd in ram)
        # self.in_args.clear() # better than {} ?

    def get_uri_group(self):
        """Returns the shared configuration for
        similar actors that should be notified
        by the same (fscheme, key) event.

        by default self.uri

        other actors may return a key for the group.
        i.e. clocks may returns its lapse seconds,
        that could be shared by many clocks.

        """
        return self.uri

    # ---------------------------------
    # protocol
    # ---------------------------------
    def connect(self, provider, wave):
        """Hook to attend a new input connnection.

        bottom-level provider are connectd by kernel itself.
        higher actors by other low-level actors closer to kernel.

        state: represent the current state of provider (keys, etc)
        """
        self.waves[WAVE_CONNECT] = min(wave, self.waves.get(WAVE_CONNECT, wave))
        wzero = self.waves.setdefault(WAVE_ZERO, wave)
        self.waves[WAVE_LAST] = max(wave, self.waves.get(WAVE_LAST, wave))

        if wzero < wave:
            provider.replay(self, wzero)
            self.state = STATE_SYNC
        else:
            self.state = STATE_LIVE

    def disconnect(self, provider):
        """Hook to attend a input disconnection"""

    def handshaking(self):
        """Hook to handle out-of-sync situations."""

    def data_received(self, provider, name, item, wave, *route):
        """a new data is received from provider.
        check if we can fire handle to make a step


        --> (live)

        -- last --------------

        --> (+ deferred)

        -- conn --------------
        --> (change to transition)


        --> (process now)

        -- zero --------------

        """
        print(f"[{self.uri:35}] wave: {str(wave)}: {name} = {item} from {provider.uri}")
        if self.state == STATE_LIVE:
            deferred = False  # must be processed now
        else:
            if wave >= self.waves[WAVE_CONNECT]:
                if len(self.deferred) < self.MAX_DEFERRED_WAVES:
                    # otherways it simply discarded and a new replay
                    # process will be started after transition
                    self.deferred.setdefault(wave, {})[name] = provider, item, route
                wlast = self.waves[WAVE_LAST] = max(wave, self.waves[WAVE_LAST])
                deferred = True
            else:
                deferred = False  # must be processed now
                wzero = self.waves[WAVE_ZERO] = max(wave, self.waves[WAVE_ZERO])
                if wzero >= self.waves[WAVE_CONNECT]:
                    self.state = STATE_TRANSITION
                    # TODO: disconnect from 'sync' provider?
                    # TODO: kernel request a fiber for flushing
                    # TODO: use a clock to fire flushing steps
                else:
                    deferred = False  # must be processed now

        return deferred

    def _transition_step(self):
        """Make a step in flushing process"""
        waves = list(self.deferred.keys())
        waves.sort()
        waves = waves[: self.MAX_REPLAYED_WAVES]  # process only some waves
        for wave in waves:
            for name, (provider, item, route) in self.deferred.pop(wave).items():
                self.data_received(provider, name, item, wave, *route)

        if not self.deferred:
            # finish all saved waves... is enough?
            if wave < self.waves[WAVE_LAST]:
                provider.replay(wave)
                self.state = STATE_SYNC
            else:
                self.state = STATE_LIVE


ALL_GROUPS = "*"


class Publisher(Protocol):
    def __init__(self, uri, **inputs):
        super().__init__(uri, **inputs)

        self.actors = {}
        self.by_scheme = {}
        self.flows = {}

    def subscribe(self, actor, name="x", group=".*", **kw):
        assert self.actors.get(actor.uri) in (None, actor)
        self.actors[actor.uri] = actor

        regexp = re.compile(group, re.I | re.DOTALL | re.MULTILINE)
        # same pattern gives same compiled object id.

        # use dict for easy register/unregister and fas access
        holder = self.flows.setdefault(regexp, {})
        holder[actor.uri] = actor, name

    def data_received(self, provider, name, item, wave, *route):
        """a new data is received from provider.
        check if we can fire handle to make a step.

        Default implementation just forwards all data received.
        """
        deferred = super().data_received(provider, name, item, wave, *route)
        if not deferred:
            # check if all in-data has been received
            assert (
                name not in self.in_args
            ), f"overwriting incoming arg '{name}' before have been processed."

            self.in_args[name] = item
            if set(self.inputs.keys()).issubset(self.in_args):
                # all inputs are completed
                result = self.compute()
                # TODO: implement filter for FWD
                fqscheme = self._fwd_group(result)
                self.forward(fqscheme, wave, result, *route)
                self.clean_inputs()
        return deferred

    def compute(self):
        """Compute the condensation of received data.

        - modify internal state (wip outcome)
        - flush outcome result when is completed.

        FWD everithing
        """
        return self.in_args

    def _fwd_group(self, result):
        """Compute FWD groups.
        ALL by default.
        """
        return ALL_GROUPS

    def forward(self, fqscheme, wave, item, *route):
        """Push processed data into output provider.

        - send data to out provider.
        - start a fresh new inputs for compute the next outcome.
        """
        for regexp, holder in self.flows.items():
            if fqscheme == ALL_GROUPS or regexp.match(fqscheme):
                for actor, name in holder.values():
                    actor.data_received(self, name, item, wave, *route)

    def replay(self, target, wzero):
        """Resend all known waves from wzero to current wave."""
        # TODO: a 2nd connection is necessary?
        raise NotImplementedError()


class Kernel(Publisher):
    """The base of any Workflow Kernel."""

    def __init__(self, uri, **inputs):
        super().__init__(uri, **inputs)

        self.resources = {}

    def allocate(self, uri, actor):
        """Allocate a resource for this actor.

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

        _uri = parse_uri(uri)

        func = getattr(self, "_allocate_{scheme}".format_map(_uri), None)
        if func:
            print("Allocating: {fscheme}://.../{path} ".format_map(_uri))
            holder = func(_uri, actor)
            if holder is None:
                raise RuntimeError(f"Allocating Failled, uri: {uri}")
            foo = 1

    def _allocate_background(self, _uri, actor):
        foo = 1

    def _process_background(self):
        """Process some background tasks until MAX_BACKGROUND_TASKS
        elapsed time.

        Brackground tasks are generators that return control nicely until
        task is completed.

        The time consumed by task is the minimun time that Kernel will
        wait until try to fire the 'fiber' again, so the more time a
        'fiber' spend, the later Kernel will activate again.

        Fiber can return whatever object to return control to Kernel, but
        only float/int will be considered.

        Fiber can also yield a higher pause if the task does not requires
        too much CPU in a particula moment.

        If Kernel can not understand the yieled value, then a default penalty
        value is used, encouraging coder to use float or predefined values.

        -


        """
        pass

    def _allocate_clock(self, _uri, actor):
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

            holder = self.resources.setdefault(_uri["fscheme"], {})
            new = value not in holder
            if new:
                # particular implementation
                holder[d["value"]] = int(time.time())  # use int for easy debugging
                self.resources["min_clock"] = min(0.5, *holder.keys())

            # 1. connect()
            state = {}
            actor.connect(self, state)

            # 2. add a fwd link between kernel and actor
            holder = self.by_scheme.setdefault(actor._uri["fscheme"], {})

            holder.setdefault(value, []).append(actor)

            return holder, new

    def _allocate_tcp(self, _uri, actor):
        raise NotImplementedError()

    def _allocate_ssl(self, _uri, actor):
        raise NotImplementedError()

    def _allocate_ssh(self, _uri, actor):
        raise NotImplementedError()

    def start(self):
        """Prepare the resources based on each provider nature."""
        self.state = STATE_INIT
        for uri, actor in self.actors.items():
            self.allocate(uri, actor)

    def main(self):
        raise NotImplementedError()


class Actor(Publisher):
    """Base interface for all Workflow Actors.

    Any Actor:

    - can be identified by unique uri.
    - needs I/O events (kernel will provides).
    - connects some inputs with an output.
    - status will moves from OFF to LIVE.
    - receives events from its inputs provides.
    - may do something with data.
    - forward processed data to it output actor.

    kernel acts as the universal provider.

    all actors behaves the same way, no matter is
    a Provider or Condenser!!

    """


class IOProvider(Publisher):
    """a provider that is connectd somehow with
    Kernel I/O resources: clocks, sockets, etc.
    """

    def connect(self, provider, state):
        """Hook to attend a new input connnection.

        bottom-level provider are connectd by kernel itself.
        higher actors by other low-level actors closer to kernel.

        state: represent the current state of provider (keys, etc)
        """
        assert isinstance(
            provider, Kernel
        ), "IOProvider can connect only to a Kernel, not other actors"

    def disconnect(self, provider):
        """Hook to attend a input disconnection"""

    def handshaking(self):
        """Hook to handle out-of-sync situations."""

    def write(self, key, item):
        """Push processed data into output provider.

        - send data to out provider.
        - start a fresh new inputs for compute the next outcome.
        """


class Clock(IOProvider):
    """Implement a clock provider."""

    def get_uri_group(self):
        """Returns the shared configuration for
        similar actors that should be notified
        by the same (fscheme, key) event.

        by default self.uri

        other actors may return a key for the group.
        i.e. clocks may returns its lapse seconds,
        that could be shared by many clocks.

        """

        args = self._uri["path"]
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

            return value

        raise RuntimeError(f"BAD uri: {self.uri}")


class WriteableProvider(Publisher):
    def push(self, key, item):
        """Save item in stream with key value."""
        pass


# --------------------------------------
# Helpers
# --------------------------------------


class DemoKernel(Kernel):
    """"""

    def __init__(self, uri="kernel://localhost/demo", **inputs):
        super().__init__(uri, **inputs)

    def _allocate_clock(self, _uri, actor):
        resource, new = super()._allocate_clock(_uri, actor)
        return resource

    def start(self, timeout=10):
        super().start()

        self.t1 = time.time() + timeout
        self.th = threading.Thread(target=self.main, name="demo-kernel")
        self.th.start()

    def main(self):
        cycles = 0

        # need to start base I/O providers
        res = self.resources
        clocks = res.setdefault("clock", {})
        fds = []
        while self.state != STATE_TERM:
            # print(f"cycles: {cycles}")
            rx, tx, ex = select.select(fds, [], fds, res["min_clock"])
            t0 = time.time()
            # check clocks
            for lapse, t1 in list(clocks.items()):
                if t0 >= t1:
                    # print(f"fire clock: {lapse} : {t1}")
                    clocks[lapse] = t1 + lapse
                    # forward data: wave, item, route=lapse
                    self.forward("clock", t1, t1, lapse)

            cycles += 1
            if time.time() > self.t1:
                self.state = STATE_TERM

        # teardown ...
        # ...
        print("cleaning ...")
        time.sleep(1.0)

        self.state = STATE_OFF


class NaturalsProvider(Actor):
    """Provide natural sequence numbers starting from n0."""

    def __init__(self, uri, **inputs):
        super().__init__(uri, **inputs)

        N = self._uri["query_"].get("start", "0")
        self.N = int(N)

    def compute(self):
        """Compute the condensation of received data.

        - modify internal state (wip outcome)
        - flush outcome result when is completed.
        """
        # TODO: check that 'pulse' arg is monotonic
        self.N += 1
        return self.N


class XZProvider(WriteableProvider):
    """Provider that stores stream in XZ csv files"""


class Console(Actor):  # like a protocol
    """Show in console data flow"""
