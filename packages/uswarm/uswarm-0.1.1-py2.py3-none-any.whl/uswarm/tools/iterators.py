"""Extended Iterators

"""
import re
from collections import deque
from inspect import isgeneratorfunction
from itertools import product, cycle, islice, chain, permutations

import pandas as pd

from uswarm.tools import zip_like

# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger, log_container

log = logger(__name__)


identity = lambda x: x


reg_ip_ranges = r"""(?ismux)
(?P<s1>\d+)\.(?P<s2>\d+)\.(?P<s3>\d+)\.(?P<s4>\d+)
\s*-\s*
(?P<e1>\d+)\.(?P<e2>\d+)\.(?P<e3>\d+)\.(?P<e4>\d+)
"""

DIGIT = r"(\d+)"


def split_edge(text, regexp=DIGIT):
    """Analize and Split a text searching for
    valid items and separators using a regexp.

    returns: itms and render pattern for later expansion.
    """
    items = []
    pattern = ""
    for token in re.split(regexp, text):
        m = re.match(regexp, token)
        if m:
            items.append(int(m.group(0)))
            pattern += "{}"
        else:
            pattern += token

    return items, pattern


def ident(x):
    return x


def expand_range(text, convert=str):
    """Detect a-b range expression and generate all
    the range expansion or just return the same text
    otherwise.
    """
    if isinstance(text, (list, tuple, set, dict)):
        for item in text:
            yield from expand_range(item, convert)
        return
    if isinstance(text, str):
        # is any range expansion?
        m = re.match(r"(?P<a>[^\s-]+)\s*-\s*(?P<b>.*)", text)
        if m:
            a, b = m.groups()
            # extract 'digits' and create render 'pattern'

            # ['', '10', '.', '1', '.', '2', '.', '100', '']
            da, pa = split_edge(a)
            db, pb = split_edge(b)
            if pa == pb and len(da) == len(db):
                iters = []
                for i, start in enumerate(da):
                    end = db[i]
                    iters.append(range(int(start), int(end) + 1))

                for seq in product(*iters):
                    value = pa.format(*seq)
                    yield convert(value)
                return

    yield convert(text)


# -------------------------------------
# General Iterators
# -------------------------------------
def cpermutations(iterable):
    """
    >>> iterable = "ABC"
    >>> list(cpermutations(iterable))
    [('A',),
     ('B',),
     ('C',),
     ('A', 'B'),
     ('A', 'C'),
     ('B', 'A'),
     ('B', 'C'),
     ('C', 'A'),
     ('C', 'B'),
     ('A', 'B', 'C'),
     ('A', 'C', 'B'),
     ('B', 'A', 'C'),
     ('B', 'C', 'A'),
     ('C', 'A', 'B'),
     ('C', 'B', 'A')]

    """
    for i, _ in enumerate(iterable):
        for x in  permutations(iterable, i+1):
            yield x

    foo = 1

def unroll(ctx, *iterables):
    gen = {}
    value = []
    N = len(iterables)
    value = [None] * N
    gen = [None] * N

    def restart(i):
        g = iterables[i]
        if getattr(g, "__iter__"):
            g = g.__iter__()
        else:
            g = g(**ctx)
        gen[i] = g

    for i in range(N):
        restart(i)
    i = 0
    while True:
        while i < N:
            try:
                x = next(gen[i])
                value[i] = x
                i += 1
            except StopIteration:
                restart(i)
                i -= 1
                if i < 0:
                    return
                continue

        yield value
        i -= 1


def edge(ctx, *iterables):
    gen = {}
    value = []
    N = len(iterables)
    value = [None] * N
    gen = [None] * N

    def restart(i):
        g = iterables[i]
        if getattr(g, "__iter__"):
            g = g.__iter__()
        else:
            g = g(**ctx)
        gen[i] = g

    for i in range(N):
        restart(i)

    while True:
        for i in range(N):
            try:
                x = next(gen[i])
                value[i] = x
            except StopIteration:
                raise
        yield value


def round_robin(*iterators, restart_exahusted=False):
    """Chain all iterators extracting an element alternatvily
    from the 1st generator, the 2dn from the 2nd generator and so on.

    The generator list is cycled and a generator is removed when exahusted.

    """

    def foo_gen(container):
        for item in container:
            yield item

    stack = []
    for gen in iterators:
        if isinstance(gen, CALLEABLE_TYPES):
            gen = gen()
        if isinstance(gen, ITERATOR_TYPES):
            gen = round_robin(*gen, restart_exahusted=restart_exahusted)

        stack.append(gen)

    while stack:
        gen = stack.pop(0)
        for item in gen:
            yield item
            stack.append(gen)
            break
        else:
            # gen exahusted
            if restart_exahusted:
                if isinstance(gen, CALLEABLE_TYPES):
                    gen = gen()
                if isinstance(gen, ITERATOR_TYPES):
                    gen = foo_gen(gen)
                stack.append(gen)


