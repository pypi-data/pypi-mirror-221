"""Helpers for dealing with processes, progress, speed control, etc.

Random Samples
-----------------------

- [x] progress.
- [x] speed control.
- [x] progress control.


"""
import time
from datetime import datetime
# --------------------------------------------------
# Speed control
# --------------------------------------------------


class Progress:
    """Tracks the progress of any external process."""

    def __init__(
        self,
        vf,
        current=0,
        _t0=None,
        v0=None,
        eta=None,
        speed=None,
        percent=0,
        reverse=False,
        samples=0,
        rolling=50,
        ):
        self.vf = vf
        self._t0 = _t0 or time.time()
        self.v0 = v0
        self.current = current
        if eta is None:
            self.eta = None
            self._eta = 0
        else:
            self.eta = eta
            self._eta = eta.timestamp()

        self.speed = speed
        self.percent = percent
        self.reverse = reverse
        self.samples = samples
        self.rolling = rolling

        if self.v0 is None:
            self._guess_v0()

    def _guess_v0(self):
        if self.vf.__class__ in (int, float):
            self.v0 = 1 if self.reverse else 0

    def __str__(self):
        return f"eta: {self.eta} : {int(100*self.percent)} %"

    def __repr__(self):
        return ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])

    def update(self, current):
        try:
            self.samples = min([self.samples + 1, self.rolling])

            if self.reverse:
                p = self.vf - current
                r = self.vf - self.v0
            else:
                p = current - self.v0
                r = self.vf - self.v0

            # now = time.time()
            # speed = current / (now - t0)
            # remain = (target - current) / speed
            # eta = now + remain
            # or ...
            self.percent = p / r
            _eta = (time.time() - self._t0) / self.percent + self._t0
            if self._eta:
                self._eta = self._eta + (_eta - self._eta) / self.samples
            else:
                self._eta = _eta
            self.eta = datetime.fromtimestamp(int(self._eta))
        except Exception as why:
            foo = 1


class SpeedControl(list):
    """TODO: review with PACING case for TWS, Calculate the next pause needed to keep an average
    speed limit between requests to some service.


    """

    def __init__(self, lapse=0, N=1, *args, **kwargs):
        self.lapse = lapse
        if lapse:
            N = N or int(100 / (lapse or 1)) + 1
            N = min(max(N, 10), 100)
        else:
            N = 1
        self.N = N

    @property
    def pause(self):
        "The next pause before make the next request"
        N = len(self)
        t1 = time.time()
        self.append(t1)
        t0 = self.pop(0) if len(self) > self.N else self[0]
        t1p = self.lapse * N + t0
        return t1p - t1

    @property
    def speed(self):
        "Return the current average speed"
        elapsed = self[-1] - self[0]
        if elapsed > 0:
            return len(self) / elapsed
        return 0
        # return float('inf')

    @property
    def round_speed(self):
        # return math.ceil(self.speed * 100) / 100
        return int(self.speed * 100) / 100


# --------------------------------------------------
# Progress
# --------------------------------------------------
class ProgressControl(list):
    """TODO: review: Class that implement a progress control."""

    def __init__(self, d0, d1):
        self.d0 = d0
        self.range_ = d1 - d0
        # assert self.range_ > 0

    def progress(self, d):
        return int(10000 * (d - self.d0) / self.range_) / 100
