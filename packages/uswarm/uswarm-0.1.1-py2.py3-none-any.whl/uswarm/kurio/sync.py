"""
Define the interface class for Synchornization and Workflow pipelines.
"""

import random

import arrow
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from datetime import timedelta
from typing import List, Set, Dict, Tuple, Optional, Union
from abc import abstractmethod

from curio.meta import awaitable, asyncioable

from ..tools import soft
from ..tools.dataframes import (
    Dataframe,
    iRepository,
    iDateBoundary,
    iFolderRepository,
    DateRepository,
)
from ..tools.fractal import Fractal
from ..tools.files import iRecordStorage
from ..tools.financial import GBM, xcals
from ..tools.iterators import edge
from ..tools.pubsub import iPersistentProcessor, awaitable

from .resource import iResource


# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger

log = logger(__name__)

# --------------------------------------------------
# iSync
# --------------------------------------------------

Delta = pd.DataFrame
Record = dict
Completed = pd.DataFrame


# --------------------------------------------------
# iSync interface
# --------------------------------------------------


class iSync(iPersistentProcessor, iResource):
    """
    Extends iPersistentProcessor interface for:

    - supporting the consolidation of multiples source streams at the same time.
    - replay(since) capabilities.



    # TODO: review documentation.



    This class implements the iSync interface for creating workflow pipelines
    by connecting *nodes* that performs a task, compute a result and pass the result
    to the *subcriptors* nodes to continue processing.

    By other hand, the iSync interface provides a way to re-synchronize workflows when
    a pipeline has been interrupted for any reason.

    This feature is archived by saving all computed values by a node in a DataFrame
    prepository and providing some synchronization method to restart the result-data flows
    from the interrupted point.

    The concept can be viewed a *waves* of information that travel from one point to another
    accross the whole pipeline ecosystem where intermediate results are stored in DataFrames
    when is convenient.

    A *wave* consists in combination of deltas comming from different sources at a time.
    Each delta represents a portion of contiguous key-data.

    Eash iSync node may have multiple input sources which feed the node with different parts
    of information at time, organized by the wave-keys.

    When a contuguos block of information is complete building a *delta*, the node will dispatch
    tihs *delta* to the processor function, save the results obtained in the repository and
    forwards the results to the listening nodes.

    This allows us to easily resume an interrupted pipeline execution or add new dataflows
    connecting another tree structure of working nodes (aka an *algorithm*) in particular point
    in the whole pipeline ecosystem.

    This new *algo* will start to work using stored data since a particular moment (the starting
    *edge*) while the rest of pipelines work normally. Sooner or later this process will consume
    all the *historical* data available reaching the current (*live*) state.

    This allows us to add *new functionality* to the whole system without having to interrupt
    any other running activities.

    As a goal design, we want iSync to be fast procesing bunch of data (*deltas*) rather
    procesing individual events such *records*, as we want fast procesing when we start a new
    pipeline-algorithm connected to the ecosystem (ie. montecarlos simulations, etc). That's
    means iSync is oriented to push *deltas* instead of *records*. For dealing with records
    we provide some sugar methods that handle records and deltas under the hood.

    In summary, the concepts are:

    - node as a worker processing *waves* of data.t
    - node delegates store processed results in dataframes repositories.
    - nodes can connect each other building pipelnes.
    - nodes can request *historical* processed data to its node *parents*
      and stay *sync* with live future data.


    Notes on when data are *triggered*

    Nodes far from external sources received data only when the last external wave
    propagates until reach these nodes. That means algorithms connected to last nodes
    will not react until the conditions for data goes so far are acomplished, maybe later
    for some aplications.

    Propagate *incompleted* waves across all pipeline ecosystem is a waste of resources, so
    the proposed solution is to connect a *higher* frequency node to these frames in order to
    *wakeup* the last node with a *fresh* data and take a decission with a higher frequency.


    ----------------------------------------------------------------

    Implements:

    - Create *subcriptors* flows.
    - Provide a *push* method to send data forwards to subscriptors.
    - Provide a *sync* method for getting missing data.
    - sender node will continue to send data forwards until no more fresh data is available.

    Assumptions:

    - Does not make any assumption about grid size or gaps from source node.
    - Assume wkeys are monotonic crescend.
    - data flows are send in order.

    Pending:

    - [ ] FWD data only when data are consolidated of allow subcriptors to receive
          data while are assembling


    Review:

    - [ ] iSync open the door to synchronized repositories.
    - [ ] Information flows in waves that share same key (wkey)
    - [ ] wkey is monotonal and an be predicted what is the next one from a particular one.
    - [ ] wave-parta data is assembled and yieled in order as 'next-key' is completed.
    - [ ] other wave-parts are waiting to be completed and fired in the right moment.
    - [ ] information is dispatched in *deltas*, grouping one or more cotiguous wkeys building a bunch of orderd records.
    - [ ] this way some processing algos can be used vectorial capabilities (i.e pandas, etc)
    - [ ] every iSync node has one or more *parents* that feed data into self.
    - [ ] *edge* is the flow advance border for a node.
    - [ ] iSync node can request data flow from a parcitular *edge* in the past.
    - [ ] when a single or bunch of data is ready is dispatched by node.
    - [ ] node does not store incoming data, just processed one.
    - [ ] a node can be linked from other nodes creating several pipelines.
    - [ ] when a link is up-to-date (synchronized) node send the processed deltas directly to them (low-latency)
    - [ ] node *edge* is moved forward only when processed data is stored.
    - [ ] moving *edge* implies cleaning the source wdata that is had just processed.

    Coding:

    - [x] Monotonal wkey sequence creation (for bunch-of-deltas).
    - [x] next-key concept.
    - [x] key clustering / boundary concept.
    - [x] grid-size concept for keys.
    - [x] smap-to-grid concept for wkeys.
    - [x] wkey -> ikey mapping: ikey is a long interget (10**18)
    - [x] internal and human representation of wkey (i.e. dates and sequence-integer)

    - [x] monitor for detecting *edge* gaps or temporal storage overflows.
    - [x] temporal store for wave-partial data waiting to be assembled.
    - [x] dispatching function (vectorial deltas)
    - [x] parents and children nodes to make the data flows through pipelines.
    - [x] processd(delta) is forwarded to children nodes.
    - [x] processed(delta) is saved from time to time moving *edge* border and cleaning input.
    - [ ] get_from(since) feature for requesting data to parents.
    - [x] ikeys are used as internal keys for clustering and storage.
    - [x] wkeys are used as human-algorithm representation of *edge*

    """

    def __init__(
        self,
        inputs=None,
        edge=None,
        # index_name="key",
        min_dispath=10,
        max_dispath=100,
        *args,
        **kw,
    ):

        super().__init__(*args, **kw)

        # record attributes
        self.inputs: List[str] = inputs or []

        # building deltas for processing
        self._edge = edge  #: workflow border edge
        self.min_dispath: int = int(min_dispath)
        self.max_dispatch: int = int(max_dispath)

        # self._inbox = pd.DataFrame(columns=inputs, index=[edge])
        # self._inbox.index.name = index_name
        self._inbox: pd.DataFrame = None

    # --------------------------------------------------
    # Waves
    # --------------------------------------------------
    def _analyze(self, data, src: str = "0", *args, **kw):
        """Try to add wpart partial wave to the inbox and get a wdelta when
        data are ready to be processed.

        The partial waves are stored in memory, not in persistent storage.
        If the process is stopped for any reason, received partial waves will be
        discarded and sync(since) will be used.
        """
        assert isinstance(data, Delta)
        if self._inbox is None:
            self._inbox = pd.DataFrame(
                columns=self.inputs,
            )
            self._inbox.index.name = data.index.name
        self._inbox = self._inbox.combine_first(data)

        # check if edge is completed.
        row0 = self._inbox.iloc[0]
        if not row0.hasnans:
            # assert row0.name == self._edge
            # check how big is the *ready* incoming delta
            mask = self._inbox.isnull().any(axis=1)
            # get where the 1st complete (ready) row
            ready = np.nanargmax(mask)
            if ready == 0 and mask.shape[0] > 0:

                # Get the size of the ready delta ...
                ready = mask.shape[0]

            while ready >= self.min_dispath:
                # inbox has fulfilled a delta starting from the 1st
                # pending row. Now we can submit this delta checking
                # the used size preferences (min_dispath, max_dispatch)

                idx = min(ready, self.max_dispatch)
                # cut the wave from inbox
                wave = self._inbox[:idx]
                self._inbox = self._inbox[idx:]
                # TODO: review
                # update the edge in order to avoid GAPS.
                # idx0 = wave.index[-1]
                # idx1 = wave.index[-2]
                # self._step = self._step or (idx0 - idx1)
                # self._edge = idx0 + self._step  # TODO: review GAPS
                yield wave
                ready -= idx

            foo = 1
        #
        # b = self._inbox.update(wdelta, overwrite=False)
        foo = 1

    @awaitable(_analyze)
    async def _analyze(self, data, src: str = "0", *args, **kw):
        """handle result locally (is any).
        do nothing by default.
        """
        return self._analyze._syncfunc(self, data, src, *args, **kw)

    # --------------------------------------------------
    # Request Synchronization from paren nodes
    # --------------------------------------------------
    @abstractmethod
    def _replay(self, since):
        """
        TODO: implement

        """
        pass




