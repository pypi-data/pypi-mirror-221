import random
import sys
import traceback

from time import sleep

from .kernel import *
from .dom import DOM
from .userver import *
from .pool import Pool

# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger, log_container

log = logger(__name__)

# --------------------------------------------------
# SelectKernel
# --------------------------------------------------


class SelectKernel(Kernel):
    """
    There is no other event that I/O activity and timers, so:

    - Channels that have fd descriptors.
    - use select() for fd activity.
    - timer for pusing time to any Node instance.

    # TODO: move down workflow and links between nodes.

    """

    def __init__(self, uri="kernel://select-demo", kernel=None, *args, **kw):
        self.queues = {}
        self.links = {}

        self.fds_rx = {}
        self.fds_tx = {}

        super().__init__(uri, kernel, *args, **kw)

    # queues
    # def register_queue(self, queue: WQueue):
    # self.queues[queue.uri] = queue

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
        timers = self.resources["each"]
        self.busy_time_mark = time()
        self.busy_time_elapsed = 0
        remain = 1e-06
        self.time = time()

        signals_captured = 0

        try:
            while self.running and signals_captured < 5:
                # loop to catch CTRL+C
                try:
                    while self.running:
                        # remain = min(0.5, remain)
                        log.debug(f" --- select for : {remain}")
                        rx, tx, ex = select(
                            fds_rx, fds_tx, fds_rx, remain if remain > 0 else 0
                        )

                        self.time = busy_time_mark = time()
                        # ----------------------------------------------------
                        # Check I/O
                        # ----------------------------------------------------
                        for fd in ex:
                            print(f"error on : {fd}")
                            foo = 1

                        for fd in tx:
                            try:
                                fds_tx[fd].tx()
                            except ConnectionError as why:
                                log.warning(
                                    f"connection lost while writting: {fds_tx[fd]}"
                                )
                                fds_tx[fd].connection_lost()
                                if fd in rx:
                                    rx.remove(
                                        fd
                                    )  # avoid unnnecessry "KeyError" processing rx
                            except OSError as why:
                                log.warning(
                                    f"connection lost while writting: {fds_tx[fd]}"
                                )
                                fds_tx[fd].connection_lost()
                                if fd in rx:
                                    rx.remove(
                                        fd
                                    )  # avoid unnnecessry "KeyError" processing rx

                        for fd in rx:
                            try:
                                fds_rx[fd].rx()
                            except ConnectionError as why:
                                log.warning(
                                    f"connection lost while reading: {fds_rx[fd]}"
                                )
                                fds_rx[fd].connection_lost()

                        # ----------------------------------------------------
                        # Check Timers
                        # ----------------------------------------------------
                        # self.time = time()
                        while True:
                            t0, timer0 = timers[0]
                            if t0 > self.time:
                                break

                            # rearm timer
                            timers.pop(0)
                            timer0.cycles -= 1
                            if timer0.cycles != 0:
                                t00 = (
                                    timer0.restart + self.time
                                    if isinstance(timer0, Each)
                                    else t0
                                )
                                for i, (t2, timer2) in list(enumerate(timers)):
                                    if t2 > t00:
                                        timers.insert(i, (t00, timer0))
                                        break
                                else:
                                    timers.append((t00, timer0))
                                log.debug(f"rearm timer: {t00} : {timer0.cycles}")
                            else:
                                log.debug(f"timer: {timer0} expired")

                            # handle timer after rearm, so
                            # kernel load can be better meassured
                            # timer0.push(t1)  # faster following implementation
                            self.enqueue(timer0.uri, timer0.event, (t0, timer0.cycles))

                        # ----------------------------------------------------
                        # Check Pending Tasks
                        # ----------------------------------------------------
                        self.date = datetime.fromtimestamp(self.time)
                        t_limit = timers[0][0]
                        remain = t_limit - self.time

                        # In every loop, kernel will consume a whole
                        # port activity before checking timers
                        # This will save for creating auxiliary lists
                        # needed to have a more fine time granularity.

                        while self.port_activity and remain > 0.001:
                            # TODO: use a priority list
                            port, _ = self.port_activity.popitem()

                            # now we need to consume the whole port data
                            log.debug(f"--- dispatching: #[{port}] events ...")
                            queue = self.ports.get(port)
                            while queue:
                                params = queue.popleft()
                                # log.debug(f"   ====> {params}")
                                # we need to create a list to avoid
                                # "builtins.RuntimeError: dictionary changed size during iteration"
                                # or create another event to add subscribres in other ports (future)
                                for uri, resource in list(
                                    self.subscribers.get(port, {}).items()
                                ):
                                    # log.debug(f"      ---> {uri}.dispatch()")
                                    resource.dispatch(*params)

                                self.time = time()
                                remain = t_limit - self.time
                                if remain < 0.001:
                                    if queue:
                                        self.port_activity[port] = True
                                        # log.info(
                                        # f"--- REACTIVATING port: {port} due not finished tasks"
                                        # )
                                        break
                                    # log.info(
                                    # f"--- Breaking dispatching... need to attend timers"
                                    # )
                                    break

                        self.time = time()
                        remain = t_limit - self.time
                        self.busy_time_elapsed += self.time - busy_time_mark

                except KeyboardInterrupt as why:
                    event = EVENT_TERM if signals_captured < 2 else EVENT_QUIT
                    log.warning("=" * 60)
                    log.warning(
                        f"Signal TERM received .... sending shutdown({event}): {signals_captured}"
                    )
                    log.warning("=" * 60)
                    self.shutdown(event)
                    signals_captured += 1

        except Exception as why:
            exc_type, exc_value, exc_tb = sys.exc_info()
            tb = traceback.format_exception(exc_type, exc_value, exc_tb)
            tb = "".join(tb)
            # trace(message=tb, level=logging.ERROR, frames=2)

            log.exception(tb)
            self.running = False

        log.debug("<< main")

    # --------------------------------------------------
    # Kernel Bootstraping
    # --------------------------------------------------

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

    # --------------------------------------------------
    # DOM Factory
    # --------------------------------------------------

    # --------------------------------------------------
    # TODO: review these resources
    # --------------------------------------------------
    def push(self, wave, queue, result):
        # TODO: review
        # print(f"push: ~{wave} : {queue} : r={result}")
        holder = self.links.get(queue.uri, {})
        for target, param in holder.items():
            target_ = self.queues[target]
            target_.push(wave, {param: result})
        foo = 1

    def link(self, source, target, param=None):
        # TODO: review
        holder = self.links.setdefault(source.uri, dict())

        if param is None and target.specs.args:
            param = target.specs.args[0]

        holder[target.uri] = param
