import os
import random
import re

import pandas as pd

import arrow
import pytest

from uswarm.tools import fileiter, soft
from uswarm.tools.configurations import load_config, process_config
from uswarm.tools.iterators import df_join, new_df

from uswarm.kurio.kurio import *
from uswarm.tools.files import IncrementalCSV
from uswarm.tools.dataframes import JOURNAL, MAIN, Dataframe, DateRepository

from uswarm.tools.testing import tmpfolder


# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger

log = logger(__name__)


def random_price(t=None, p=1000, mu=0.025, sigma=2, tick=0.25, delta=1):
    t = t or arrow.utcnow()
    t = t.floor("second")

    while True:
        p = p * (1 + (random.random() - 0.5) * mu / sigma)
        record = {
            "date": pd.Timestamp(t._datetime),
            "price": (p // tick) * tick,
            "volume": random.randint(0, 9),
        }
        yield record
        t = t.shift(seconds=delta)


def random_bar(t=None, p=11000, mu=0.025, sigma=2, tick=0.25, delta=1):
    t = t or arrow.utcnow()
    t = t.floor("second")

    while True:
        o = (p // tick) * tick
        h = o + random.randint(0, 10) * tick
        l = o - random.randint(0, 10) * tick
        p = p * (1 + (random.random() - 0.5) * mu / sigma)
        c = (p // tick) * tick

        record = {
            "date": pd.Timestamp(t._datetime),
            "open": o,
            "high": h,
            "low": l,
            "close": c,
            "volume": random.randint(0, 9),
        }
        yield record
        t = t.shift(seconds=delta)


class SBroker(Node):
    pass
