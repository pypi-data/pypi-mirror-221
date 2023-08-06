import random

from collections import namedtuple
from dataclasses import dataclass

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

from arrow import Arrow


def sign(x):
    return -1 if x < 0 else 1


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


# ----------------------------------------------------------
# Price Stream
# ----------------------------------------------------------

# tick types taken from IB
BID_SIZE = 0
BID_PRICE = 1
ASK_PRICE = 2
ASK_SIZE = 3
VOLUME = 8
TIME = 45

tick_types = {
    #  https://interactivebrokers.github.io/tws-api/tick_types.html
    0: "Bid-Size",
    1: "Bid-Price",
    2: "Ask-Price",
    3: "Ask-Size",
    4: "Last-Price",
    5: "Last-Size",
    6: "High",
    7: "Low",
    8: "Volume",
    9: "Close-Price",
    14: "Open-Tick",
}


class SourceStream:
    """The base of any price stream."""

    def __init__(self):
        self.running = False

    def __iter__(self):
        self.running = True
        return self._stream()

    def _stream(self):
        raise NotImplementedError()


class TicksStream(SourceStream):
    """Ticks Stream inspired in IB ticks stream."""


class DepthStream(SourceStream):
    """Depth Of Market stream.
    Note that may not be compatible with other streams.
    """

    pass


@dataclass
class Transaction:
    sender: str
    receiver: str
    date: str
    amount: float = None


@dataclass
class Tick:
    # __slots__ = ["type", "value", "size", "mask"]
    type: int
    value: float
    size: int = 0
    mask: int = 0


@dataclass
class Bar:
    # __slots__ = ["t1", "open", "high", "low", "close", "volume", "t0"]
    t1: float
    open: float
    high: float
    low: float
    close: float
    volume: float
    t0: float = 0

    # def __init__(self, t0, o=0, h=0, l=0, c=0, v=0, t1=None):
    # self.t0 = t0
    # self.t1 = t1 or t0

    # self.open = o
    # self.high = h or o
    # self.low = l or o
    # self.close = c or o
    # self.volume = v

    def update(self, date, price, volume):
        assert date > self.date
        self.date = date
        self.high = max(self.high, price)
        self.low = min(self.low, price)
        self.close = price
        self.volume += volume


class BarStream(SourceStream):
    def __init__(self, source):
        self.bar = None  #: WIP condensed data
        self.threshold = None  #: threshold/cummulative data

        self.source = source  #: "flow" chain
        self._source = None  #: generator from source

    def _datapoint(self, data):
        for k, v0 in data.items():
            if k in ("volume",):
                v1 = self.bar.__dict__[k] + v0
            else:
                v1 = v0
            if v1 > self.threshold[k]:
                # new bar must be generated
                pass
            else:
                self.bar.__dict__[k] = v1


    def _new_bar(self, price, t0):
        self.bar = Bar(t0, price, price, price, price, 0, t0)
        # TODO: set threshold
        return self.bar

    def _bar_completed(self):
        """Generic Threshold criteria for generating a new bar.
        Data is updating / accumulating until a Threshold is
        reached.

        Then a new bar is generated with the remain *data*
        still not used. (i.e. Atlas bars)
        -

        """
        pass


class BarStreamBars(BarStream):
    """Generate Bars from TickStream."""

    def __init__(self, source):
        super().__init__(source)

    def _handshaking(self, required=None):
        """Bar sources types has the same structure, so
        we don't need anything else than 1st (mini) bar to
        finish the handshaking."""
        self._source = iter(self.source)
        bar1st = next(self._source)
        return bar1st

    def _stream(self):
        # 1st we need to get the minial required data
        # from stream: date, price
        # using a 'handshaking' method that collect them all
        bar1st = self._handshaking([BID_PRICE, TIME])

        # now we can "condense" stream into bars
        count = 0
        bar = self._new_bar(price, t0)
        for bar in self._source:  # use same iterator instance
            # try to split big bars into many small ones
            # spliting the volume based on range and elapsed time.
            # GAP is also considered
            # self.bar vs bar

            # print(f"{count}: {tick}: {bar}")
            if tick.type == BID_PRICE:
                bar.close = tick.value
                bar.low = min(bar.low, bar.close)
            elif tick.type == ASK_PRICE:
                bar.close = tick.value
                bar.high = max(bar.high, bar.close)
            elif tick.type == VOLUME:
                bar.volume += tick.value
            elif tick.type == TIME:
                bar.t1 = tick.value
                # if random.random() < 0.01:
                # print(self.bar)
                # foo = 1

            if bar.volume > 0 and self._bar_completed():
                print(f"[{count:5}]: e: {bar.t1-bar.t0:4} secs :{bar}")
                yield bar
                bar = self._new_bar(bar.close, bar.t1)
                count = 0
            else:
                count += 1

            if not self.running:
                break


