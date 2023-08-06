"""Convert some units"""
import re
from datetime import timedelta

import arrow

from datemath import dm
from . import TZ, parse_date

# -------------------------------------------
# Time Converters
# -------------------------------------------
_regexp_timeframe = re.compile(r"(?P<value>[\d]+)\s*(?P<unit>[A-z]+)?")
_timeframe_map = {
    "s": "seconds",
    "m": "minutes",
    "h": "hours",
    "d": "days",
    "w": "weeks",
    "y": "years",
}

_time_alias = {
    "secs": "s",
    "min": "m",
}
_time_fractions = [
    (31449600, "y"),
    (604800, "w"),
    (86400, "d"),
    (3600, "h"),
    (60, "m"),
    (1, "s"),
]

_higher_frame = {
    "s": "m",
    "m": "h",
    "h": "d",
    "w": "y",
}
_frame_values = {
    "s": (1, 5, 10, 15, 20, 30),
    "m": (1, 2, 5, 10, 15, 20, 30),
    "h": (1, 2, 4, 8),
    "d": (1, 2, 5),
    "w": (1, 2, 4),
}


def timeframe2delta(tf, klass=timedelta ,**kw):
    m = _regexp_timeframe.match(str(tf))
    if m:
        value, unit = m.groups()
        unit = unit or "s"
        kw = dict()
        kw[_timeframe_map[unit.lower()]] = int(value)
        return klass(**kw)
    raise RuntimeError(f"Unknown timeframe '{tf}'")


def neg_delta(delta):
    if isinstance(delta, dict):
        return delta.__class__({k: -v for k, v in delta.items()})
    return -delta


def delta2timeframe(delta, fmt=str, short=True):
    seconds = delta.total_seconds()
    if seconds < 0:
        delta = -delta
        seconds = -seconds

    units = dict()
    for value, key in _time_fractions:
        units[key] = 0
        while seconds >= value:
            seconds -= value
            units[key] += 1

    if short:
        for k, v in list(units.items()):
            if not v:
                units.pop(k)

    if fmt in (str,):
        units = ", ".join([f"{units[k]}{k}" for _, k in _time_fractions if k in units])

    return units


def delta2time(tf):
    m = _regexp_timeframe.match(tf)
    if m:
        value, unit = m.groups()
        kw = dict()
        kw[_timeframe_map[unit.lower()]] = int(value)
        return timedelta(**kw)
    raise RuntimeError(f"Unknown timeframe {tf}")


def normalize_lapse(lapse):
    m = re.match(r"(?P<value>\d+)\s*(?P<unit>.*?)$", lapse)
    if m:
        value, unit = m.groups()
        unit = unit.lower().strip()
        unit = _time_alias.get(unit, unit)
        for k, v in _timeframe_map.items():
            if re.match(unit, v):
                return f"{value}{k}"
    return lapse


def to_seconds(lapse):
    "16s, 3min, etc"
    lapse = normalize_lapse(lapse)
    m = re.match(r"(?P<value>\d+)\s*(?P<unit>.*?)$", lapse)
    if m:
        value, unit = m.groups()
        for v, k in _time_fractions:
            if k == unit:
                return v * int(value)
    print(f"UKNOWN lapse: {lapse}")


# ------------------------------------------------
# Arrow datetime
# ------------------------------------------------
parser = arrow.parser.DateTimeParser()


def parse_arrow(string):
    dt = parse_date(string)
    return arrow.Arrow.fromdatetime(dt)  # , tzinfo=TZ)
