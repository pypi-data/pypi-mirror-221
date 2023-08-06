import re
from datetime import datetime, timedelta

# -------------------------------------------
# Time helpers
# -------------------------------------------
_regexp_timeframe = re.compile(r'(?P<value>\d+)\s*(?P<unit>[A-z]+)')
_timeframe_map = {
    's': 'seconds',
    'm': 'minutes',
    'h': 'hours',
    'd': 'days',
    'w': 'weeks',
    'y': 'years',
}

_time_fractions = [
    (31449600, 'y'),
    (604800, 'w'),
    (86400, 'd'),
    (3600, 'h'),
    (60, 'm'),
    (1, 's'),
]

_higher_frame = {
    's' : 'm',
    'm' : 'h',
    'h' : 'd',
    'w' : 'y',
}
_frame_values = {
    's' : (1, 5, 10, 15, 20, 30),
    'm' : (1, 2, 5, 10, 15, 20, 30),
    'h' : (1, 2, 4, 8),
    'd' : (1, 2, 5),
    'w' : (1, 2, 4),
}

class Discrete():
    values = {}
    ranges = []

    def __init__(self, **kw):
        self.digits = kw

    def inc(self, **kw):
        pass

    def dec(self):
        pass



class TimeFrame(timedelta, Discrete):
    """A timeframe utility class for TWS"""

    def up(self, value=1, unit=0):
        """Returns an upper level timeframe.

        1 -> 5 -> 10 -> 20 -> 30 -> (next unit)

        s -> m -> h -> d -> w
        """
        tf = delta2timeframe(self, fmt=None, short=False)
        for v, u in _time_fractions:
            if tf[u] != 0:
                break

        if unit:
            for _ in range(unit):
                u = _higher_frame[u]
                if value > 0:
                    v = value
                else:
                    v = _frame_values[u][0]
            else:
                pass

        while value > 0:
            # locate where is now
            tmp = list(_frame_values[u])
            for i, x in enumerate(tmp):
                if v <= x:
                    value -= 1
                    break
            else:
                u = _higher_frame[u]

            # move fwd
            if value < len(tmp):
                v = tmp[value]
            else:
                u = _higher_frame[u]
                v = _frame_values[u][0]


        foo =1



def tws_historical_duration(tf):
    """Compute the best duration for historical
    bars download in TWS.

    Limits:
    - not all timeframes are available
    - max of 2000 bars can be requested

    """
    delta = timeframe2delta(tf)



def timeframe2delta(tf):
    m = _regexp_timeframe.match(tf)
    if m:
        value, unit = m.groups()
        kw = dict()
        kw[_timeframe_map[unit.lower()]] = int(value)
        return timedelta(**kw)
    raise RuntimeError(f"Unknown timeframe {tf}")


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

    if fmt in (str, ):
        units = ', '.join([f'{units[k]}{k}' for _, k in _time_fractions if k in units])

    return units


def delta2time(tf):
    m = _regexp_timeframe.match(tf)
    if m:
        value, unit = m.groups()
        kw = dict()
        kw[_timeframe_map[unit.lower()]] = int(value)
        return timedelta(**kw)
    raise RuntimeError(f"Unknown timeframe {tf}")


def short_keys(d, key):
    """Sort the dictionary keys by element"""
    result = list(d.keys())
    result.sort(key=lambda x: d[x][key])
    return result


def tranlate_bar_size(bar_size):
    m = re.match(r'(?P<value>\d+)\s*(?P<unit>.*?)$', bar_size)
    if m:
        value, unit = m.groups()
        for k, v in _timeframe_map.items():
            if re.match(unit, v):
                return f"{value}{k}"

# -------------------------------------------
# Time helpers
# -------------------------------------------

tick_types = {
    #  https://interactivebrokers.github.io/tws-api/tick_types.html
    0: 'Bid-Size',
    1: 'Bid-Price',
    2: 'Ask-Price',
    3: 'Ask-Size',
    4: 'Last-Price',
    5: 'Last-Size',
    6: 'High',
    7: 'Low',
    8: 'Volume',
    9: 'Close-Price',
    14: 'Open-Tick',
    45: 'Time',
    49: 'Halt-Status',
}


# -------------------------------------------
# Future Contracts
# -------------------------------------------
month2exp = {
    1: 'F',
    2: 'G',
    3: 'H',
    4: 'J',
    5: 'K',
    6: 'M',
    7: 'N',
    8: 'Q',
    9: 'U',
    10: 'V',
    11: 'X',
    12: 'Z',
}
"Future expiration dates"

exp2month = dict([(z, m) for m, z in month2exp.items()])
"Expiration 2 Month map"

def futsplit(local_symbol):
    exp = ''.join(month2exp.values())
    pattern = r'(?P<master>\w+)(?P<exp>[' + exp + ']\d)$'
    m = re.match(pattern, local_symbol)
    if m:
        return m.groupdict()
    return {}