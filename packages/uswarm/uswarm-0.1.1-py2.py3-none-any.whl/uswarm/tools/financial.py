import random

from dataclasses import dataclass


from arrow import Arrow

import exchange_calendars as xcals

# import pandas_market_calendars as mcal

from uswarm.sparse import DateRepository, DateSparseFile
from uswarm.tools import (
    expandpath,
    fileiter,
    soft,
    supdate,
    _find_match,
    _prepare_test_regext,
)
from uswarm.tools.units import timeframe2delta, parse_date, parse_arrow, neg_delta

from uswarm.tools.grid import Grid
from uswarm.tools.stream import *

import arrow

# from arrow import Arrow

# --------------------------------------------------
# Exchange calendars
# --------------------------------------------------
# X_CMES = xcals.get_calendar("CMES")  # , start='2015')
# foo = X_CMES.trading_index(
# "2022-05-07",
# "2022-05-17",
##period="90T",
# period="1min",
# force_close=True,
# force_break_close=True,
# curtail_overlaps=True,
# )


# def skip_holydays(t0):
## minute_to_trading_minute

# t0 = arrow.get(t0)

# return t0


def sign(x):
    return -1 if x < 0 else 1


# ----------------------------------------------------------
# Brouniam movements
# ----------------------------------------------------------


