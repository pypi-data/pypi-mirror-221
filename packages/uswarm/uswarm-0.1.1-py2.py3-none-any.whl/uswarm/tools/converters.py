from ..tools import TZ

# -----------------------------------------------------------
# Misc converters handling
# -----------------------------------------------------------
def to_camel(exp):
    if isinstance(
        exp,
        (
            tuple,
            list,
        ),
    ):
        return exp.__class__([to_camel(k) for k in exp])
    if isinstance(exp, str):
        return " ".join([t[0].upper() + t[1:] for t in exp.split()])


def Str(item):
    "Extended String converter"
    if isinstance(item, bytes):
        return item.decode("UTF-8")
    return str(item)


def Float(item):
    "Extended Float converter"
    return float(item or 0)


def Int(item):
    "Extended Int converter. Valid is number can be converted to INT without loosing precission"
    f = float(item or 0)
    i = int(f)
    if i == f:
        return i
    raise ValueError()


def Date(item, tz=TZ):
    return parser.parse(item, ignoretz=True)


# ----------------------
# Encoders
# ----------------------
def item_normal(item):
    return f"{item}"


def date_normal(item):
    return item.strftime("%Y%m%d-%H%M%S")


def date_with_miliseconds(item):
    return item.strftime("%Y%m%d-%H%M%S.%f")


def date_2_string(q, fmt="%Y%m%d %H:%M:%S", tzd=None):
    r = q.__class__()
    for k, v in q.items():
        if isinstance(v, datetime):
            if tzd:
                v = v - tzd  # + timedelta(seconds=1)
            v = v.strftime(fmt)
        r[k] = v
    return r

def short_float(item):
    return f"{item:.2f}"