TIME_TYPE = Union[arrow.Arrow, pd.Timestamp]


class iTimeSync(iSync):
    """Implements time-waved iSync."""

    def __init__(self, *args, **kw):
        soft(kw, cluster_size=24 * 3600, index_name="date")
        super().__init__(*args, **kw)


class iCandleStick(iTimeSync):
    """condense data into fixed-time based bars."""

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    # --------------------------------------------------
    # Data procesing
    # --------------------------------------------------
    def _process(self, wdelta):
        """Process a fresh new delta.
        - vectorial (whenever is possible) function (i.e pandas, etc).
        """
        data = {
            "open": wdelta.iloc[0]["open"],
            "high": wdelta["high"].max(),
            "low": wdelta["low"].min(),
            "close": wdelta.iloc[-1]["close"],
            "volume": wdelta["volume"].sum(),
        }
        bar = pd.DataFrame(data, index=wdelta.index[-1:])

        # log.debug(f"Condensed: [{self.max_dispatch}]: {wdelta.index[-1]}: {data}")
        return bar

    @awaitable(_process)
    async def _process(self, wdelta):
        """Process incoming message"""
        # curio trick
        return self._process._syncfunc(self, wdelta)


class iDevice(iSync):
    pass


class Candlestick(iCandleStick):
    def __init__(self, *args, **kw):
        # kw.setdefault("cluster_size", 24 * 3600)
        # kw.setdefault("index_name", "date")
        super().__init__(*args, **kw)