def create_GBM(base, s0, mu, sigma, quantum=None):
    """
    Generates a price following a geometric brownian motion process based on the input of the arguments:
    - s0: Asset inital price.
    - mu: Interest rate expressed annual terms.
    - sigma: Volatility expressed annual terms.
    """
    from random import gauss, seed
    from math import sqrt, exp

    base = base - s0
    if quantum:
        base = (base // quantum) * quantum

    st = s0
    frac = 1.0 / 365.0
    sqrfrac = sqrt(frac)

    def generate_value():
        nonlocal st

        st *= exp(
            (mu - 0.5 * sigma ** 2) * frac + sigma * sqrfrac * gauss(mu=0, sigma=1)
        )
        if quantum:
            x = st / quantum
            f = x - int(x)
            if f > 0.5:
                x += 1
            st = int(x) * quantum
        return base + st

    return generate_value


def stream_GBM_old(base, s0, mu, sigma, quantum=None):
    func = create_GBM(base, s0, mu, sigma, quantum)
    while True:
        yield func()


def GBM(s0, mu, sigma, period=200, quantum=None):
    """
    Generates a price following a geometric brownian motion process based on the input of the arguments:
    - s0: Asset inital price.
    - mu: mean of percent returns
    - var2 =
    - sigma: Volatility expressed annual terms.


    S_i+1 = S_i * exp( mu - 0.5*var2 `` )
    """
    from random import gauss
    from math import sqrt, exp

    st = s0
    frac = 1.0 / period
    sqrfrac = sqrt(frac)

    half_var = 0.5 * (sigma ** 2)
    drift = (mu - half_var) * frac
    amp = sigma * sqrfrac

    while True:
        st *= exp(drift + amp * gauss(mu=0, sigma=1))
        if quantum:
            x = st / quantum
            f = x - int(x)
            if f > 0.5:
                x += 1
            x = int(x) * quantum
            yield x
        else:
            yield st


# ----------------------------------------------------------
# Price Stream
# ----------------------------------------------------------


class TicksStream(SourceStream):
    """Ticks Stream inspired in IB ticks stream."""


class DepthStream(SourceStream):
    """Depth Of Market stream.
    Note that may not be compatible with other streams.
    """

    pass


class Point(Grid):
    ACC = {"a", "b"}
    ROUND = {
        "a": 1,
        "b": 1,
        "h": 0.25,
        "l": 0.25,
        "p": 0.25,
        "v": 1,
        "t": 1,
    }
    MAX = {
        "p": "h",
    }
    MIN = {
        "p": "l",
    }


class X1Point(Point):
    ACC = {"x"}

    ROUND = {
        "h": 0.50,
        "l": 0.50,
        "p": 0.50,
    }


class X2Point(Point):
    "Example for inherited attributes"
    ACC = {"y"}

    ROUND = {
        "h": 0.10,
        "l": 0.10,
        "p": 0.10,
    }


class X3Point(X2Point):
    "Example for inherited attributes"
    ACC = {"z"}


class BarStream(SourceStream):
    """Generic Bar generator.

    Uses:
    - a 'zero' reference point as base reference.
    - a 'current' point (last state).
    - a 'bounds' point to know when a new bar must be generated.

    When a new point is received then 1 o more bars can be created
    to reflect the transition from last point to the new state.
    """

    def __init__(self, source, **bounds):
        super().__init__()
        self.current = Point()  #: current increassing point
        self.bounds = Point(bounds)  #: limits per coordenate (if any)

        # Reference points for grid
        # set by _init_block()
        self.zero = Point()  #: staring point
        self.zero_box = Point()  #: starting point in grid coordinates.

        self.crossing = Point()
        self.over_key = None
        self.over_value = 0

        self.ready_bars = []  #: a list of bars ready to serve

        self.source = source  #: "flow" chain
        self._source = None  #: generator from source
        self.status = ST_DISCONNECTED

        # streaming
        # self._operations = {
        # "a": self._acc_operation,  #: ask
        # "b": self._acc_operation,  #: bid
        # "p": self._set_operation,  #: price
        # "v": self._acc_operation,  #: relative volume
        # }
        # self._post_operations = {
        # "p": [
        # (self._max_operation, ("h", "p")),
        # (self._min_operation, ("l", "p")),
        # ],
        # }

    def __iter__(self):
        if not self.bounds:
            raise RuntimeError("you must set almost 1 bounding limit for creating bars")
        # self._handshaking()
        return super().__iter__()

    def _handshaking(self):
        """Performs a handshaking with source *moving*
        the current point as input stream commands
        until we got the 'zero' (starting) point.

        'zero' point is reached when all required
        for this kind of stream are completed.
        """
        # create the generator stream
        self._source = iter(self.source)

        required = set(["p", "t", "v"])
        data = self.current

        for i, tick in enumerate(self._source):
            # translate ticks keys names to point ones.
            point = self.to_point(tick)
            data.move(point)
            # check if all required fields are set
            if not required.difference(data):
                print(data)
                break
            if i > 200:
                raise RuntimeError(
                    "Handshaking failed: can not get initial data from input tick stream"
                )

        self.current.limits()
        self._init_block()

    def _init_block(self):
        """Compute relative 'zero' coordinate origin
        from point, preserving any key not bounded
        and replacing all bounded keys with grid values.
        """
        self.current.reset()
        self.zero = self.current.copy()

        self.zero_box = self.current // self.bounds
        zero = self.zero_box * self.bounds
        self.zero.update(zero)

        self.zero.reset()

        foo = 1

    def _stream(self):
        if self.status in (ST_DISCONNECTED,):
            self._handshaking()

        for tick in self._source:  # use same iterator instance
            # if tick in (DISCONNECTION):
            # self.status = ST_DISCONNECTED
            # self._handshaking()
            # continue

            point = self.source.to_point(tick)
            self._datapoint(point)
            while self.ready_bars:
                yield self.ready_bars.pop(0)

            if not self.running:
                break

    # ------------------------------------------------------
    # streaming
    # ------------------------------------------------------

    def _datapoint(self, point):
        """Add point information to current bar and create
        any bars needed when limits are overflowed.

        TODO:
        - [x] save current delta and compute the new one.
        - [x] in overflow, compute last jump micro-delta.
        - [ ] select the winner direction (vector) to move.
        - [ ] iterate calculating the next micro-step to reach
              the winner (closer) boundary.
              we assume boundaries sizes are fixed.
        - [ ] create a new bar from current point.
        - [ ] iterate until remain micro-delta is contained in a
              single block.
        - [ ] spread time across deltas as well

        - [ ] spread time across deltas as well
        - [ ] in GAP case, ask for missing data and rebuild bars as possible.

        Big GAP case:

        If source is ticks and there is a big GAP due a disconnection,
        the next generated points would be very inprecise.

        Price evolution may be more close to reallity but cummulative
        data (i.e volume) definetely will not due all missing data.

        Stream must be marked as *blur* and we request missing data
        from broker.

        It should be possible to alter already generated bars as more
        precise data comes from the broker and we should be able to
        inform bar-listeners that their bars have been updated.

        Note: Is broker sends absolute volume from session starting
        me can be checked that everything is ok comparing my accumulate
        volme with broker absolute value as a regular check.

        Loading historical ticks may require more complex self-updating.

        Overflow scheme

        - zero (z0, z1, ...) : the starting points of a block.
        - delta: current (point - zero) vector.
        - last delta: last increment from last point to current point.

        +--------------+
        |              |
        |         .ld  |
        |         ^    | create bars while remain
        |         |    |
        +-------*-------+ z1, p1, h1, l1, v1
        |       ^      |
        |       |      |
        |    .d |      |
        |              |
        +--------------+
        z0,  ...

        Operations:

          set: p, t, v (absolute)
          acc: dv
          max: (h, p)
          min: (l, p)

        Quality Control:

        We have absolute and incremental values for 'volume' data.

        - meassuring deltas between absolute values may help in GAP detection.
        - absolute value may match with accummulaive delta values.
          show warning otherwise.

        """
        # apply point information on current point

        end = self.current.copy().move(point)
        end.limits()

        # print(f">> {point}: {new}")
        while True:
            # num of overflow 'blocks' from zero in each axis.
            n = (end - self.zero) / self.bounds
            # the axis where block breaks (positive or negative)
            exit_axis, over_val = n.argabsmax()

            if abs(over_val) > 1:
                # we have an overflow on 'over_key' axis.
                # Now we start a process to "spread" the delta
                # from current position to new point accross
                # all crossed "boxes" (typially just one)

                # 1. compute the exit point inside current block
                # along the exit axis
                delta = end - self.current
                u = delta.single(exit_axis)
                border = self.zero + (self.bounds * u)

                # 2. compute the fraction of current jump to reach the
                # is the border over the exit axis.
                alpha = (border - self.current) / delta
                alpha_key, alpha_val = alpha.argabsmax()

                # now we 'spread' values proportionally from current
                # point to border, subtracting from the end point
                # and repeat the process until the next jump is contained
                # in the current block.

                # 3. jump to border
                jump = delta.I * alpha_val * delta
                jump.round()
                if False:
                    print(f"point : {point}")
                    print(f"new   : {end}")
                    print(f"cur   : {self.current}")
                    print(f"zero  : {self.zero}")
                    print(f"n     : {n}")
                    print(f"border: {border}")
                    print(f"delta : {delta}")
                    print(f"alpha : {alpha}")
                    print(f"jump  : {jump}")

                # 4. move the current point to the border
                # and subtract cummulative values from end point
                self.current += jump
                # assert the jump reach the exit point in the border block.
                assert border == self.current * alpha.I

                # 5. add a new bar with the just created 'cell'
                bar = self.current.copy()
                bar.limits()
                # print(f"bar   : {bar}")
                self.ready_bars.append(bar)

                # start a new 'fresh' cell from current point
                self._init_block()

                # 6. decrease cummulative attributes from end point
                # that has been used in last 'jump' to reach the border.
                # new = new - bar * delta.A
                delta = delta - jump
                end = self.current + delta
            else:
                self.current = end
                break


class BarStreamTicks(BarStream):
    """Generate Bars from TickStream."""


class CandlestickStream(BarStreamTicks):
    """Bars that are created on 'time' overflow."""

    def __init__(self, source, **bounds):
        bounds.setdefault("t", 1)
        super().__init__(source, **bounds)


class VolumeBarsStream(BarStreamTicks):
    """Bars that are created on 'volume' overflow."""

    def __init__(self, source, **bounds):
        bounds.setdefault("v", 1000)
        super().__init__(source, **bounds)


class AtlasBarStream_Ticks(BarStreamTicks):
    """Atlas bars takes ticks stream or any other BarStream."""


# ----------------------------------------------------------
# Price Stream Generation
# ----------------------------------------------------------
# TODO: simulate Ticks and Depth streams


class DemoTicksStream(TicksStream):
    def __init__(
        self,
        base,
        s0,
        mu,
        sigma,
        quantum=None,
        timeframe="1s",
        t0=None,
        daily_volume=0,
        gap_prob=0,
        gap_duration=0,
    ):
        super().__init__()

        self.generator = create_GBM(base, s0, mu, sigma, quantum)
        self.price = base  #: last price
        t0 = t0 or Arrow.utcnow()  # TODO: from datetime.timestamp as well
        self.t0 = int(t0.timestamp())
        self.delta = timeframe2delta(timeframe).total_seconds()
        self.daily_volume = daily_volume
        self.gap_prob = gap_prob
        self.gap_duration = gap_duration

    def _stream(self):
        delta = self.delta
        last_operation = self.generator()
        # flush_vol = 0
        send_vol = False

        n = 0
        t1_mute = 0
        publish = True

        # TODO: review tick stream order in TWS
        # TODO: volume is sent 1st or later price ??
        # TODO: simulate market close (rth/overnigth)
        yield CONNECTION
        while self.running:
            # Tick price BID/ASK
            price = self.generator()
            n += 1

            placement = random.randint(1, 10)
            if random.random() < 0.5:
                if publish:
                    tick = {BID_PRICE: price, BID_SIZE: placement}
                    # yield self.to_point(tick)
                    yield tick
                if last_operation < price:
                    # flush_vol += placement
                    self.daily_volume += placement
                    last_operation = price
                    send_vol = True
            else:
                if publish:
                    tick = {ASK_PRICE: price, ASK_SIZE: placement}
                    # yield self.to_point(tick)
                    yield tick
                if last_operation > price:
                    # flush_vol += placement
                    self.daily_volume += placement
                    last_operation = price
                    send_vol = True

            # Tick Time
            # print(f"-- {flush_vol}")
            if send_vol or (random.random() < 0.05):  # and flush_vol > 0):
                # TODO: publish VOL from opening day (self.volume)
                if publish:
                    tick = {VOLUME: self.daily_volume}
                    # yield self.to_point(tick)
                    yield tick

                # flush_vol = 0
                send_vol = False

            # Tick Time
            if random.random() < 0.3:
                self.t0 += delta
                if publish:
                    tick = {TIME: self.t0}
                    # yield self.to_point(tick)
                    yield tick

                if not publish:
                    if self.t0 > t1_mute:
                        publish = True
                        yield CONNECTION

            # Simulate GAP muting stream for a while
            if not n % 1000:
                if random.random() < self.gap_prob:
                    t1_mute = random.randint(1, self.gap_duration)
                    print(f"Generting GAP for {t1_mute} secs")
                    t1_mute += self.t0
                    publish = False
                    yield DISCONNECTION


# ----------------------------------------------------------
# Tinny Account Simulator
# ----------------------------------------------------------


class AccountSim:
    def __init__(self):
        self.lifo = []
        self.pos_size = 0
        self.realized = 0.0
        self.unrealized = 0.0
        self.n_trades = 0
        self.n_orders = 0

    def place_order(self, t0, n, p):
        lifo = self.lifo
        realized = self.realized
        if n != 0:
            self.n_trades += abs(n)
            self.n_orders += 1

            closing = n * self.pos_size < 0
            if closing:
                remain = n
                while remain != 0:
                    available, p0 = entry = lifo[0]
                    used = sign(available) * min(abs(available), abs(-remain))
                    remain += used
                    profit = (p - p0) * used
                    self.realized += profit
                    entry[0] -= used
                    if entry[0] == 0:
                        lifo.pop(0)
                # balance = pos_value - p * n
                # pos_value = pos_value - p * n
            else:
                lifo.append([n, p])
            self.pos_size += n

            # pos_value = pos_value - p * n

        self.unrealized = self.pos_size * p - sum([n0 * p0 for n0, p0 in self.lifo])
        foo = 1
        record = (
            t0,
            n,
            p,
            self.pos_size,
            self.realized - realized,
            self.unrealized,
            self.realized,
            self.n_trades,
            self.n_orders,
        )
        return record
        foo = 1


# ------------
class HistoricalFile(DateSparseFile):
    """Historical Base File."""


class HistoricalRepository(DateRepository):
    """Historical Repository for FinTech."""

    DEFAULT_FACTORY = HistoricalFile
    DateRepository.PATH.update(
        {
            "trade": "{provider}/{klass_name}/{sub}/{date1}-{date2}.{fmt}.{ext}",
            "historical": "{provider}/{klass_name}/{sub}/{date1}-{date2}.{fmt}.{ext}",
        }
    )

    supdate(
        DateRepository.DEFAULT_QUERY,
        {
            "trade": {
                "timeframe": "1w",
            },
        },
    )

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self._add_patterns(
            # ib/trades/agp/20211129-20211205.csv.xz
            r"""(?imux)
            # main: provider, klass-type and sub-topic
            (?P<provider>[^./]+)
            ([./](?P<klass_name>[^./-]+))
            ([./-](?P<sub>[^./-]+))?

            # date is optional
            (
              [./-]
              (?P<key1>
                (?P<date1>(?P<year1>\d{4})-?(?P<month1>\d{2})-?(?P<day1>\d{2}))
              )
              [./-]
              (?P<key2>
                (?P<date2>(?P<year2>\d{4})-?(?P<month2>\d{2})-?(?P<day2>\d{2}))
              )
            )?

            # last details: timeframe, data format (csv, etc) and extesion (xz, ...)
            ([./-](?P<timeframe>\d+[smhd]))?
            ([./-](?P<fmt>(csv)))?
            ([./-](?P<ext>(xz)))?
            $
            """,
            ## ib/ESU8/bar/20180903/070000-080000.1s.xz
            # r"""
            # (?P<provider>[^./]+)(\.|/|-)
            # (?P<local_symbol>[^./]+)(\.|/|-)
            # (?P<klass_name>[^./]+)(\.|/|-)
            # (?P<date1>(?P<year1>\d{4})-?(?P<month1>\d{2})-?(?P<day1>\d{2}))(\.|/)
            # (?P<time1>(?P<hour1>\d{2}):?(?P<min1>\d{2}):?(?P<sec1>\d{2})(\.(?P<usec1>\d+))?)(\.|/|-)
            # (?P<time2>(?P<hour2>\d{2}):?(?P<min2>\d{2}):?(?P<sec2>\d{2})(\.(?P<usec2>\d+))?)(\.|/|-)
            # (?P<timeframe>\d+[smhd])(\.|/-)
            # (?P<ext>[^.]+)
            # $
            # """,
            ## ib/ESU8/bar/1s/20180903/070000-080000.xz
            # r"""
            # (?P<provider>[^./]+)(\.|/|-)
            # (?P<local_symbol>[^./]+)(\.|/)
            # (?P<klass_name>[^./]+)(\.|/)
            # (?P<timeframe>\d+[smhd])(\.|/)
            # (?P<begin>
            # (?P<date1>
            # (?P<year1>\d{4})-?(?P<month1>\d{2})-?(?P<day1>\d{2})
            # )-?
            # (?P<time1>
            # (?P<hour1>\d{2}):?(?P<min1>\d{2}):?(?P<sec1>\d{2})(\.(?P<usec1>\d+))?
            # )
            # )
            # \.
            # (?P<end>
            # (?P<date2>
            # (?P<year2>\d{4})-?(?P<month2>\d{2})-?(?P<day2>\d{2})
            # )-?
            # (?P<time2>
            # (?P<hour2>\d{2}):?(?P<min2>\d{2}):?(?P<sec2>\d{2})(\.(?P<usec2>\d+))?
            # )
            # )
            # \.
            # (?P<ext>[^.]+)
            # $
            # """,
            ## ib/ESU8/bar/20180903-070000.20180903-080000.1s.xz
            # r"""
            # (?P<provider>[^./]+)(\.|/|-)
            # (?P<local_symbol>[^./]+)(\.|/)
            # (?P<klass_name>[^./]+)(\.|/)
            # (?P<begin>
            # (?P<date1>
            # (?P<year1>\d{4})-?(?P<month1>\d{2})-?(?P<day1>\d{2})
            # )-?
            # (?P<time1>
            # (?P<hour1>\d{2}):?(?P<min1>\d{2}):?(?P<sec1>\d{2})(\.(?P<usec1>\d+))?
            # )
            # )
            # \.
            # (?P<end>
            # (?P<date2>
            # (?P<year2>\d{4})-?(?P<month2>\d{2})-?(?P<day2>\d{2})
            # )-?
            # (?P<time2>
            # (?P<hour2>\d{2}):?(?P<min2>\d{2}):?(?P<sec2>\d{2})(\.(?P<usec2>\d+))?
            # )
            # )
            # \.
            # (?P<timeframe>\d+[smhd])(\.|/)
            # (?P<ext>[^.]+)
            # $
            # """,
            ## ib/ESU8/bar/1s/20180903-070000.20180903-080000.xz
            # r"""
            # (?P<provider>[^./]+)(\.|/|-)
            # (?P<local_symbol>[^./]+)(\.|/)
            # (?P<klass_name>[^./]+)(\.|/)
            # (?P<timeframe>\d+[smhd])(\.|/)
            # (?P<begin>
            # (?P<date1>
            # (?P<year1>\d{4})-?(?P<month1>\d{2})-?(?P<day1>\d{2})
            # )-?
            # (?P<time1>
            # (?P<hour1>\d{2}):?(?P<min1>\d{2}):?(?P<sec1>\d{2})(\.(?P<usec1>\d+))?
            # )
            # )
            # \.
            # (?P<end>
            # (?P<date2>
            # (?P<year2>\d{4})-?(?P<month2>\d{2})-?(?P<day2>\d{2})
            # )-?
            # (?P<time2>
            # (?P<hour2>\d{2}):?(?P<min2>\d{2}):?(?P<sec2>\d{2})(\.(?P<usec2>\d+))?
            # )
            # )
            # \.
            # (?P<cmp>[^.]+)
            # $
            # """,
            ## NT8-TWS bridge service
            ## NQM0.tick-price.20200605
            ## NQM0.tick-price.csv.20200605
            ## NQM0.tick-price.csv.20200605.xz
            ## NQM0.tick-mixed.csv.20200605.xz
            ## M6EM0.market-depth.csv.20200611.xz
            ## ESM0.historical-data.csv.20200611.xz
            # r"""
            # (?P<provider>[^./]+)(\.|/|-)
            # (?P<local_symbol>[^./]+)(\.|/|-)
            # (?P<handler>[^./]+)(\.|/|-)
            # ((?P<fmt>(csv))(\.|/|-))?
            # (?P<date1>(?P<year1>\d{4})-?(?P<month1>\d{2})-?(?P<day1>\d{2}))
            # ((\.|/)((?P<cmp>(xz))))?
            # $
            # """,
            ## ESM9.bar
            ## ESM9.bar.csv
            ## ESM9.bar.csv.xz
            # r"""
            # (?P<provider>[^./]+)(\.|/|-)
            # (?P<local_symbol>[^./]+)(\.|/)
            # (?P<klass_name>(bar))
            # ((\.|/)(?P<fmt>(csv)))?
            # ((\.|/)((?P<cmp>(xz))))?
            # $
            # """,
        )

    def _get_boundaries(self, query):
        query.setdefault("date2", query["date1"])  #: in missing case
        query.setdefault("time1", "000000")  #: in missing case
        query.setdefault("time2", "000000")  #: in missing case

        dt1 = "{date1}-{time1}".format_map(query)
        dt2 = "{date2}-{time2}".format_map(query)
        query.setdefault("key1", dt1)
        query.setdefault("key2", dt2)

        begin = parse_arrow(query["key1"])
        end = parse_arrow(query["key2"])
        return begin, end


# --- end ---


def test_candlestick():
    source = DemoTicksStream(10000, 100, 0.05, 0.05, quantum=0.20)
    for i, tick in enumerate(source):
        print(tick)
        if i >= 200:
            break

    # nq = CandlestickStream(source)
    # for i, bar in enumerate(nq):
    # print(bar)
    # if i >= 10:
    # break

    foo = 1


if __name__ == "__main__":
    test_candlestick()
