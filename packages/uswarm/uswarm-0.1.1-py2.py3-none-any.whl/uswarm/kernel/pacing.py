"""TODO: delete this file ? """
from collections import deque
from time import time

# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger

log = logger(__name__)

# --------------------------------------------------
# Pacing Request Intensity
# --------------------------------------------------
class Pacing:
    """Class to handle PACING violations due too many requests
    for a single source.

    # https://interactivebrokers.github.io/tws-api/historical_limitations.html#pacing_violations

    1. The maximum number of simultaneous open historical data requests from the API is 50.
       In practice, it will probably be more efficient to have a much smaller number of
       requests pending at a time.

    2. Making identical historical data requests within 15 seconds.

    3. Making six or more historical data requests for the same Contract,
       Exchange and Tick Type within two seconds.

    4. Making more than 60 requests within any ten minute period.

    Note that when BID_ASK historical data is requested, each request is counted twice.

    In a nutshell, the information above can simply be put as "do not request too much
    data too quick".

    """

    def __init__(self, n, window, uri=None):
        self.max_n = n  #: number of request inside 'window' period
        self.window = window  #: time 'window' period
        self.max_speed = n / window
        self.uri = uri  #: reference to "paced" object
        self.delay = 10

        self.timeouts = []
        self.lapse = 1
        self.recalc()

    def recalc(self):
        if len(self.timeouts) >= 2:
            elapsed = self.timeouts[-1] - self.timeouts[0]
            samples = len(self.timeouts)
            current_speed = samples / elapsed

            remain_time = self.window - elapsed
            remain_samples = self.max_n - samples
            remain_speed = remain_samples / remain_time

            speed = remain_speed * 0.25 + current_speed * 0.25 + self.max_speed * 0.50

            roundtrip = 0.0  #: secs
            lapse = 1 / speed - roundtrip
            # lapse = 0
            self.lapse = lapse + self.delay
            self.delay *= 0.90

            log.debug(
                f"[{self.uri}] PACING n: {current_speed}, {remain_speed}, {speed} -> {self.lapse}"
            )

    def slow(self):
        self.delay += 2 * self.window / self.max_n

    def when(self):
        """Compute when a request must be fired to avoid PACING VIOLATION."""
        now = time()
        t0 = now - self.window

        # clean already sent time-marks
        while self.timeouts:
            if self.timeouts[0] < t0:
                self.timeouts.pop(0)
            else:
                break

        t1 = now + self.lapse
        self.timeouts.append(t1)
        self.recalc()

        log.warning(f"[{self.uri}] load: {len(self.timeouts)}")
        delays = [
            self.timeouts[i] - self.timeouts[i - 1]
            for i in range(1, len(self.timeouts))
        ]
        delays = [f"{x:0.2f}" for x in delays]
        log.debug(f"[{self.uri}] {delays}")
        log.debug(f"[{self.uri}] lapse: {self.lapse}, window: {self.window}")
        for i, x in enumerate(self.timeouts):
            log.debug(f"[{i}] : {x - now}")

        return t1