class WDeltaGenerator:
    """A demo class for generating Synthetic streaming deltas."""

    def __init__(
        self,
        t0=None,
        s0=1000,
        mu=0.5 / 200,
        sigma=0.05 / 200,
        quamtum=0.25,
        exchange: Union[str, xcals.ExchangeCalendar] = "Atlas",
        gaps=3600,  # number of auto-generated bars to simulate a GAP
        depth=6,
        grid="1s",
        *args,
        **kw,
    ):
        # super().__init__(self, *args, **kw)
        # dt and offset in case of resuming a prevoius streaming
        self.dt = pd.to_timedelta(grid)

        # exchange calendar
        if isinstance(exchange, str):
            exchange = xcals.get_calendar(exchange)
            xcals.register_calendar
            # exchange = mcal.get_calendar(exchange)

        # assert isinstance(exchange, xcals.ExchangeCalendar)
        # assert isinstance(exchange, mcal.MarketCalendar)

        self.exchange = exchange
        self.gaps = gaps
        self._calendar = None

        # calc starting point
        if t0 is None:
            t0 = arrow.utcnow().floor("seconds").shift(days=-1)
        else:
            t0 = arrow.get(t0)
            t0 = t0 + self.dt

        t0 = pd.to_datetime(t0._datetime)
        self.t0 = t0

        # price settings
        self.s0 = s0
        self.mu = mu
        self.sigma = sigma
        self.quantum = quamtum

        # vix settings
        self.vix_s0 = self.s0
        self.vix_mu = self.mu
        self.vix_sigma = self.sigma

        # fractal settings
        self.depth = depth
        self.grid = grid

        # in-advance data generation
        self._pregen = {}

        def gbm_price():
            # same generator but used in 2 forms
            stream = GBM(self.s0, self.mu, self.sigma, quantum=self.quantum)
            for p in stream:
                yield p

        def fractal_price(t0, dt):
            # same generator but used in 2 forms
            frac = Fractal(**self.__dict__)
            start = t0, self.s0
            while True:
                end = (
                    start[0] + timedelta(days=1),
                    start[1]
                    * (1 - 0.5 * random.random() * 0.20)
                    // self.quantum
                    * self.quantum,
                )
                A = frac.generate(start, end)
                # A.columns =['open']
                A = A // self.quantum * self.quantum
                for t0, row in A.iterrows():
                    yield row
                start = end

        def volume(dt):
            size = int(dt.total_seconds() * 15)
            while True:
                v = random.randint(0, size)
                yield v

        def vix(dt):
            size = dt.total_seconds()
            f = 0.0002 * size
            stream = GBM(self.vix_s0, self.vix_mu, self.vix_sigma)
            for i, p in enumerate(stream):
                yield p * f

        def gbm_bar(t0, dt):
            "no gaps"
            bb0 = gbm_price()
            vol = volume(dt)
            vx = vix(dt)

            # get bar-open
            for op in bb0:
                break

            ctx = {}
            gen = edge(ctx, bb0, vol, vx)

            for cl, v, x in gen:
                h = op + random.random() * x // self.quantum
                l = op - random.random() * x // self.quantum
                h = max(h, cl)
                l = min(l, cl)
                yield t0, op, h, l, cl, v

                # move to next bar
                t1 = t0 + dt
                if t1 in self._calendar:
                    # no GAP
                    t0 = t1
                    op = cl
                else:
                    # and generate a GAP jumping 'gaps' times.
                    self._generate_calendar(t0)
                    # move to next valid date
                    t0 = self.exchange.next_minute(t0)

                    if self.gaps > 0:
                        n = random.randint(1, self.gaps)
                        for i, op in enumerate(bb0):
                            if i >= n:
                                break

        def fractal_bar(t0, dt):
            "no gaps"
            to = t0.to_numpy()
            bb0 = fractal_price(t0, dt)
            vol = volume(dt)
            vx = vix(dt)

            # get bar-open
            for op in bb0:
                break

            ctx = {}
            gen = edge(ctx, bb0, vol, vx)

            for cl, v, x in gen:
                h = op + random.random() * x // self.quantum
                l = op - random.random() * x // self.quantum
                h = cl if cl.max() > h.max() else h
                l = cl if cl.min() < l.min() else l

                yield [op.name, *op.values, *h.values, *l.values, *cl.values, v]

                # move to next bar
                t1 = t0 + dt
                if t1 in self._calendar:
                    # no GAP
                    t0 = t1
                    op = cl
                else:
                    # and generate a GAP jumping 'gaps' times.
                    self._generate_calendar(t0)
                    # move to next valid date
                    t0 = self.exchange.next_minute(t0)

                    if self.gaps > 0:
                        n = random.randint(1, self.gaps)
                        for i, op in enumerate(bb0):
                            if i >= n:
                                break

        self.generators = {
            "price": fractal_price(self.t0, self.dt),
            "volume": volume(self.dt),
            "vix": vix(self.dt),
            "bar": fractal_bar(self.t0, self.dt),
        }

        self._generate_calendar(self.t0)

    def _generate_calendar(self, t0):
        start = arrow.get(t0).floor("days").strftime("%Y-%m-%d")
        start = pd.to_datetime(start)

        while not self.exchange.is_session(start):
            start = start - timedelta(days=-1)

        end = self.exchange.next_session(start)
        # end = start
        period = f"{self.dt.total_seconds()}s"
        self._calendar = self.exchange.trading_index(
            start=start, end=end, period=period, intervals=False
        )
        assert t0 in self._calendar

    def wdelta(self, src, index=["date"], columns=None, n=None):
        # get the max-edge for retrieving data
        if "date" in index:
            edge = pd.to_datetime(arrow.utcnow()._datetime, utc=True).to_numpy()
        else:
            edge = None

        df = self._pregen.pop(src, None)
        if df is None:
            gen = self.generators[src]
            n = n or random.randint(3, 5000)

            data = []
            for record in gen:
                data.append(record)
                if len(data) >= n:
                    break

            columns = columns or [*index, src]

            df = pd.DataFrame(data, columns=columns)
            df.set_index("date", inplace=True)

        if edge is None:
            return df
        else:
            mask = df.index <= edge
            result = df[mask]
            pregen = df[~mask]
            if pregen.shape[0] > 0:
                self._pregen[src] = pregen
            return result


# End