# -------------------------------------
# String Iterators
# -------------------------------------


def to_camel(exp):
    """Convert to Camel Case an expression."""
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


def snake_case(name, separator="_", lower=True):
    """Change capitalized compossed words into '_' separate words."""
    s2 = f"\\1{separator}\\2"
    s1 = re.sub("(.)([A-Z][a-z]+)", s2, name)
    result = re.sub("([a-z0-9])([A-Z])", s2, s1)
    if lower:
        result = result.lower()
    return result


# --------------------------------------------------
# Pandas
# --------------------------------------------------


def _df(d, **ctx):
    if not isinstance(d, (pd.DataFrame, pd.Series)):
        d = new_df(data=d, **ctx)
    return d


def new_df(data, **ctx):
    """create a dataframe based on columns and values expressions.

      >>> df
      symbol
    0     ES
    1     NQ
    """
    log.info(f"data: {data}")
    for key, value in list(data.items()):
        log.debug(f"  {key}: {value}")
        value = lexpand(value, **ctx)
        data[key] = value

    df = pd.DataFrame(data)
    return df


def expand(value, **ctx):
    if isinstance(value, (list, tuple, set)):
        value = value.__class__([expand(x) for x in value])
    elif isinstance(value, (dict,)):
        value = value.__class__({k: expand(v) for k, v in value.items()})
    elif isinstance(value, (int, float, complex)):
        pass
    elif isinstance(value, (str,)):
        try:
            # generic expression from str
            # i.e: range(2, 10), etc
            # will be evaluated a the end of function
            value = eval(value, ctx, ctx)
        except (NameError, SyntaxError):
            pass
        except Exception as why:
            pass
    elif value is None:
        pass

    if isinstance(value, (range,)):
        value = list(value)

    return value


def lexpand(value, **ctx):
    value = expand(value, **ctx)
    if not isinstance(value, (list, tuple, set, dict)):
        value = [x for _, x, _x in zip_like(value, value)]

    return value


def df_concat(*data, **kw):
    kw.setdefault("ignore_index", True)
    return pd.concat([_df(d) for d in data], **kw)


def df_join(*data, **kw):
    """Join multiples df in a single one using method 'how'.
    by default how = 'cross' so result will be the cartesian
    product of all df (expansion).

    input:
    data[0]
      month
    0     H
    1     M
    2     U
    3     Z

    data[1]
       year
    0     2
    1     3

    output:
      month  year
    0     H     2
    1     H     3
    2     M     2
    3     M     3
    4     U     2
    5     U     3
    6     Z     2
    7     Z     3

    Combining:

    1. dict: { "symbol": ["ES", "NQ"] }

    2. dataframe:
         exp04
     0    H2
     1    H3
     2    M2
     3    M3
     4    U2
     5    U3
     6    Z2
     7    Z3
     Name: expiration, dtype: object

     3. dict: { "tf": ["1s", "5s", "1m", "20m", "60m", "1d"] }

     output:

             symbol expiration   tf
      0      ES         H2   1s
      1      ES         H2   5s
      2      ES         H2   1m
      3      ES         H2  20m
      4      ES         H2  60m
      ..    ...        ...  ...
      91     NQ         Z3   5s
      92     NQ         Z3   1m
      93     NQ         Z3  20m
      94     NQ         Z3  60m
      95     NQ         Z3   1d

      [96 rows x 3 columns]


    """
    kw.setdefault("how", "cross")
    data = list(data)
    while data:
        master = data.pop(0)
        if master is not None:
            master = _df(master)
            break

    for d in data:
        df = _df(d)
        master = master.join(df, **kw)
    return master


def df_glue(*data, name="foo", sep="", **kw):
    """Join all row values as a single serie values
    and set a name for the serie in order to be used
    as a index or similar.

    input:
        month  year
    0     H     2
    1     H     3
    2     M     2
    3     M     3
    4     U     2
    5     U     3
    6     Z     2
    7     Z     3

    output:
    0    H2
    1    H3
    2    M2
    3    M3
    4    U2
    5    U3
    6    Z2
    7    Z3
    Name: expiration, dtype: bool
    """
    tmp = df_join(*data, **kw)
    serie = tmp.apply(lambda x: sep.join([str(_) for _ in x]), axis=1)
    serie.name = name
    return serie