class BarStreamTicks(BarStream):
    """Generate Bars from TickStream."""

    def _handshaking(self, required):
        required = set(required)
        data = {}

        self._source = iter(self.source)
        for i, tick in enumerate(self._source):
            data[tick.type] = tick.value
            if not required.difference(data):
                break
            if i > 200:
                raise RuntimeError("can not get initial data from input tick stream")
            if not self.running:
                # abort prematurely
                break
        return data

    def _new_bar(self, price, t0):
        self.bar = Bar(t0, price, price, price, price, 0, t0)
        return self.bar

    def _stream(self):
        # 1st we need to get the minial required data
        # from stream: date, price
        # using a 'handshaking' method that collect them all
        data = self._handshaking([BID_PRICE, TIME])

        # now we can "condense" stream into bars
        price = data[BID_PRICE]
        t0 = data[TIME]
        count = 0
        bar = self._new_bar(price, t0)
        for tick in self._source:  # use same iterator instance
            # print(f"{count}: {tick}: {bar}")
            if tick.type == BID_PRICE:
                bar.close = tick.value
                bar.low = min(bar.low, bar.close)
            elif tick.type == ASK_PRICE:
                bar.close = tick.value
                bar.high = max(bar.high, bar.close)
            elif tick.type == VOLUME:
                bar.volume += tick.value
            elif tick.type == TIME:
                bar.t1 = tick.value
                # if random.random() < 0.01:
                # print(self.bar)
                # foo = 1

            if bar.volume > 0 and self._bar_completed():
                print(f"[{count:5}]: e: {bar.t1-bar.t0:4} secs :{bar}")
                yield bar
                bar = self._new_bar(bar.close, bar.t1)
                count = 0
            else:
                count += 1

            if not self.running:
                break

    def _bar_completed(self):
        raise NotImplementedError()


class CandlestickStream(BarStreamTicks):
    def __init__(self, source, timeframe="1s"):
        super().__init__(source)
        self.timeframe = timeframe
        self.delta = timeframe2delta(timeframe).total_seconds()
        self.t1 = 0  # . limit for a new bar to be created

    def _new_bar(self, price, t0):
        self.t1 = t0 + self.delta
        return super()._new_bar(price, t0)

    def _bar_completed(self):
        # this is the condition for a new bar to be generated.
        return self.bar.t1 >= self.t1


class AtlasBarStream_Ticks(BarStreamTicks):
    """Atlas bars takes ticks stream or any other BarStream."""

    def __init__(self, source, size=10):
        super().__init__(source)

        # TODO: detect type of source: Ticks or Bars
        # use always BarStream
        # create a temporary 1s BarStream if source are ticks
        self.size = size
        self.size2 = size / 2
        self.high = 0
        self.low = 0
        self.high2 = 0
        self.low2 = 0

    def _new_bar(self, price, t0):
        if self.bar:
            if price > self.high:
                self.low2 = self.low
                self.low = self.high
                self.high = self.high2
                self.high2 += self.size
            else:
                self.high2 = self.high
                self.high = self.low
                self.low = self.low2
                self.low2 -= self.size
        else:
            rnk = int(price / self.size)
            self.low = (rnk - 1) * self.size
            self.high = (rnk + 1) * self.size
            self.low2 = self.low - self.size
            self.high2 = self.high + self.size

        return super()._new_bar(price, t0)

    def _bar_completed(self):
        # this is the condition for a new bar to be generated.
        return self.bar.low < self.low2 or self.bar.high > self.high2


# ----------------------------------------------------------
# Price Stream Generation
# ----------------------------------------------------------
# TODO: simulate Ticks and Depth streams
class DemoTicksStream(TicksStream):
    def __init__(self, base, s0, mu, sigma, quantum=None, timeframe="1s", t0=None):
        super().__init__()

        self.generator = create_GBM(base, s0, mu, sigma, quantum)
        self.price = base  #: last price
        t0 = t0 or Arrow.utcnow()  # TODO: from datetime.timestamp as well
        self.t0 = int(t0.timestamp())
        self.delta = timeframe2delta(timeframe).total_seconds()
        self.acc_volume = 0

    def _stream(self):
        delta = self.delta
        last_operation = self.generator()
        flush_vol = 0
        send_vol = False

        while self.running:
            # Tick price BID/ASK
            price = self.generator()
            placement = random.randint(1, 10)
            if random.random() < 0.5:
                yield Tick(BID_PRICE, price)
                yield Tick(BID_SIZE, placement)
                if last_operation < price:
                    self.acc_volume += placement
                    last_operation = price
                    flush_vol += placement
                    send_vol = True
            else:
                yield Tick(ASK_PRICE, price)
                yield Tick(ASK_SIZE, placement)
                if last_operation > price:
                    self.acc_volume += placement
                    last_operation = price
                    flush_vol += placement
                    send_vol = True

            # Tick Time
            # print(f"-- {flush_vol}")
            if send_vol or (flush_vol > 0 and random.random() < 0.05):
                # TODO: publish VOL from opening day (self.volume)
                yield Tick(VOLUME, flush_vol)
                flush_vol = 0
                send_vol = False

            # Tick Time
            if random.random() < 0.3:
                self.t0 += delta
                yield Tick(TIME, self.t0)


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
