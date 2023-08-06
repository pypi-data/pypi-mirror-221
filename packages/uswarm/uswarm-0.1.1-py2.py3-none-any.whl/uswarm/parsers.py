import sys
import os

import arrow
from datetime import datetime
import dateutil
import dateutil.tz as tz
import dateutil.parser


os.environ["TZ"] = "Europe/Madrid"

TZ_CET = tz.gettz("Europe/Madrid")
TZ_CST = tz.gettz("US/Central")
TZ_EST = tz.gettz("America/Chicago")
TZ_GMT = tz.gettz("Etc/UCT")

TZ_DEFAULT = TZ_GMT


TZ_INFOS = {
    "CET": TZ_CET,
    "CST": TZ_CST,
    "EST": TZ_EST,
    "GMT": TZ_GMT,
}

TZ_DELTA = TZ_CET.utcoffset(datetime.now())

handlers = {
    str: None,
    bool: None,
    "date": None,
    "sdate": None,
    "csv": None,
    "utctimestamp": None,
    "timestamp": None,
    "tztimestamp": None,
}

MAX_FLOAT = sys.float_info.max


def dict_decode(types, fields, result=None):
    """Parse received fields using a types dict
    for storing (key, value) pairs in a dict.

    This method could be a function, but we put here
    just to enable overriding.
    """
    if result is None:
        result = {}
    try:
        for i, (key, t) in enumerate(types):
            # s = fields[i]
            s = fields.pop(0)
            # print(f"[{i}]: {key}: {t} <-- {s}")

            if key[0] == "_":
                continue  # ignore param that starts with '_'
            if t is str:
                if type(s) is bytes:
                    s = s.decode()
            elif t is int or t is float:
                s = t(s or 0)
            elif t is bool:
                s = s.lower()
                if s == b"false":
                    s = False
                elif s == b"true":
                    s = True
                else:
                    s = False if int(s or 0) == 0 else True
            elif t == "float":
                s = float(s)
                # fix max float -> 0
                if s == MAX_FLOAT:
                    s = 0
            elif t == "date":
                s = dateutil.parser.parse(s, tzinfos=TZ_INFOS)
                s = arrow.get(s)
            elif t == "sdate":
                s = datetime.strptime(s.decode(), "%Y%m") # b'202203' (contract_month)
                s = arrow.get(s)
            # elif t is 'Date':
            # s = parse(s.replace('  ', ' '))  # TWS weird format
            elif t == "utctimestamp":
                s = datetime.fromtimestamp(int(s), TZ_CET)
                s = arrow.get(s)
            elif t == "timestamp":
                s = datetime.fromtimestamp(int(s))
                s = arrow.get(s)
            elif t == "tztimestamp":
                s = datetime.fromtimestamp(int(s)) - TZ_DELTA
                s = arrow.get(s)
            elif t == "csv":
                s = s.decode().split(",")
                if len(s) > 0 and s[-1] == "":
                    s.pop()
            elif t == "dcsv":
                s = s.decode().split(",")
                if len(s) > 0 and s[-1] == "":
                    s.pop()
            elif t == "rth":
                # TODO: implement parsing of ...
                # [28]: trading_hours: <class 'str'> <-- 20210908:1700-20210909:1600;20210909:1700-20210910:1600;20210911:CLOSED;20210912:1700-20210913:1600;20210913:1700-20210914:1600;20210914:1700-20210915:1600
                # ['20210908:1700-20210909:1600',
                # '20210909:1700-20210910:1600',
                # '20210911:CLOSED',
                # '20210912:1700-20210913:1600',
                # '20210913:1700-20210914:1600',
                # '20210914:1700-20210915:1600']
                rth = []
                for rg in s.decode().split(";"):
                    rg = rg.split("-")
                    if len(rg) > 1:
                        # rth.append(
                        # tuple(
                        # [datetime.datetime.strptime(rg[0], '%Y%m%d:%H%M'),
                        # datetime.datetime.strptime(rg[1], '%Y%m%d:%H%M')]
                        # )
                        # )
                        rth.append(
                            [
                                arrow.get(datetime.strptime(rg[0], "%Y%m%d:%H%M")),
                                arrow.get(datetime.strptime(rg[1], "%Y%m%d:%H%M")),
                            ]
                        )

                s = rth
            elif isinstance(t, (tuple, list)):
                # repeat
                n = int(s or "")
                # t is the sequence
                # n the number of repetitions
                s = []
                for _ in range(n):
                    # print("-"*30)
                    r = dict_decode(list(t), fields)
                    s.append(r)
                    
            elif t == "lstr":
                if type(s) is bytes:
                    s = s.decode()            
                s = s.lower()
            else:
                s = t(s or 0)

            # print(f"[{i}]: {key}: {t} <-- {s}")
            result[key] = s

    except ValueError:
        print(f"field: '{key}' : Can not cast {s} to {t}")
        foo = 1
        # raise BadFormat(f"Can not cast {s} to {t}")

    except Exception as why:
        print(why)
        error(f"{why.__class__}: {why}")
        raise ()

    finally:
        return result


def parse_date(timestr):
    s = dateutil.parser.parse(timestr, tzinfos=TZ_INFOS)
    # s = arrow.get(s)
    return s


# End