# --------------------------------------------------
# Xiterators
# --------------------------------------------------


class Xiterator(dict):
    def __init__(self, *args, **kwargs):
        self._reversed_ = False
        self._sort_ = None
        self._first_ = []

        self._reversed_values = False
        self._sort_values = None
        self._first_values = []

        super().__init__(*args, **kwargs)

        config = self.pop("__config__", {})
        self.__dict__.update(config)

    def _prepare(self):
        self._keys_seq = list(self.keys())
        if self._sort_:
            self._keys_seq.sort(key=self._sort_, reverse=self._reversed_)
        else:
            self._keys_seq.sort(reverse=self._reversed_)

        for k in self._first_[::-1]:
            if k in self._keys_seq:
                self._keys_seq.remove(k)
                self._keys_seq.insert(0, k)

        self._iters = []
        for k in self._keys_seq:
            g = self[k]
            if isgeneratorfunction(g):
                if self._reversed_values:
                    g = reversed(g())
                else:
                    g = g()

            if isinstance(g, dict):
                g = list(g.items())

            if not isinstance(g, (list, dict, set)):
                g = [g]
                if self._reversed_values:
                    g.sort(reverse=self._reversed_values)

            self._iters.append(g)

    def render(self, pattern):
        used = set()
        for data in self:
            item = pattern.format_map(data)
            if item in used:
                continue
            used.add(item)
            yield item


class Xproduct(Xiterator):
    """Smart iterator.

    key: iterator

    iterate over the product of 'named' values
    """

    def __iter__(self, *validators):
        self._prepare()

        for seq in product(*self._iters):
            sequence = Xiterator()
            for i, value in enumerate(seq):
                key = self._keys_seq[i]
                sequence[key] = expand_range(value)

            item = {}
            keys = list(sequence.keys())
            iters = [sequence[k] for k in keys]
            for values in product(*iters):
                for i, value in enumerate(values):
                    key = keys[i]

                    if isinstance(key, str):
                        # "key1, key2" = value[0], value[1]
                        subkeys = [t.strip() for t in key.split(",")]
                        if len(subkeys) == 1:
                            item[key] = value
                        else:
                            # TODO: review multi-keys case (will value[] match?)
                            for j, k in enumerate(subkeys):
                                item[k] = value[j]
                    else:
                        item[key] = value

                # ALL validators must pass the item
                for func in validators:
                    if not func(item):
                        break
                else:
                    yield item

        # print(len(used))
        foo = 1


class Xpickone(Xiterator):
    """Smart iterator."""

    def __iter__(self, *validators):
        self._prepare()
        # list(itertools.product(('ticks',), kk['ticks']))
        # [('ticks', 'midpoint'), ('ticks', 'trades'), ('ticks', 'bidask')]
        for i, key in enumerate(self._keys_seq):
            for value in self._iters[i]:
                yield key, value


class Xexpand(Xiterator):
    """Smart iterator."""

    def __iter__(self, *validators):
        self._prepare()

        for seq in product(*self._iters):
            item = {}
            for i, value in enumerate(seq):
                key = self._keys_seq[i]
                item[key] = value
            yield item


class Xroundrobin(Xiterator):
    """Smart iterator."""

    def __iter__(self, *validators):
        self._prepare()
        # list(itertools.product(('ticks',), kk['ticks']))
        # [('ticks', 'midpoint'), ('ticks', 'trades'), ('ticks', 'bidask')]

        num_active = len(self._iters)
        nexts = cycle(iter(it).__next__ for it in self._iters)
        keys = []
        level = -1
        while num_active:
            try:
                for next in nexts:
                    value = next()
                    if not keys:
                        level += 1
                        keys = list(self._keys_seq)

                    key = keys.pop(0)
                    yield key, value, level
                    # yield next()
            except StopIteration:
                # Remove the iterator we just exhausted from the cycle.
                num_active -= 1
                nexts = cycle(islice(nexts, num_active))


def test_xproduct():
    import random

    xit = Xproduct()
    xit["host"] = ["xps", "mnt", "dream"]
    xit["port"] = list(range(10000, 10010))
    xit["client"] = range(0, 4)

    def custom():
        for n in range(random.randint(1, 20)):
            yield random.randint(0, 10)

    xit["random"] = custom
    xit["repeat"] = [1, 2, 2]

    for i, item in enumerate(xit.iter()):
        print(f"{i} : {item}")

    foo = 1


if __name__ == "__main__":
    test_xiterator()
