import re
import sys
import tempfile
import shutil

import timeit
import pytest

from uswarm.tools.colors import *
from ..reactor import *
from ..network import *


@pytest.fixture()
def isdebug():
    print(f"Debug is: {__debug__}")
    modules = list(sys.modules)
    modules.sort()

    # def dump():
    # print(f"{modules}")
    # with open('modules.txt', 'w') as f:
    # for m in modules:
    # f.write(f"{m}\n")

    # dump()

    return len(set(["_winghome"]).intersection(sys.modules)) > 0


@pytest.fixture()
def delay(isdebug):
    if isdebug:
        return 600
    return 120


@pytest.fixture(scope="function")
def tmpfolder():
    d = tempfile.mkdtemp()
    yield d
    shutil.rmtree(d, ignore_errors=True)


@pytest.fixture(scope="function")
def reactor(delay):
    Reactor.clear()  # needed to avoid mixing states from test to test

    r = Reactor(name="main-reactor")
    yield r

    r.stop()


@pytest.fixture(scope="function")
def nested():
    r = Reactor(name="nested-reactor")
    return r


# -----------------------------------------------------------
# Network
# -----------------------------------------------------------
@pytest.fixture(scope="function")
def network(reactor):
    Reactor.clear()  # needed to avoid mixing states from test to test
    net = NetWorker(name="net-worker")
    # reactor.attach(net)
    return net


# ----------------------------------------------------
# FlowTesters
# ----------------------------------------------------


class FlowTester(iLog):
    """Tester class that define a flow for a test
    and try to reach each state defined.

    - monitor test evolution
    - progress and ETA
    - reuse common steps

    """

    def __init__(self, **ctx):
        super().__init__()
        self.__dict__.update(ctx)
        self.flow = {}
        self.sub_delay = 6  #: subscription delay

    async def main(self):
        """Gather all steps in the flow.
        By default it build a sequence (no branched) flow.
        """
        for name in dir(self):
            m = re.match(r"state_(?P<state>[^_]*)_(?P<name>.*)$", name)
            if m:
                d = m.groupdict()
                func = getattr(self, name)
                self.flow[d["state"]] = [d["name"], func]

        # run flow
        flow = list(self.flow.keys())
        flow.sort()

        N = len(flow)
        for i, state in enumerate(flow):
            name, func = self.flow[state]
            self.banner(f"[{i + 1}/{N}] State: {state}: {name}", _style_="banner")
            await func()

        print(f"-End-")



# ----------------------------------------------------
# Timeit
# ----------------------------------------------------


def performance(stmt="pass",
                setup="pass", \
            timer=timeit.default_timer,
            repeat=timeit.default_repeat,
            #number=timeit.default_number,
            number=timeit.default_number/1000,
        globals=None):


    number = 0 # auto-determine
    verbose = 0
    time_unit = None
    units = {"nsec": 1e-9, "usec": 1e-6, "msec": 1e-3, "sec": 1.0}
    precision = 3


    # Include the current directory, so that local imports work (sys.path
    # contains the directory of this script, rather than the current
    # directory)
    import os
    sys.path.insert(0, os.curdir)

    t = timeit.Timer(stmt, setup, timer, globals)
    if number == 0:
        # determine number so that 0.2 <= total time < 2.0
        callback = None
        if verbose:
            def callback(number, time_taken):
                msg = "{num} loop{s} -> {secs:.{prec}g} secs"
                plural = (number != 1)
                print(msg.format(num=number, s='s' if plural else '',
                                  secs=time_taken, prec=precision))
        try:
            number, _ = t.autorange(callback)
        except:
            t.print_exc()
            return 1

    try:
        raw_timings = t.repeat(repeat, number)
    except:
        t.print_exc()
        return 1

    def format_time(dt):
        unit = time_unit

        if unit is not None:
            scale = units[unit]
        else:
            scales = [(scale, unit) for unit, scale in units.items()]
            scales.sort(reverse=True)
            for scale, unit in scales:
                if dt >= scale:
                    break

        return "%.*g %s" % (precision, dt / scale, unit)


    timings = [dt / number for dt in raw_timings]

    best = min(timings)
    if verbose:
        #print("raw times: %s" % ", ".join(map(format_time, raw_timings)))
        #print()
        print("%d loop%s, best of %d: %s per loop"
              % (number, 's' if number != 1 else '',
                 repeat, format_time(best)))

    best = min(timings)
    worst = max(timings)
    if worst >= best * 4:
        import warnings
        warnings.warn_explicit("The test results are likely unreliable. "
                               "The worst time (%s) was more than four times "
                               "slower than the best time (%s)."
                               % (format_time(worst), format_time(best)),
                               UserWarning, '', 0)
    return best