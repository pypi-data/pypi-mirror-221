import re

YEAR = r'[12]\d{3}'
DAY = r'\d{4}'
TIME = r'((0\d)|(1\d)|(2[0123]))\d{4}'
TIME2 = r'((0\d)|(1\d)|(2[0123]))\d{2}'
DATE = f"{YEAR}{DAY}-{TIME}"
TIMEFRAME = '(1s)'

def build_extract_pattern(fields):
    """Build a patter for extract"""
    cast = []
    flags = flags or '(?imux)'
    pattern = [flags]
    n = len(fields) - 1
    for i, (k, p, m, f) in enumerate(fields):
        p = p or f'[^{sep}]+'
        if i < n and sep:
            token = f'((?P<{k}>{p})[{sep}]){m}'
        else:
            token = f'((?P<{k}>{p})){m}'

        pattern.append(token)
        cast.append((k, f))
    if end:
        pattern.append(end)

    bsep = f'\n'
    pattern = bsep.join(pattern)
    return pattern, tuple(cast)    

def build_regexp(fields, sep='', flags=None, end='$'):
    cast = []
    flags = flags or '(?imux)'
    pattern = [flags]
    n = len(fields) - 1

    for i, (k, (p, m, f)) in enumerate(fields.items()):
        p = p or f'[^{sep}]+'
        if i < n and sep:
            token = f'((?P<{k}>{p})[{sep}]){m}'
        else:
            token = f'((?P<{k}>{p})){m}'

        pattern.append(token)
        cast.append((k, f))
    if end:
        pattern.append(end)

    bsep = f'\n'
    pattern = bsep.join(pattern)
    return pattern, tuple(cast)


def match_patterns(string, *patterns):
    for pattern in patterns:
        m = re.match(pattern, string)
        if m:
            return m.groupdict()


def compile_multi(fied):
    pass

def ident(x): return x


def parse_muti(string, *xpatterns):
    for (pattern, cast) in xpatterns:
        m = re.match(pattern, string)
        if m:
            d = m.groupdict()
            for (k, f) in cast:
                if f:
                    d[k] = f(d[k])
            return d


# ------------------------------------------------
# testing
# ------------------------------------------------


def test_regexp(pattern, data, show=False):
    results = []
    for match, string in data:
        m = re.match(pattern, string)
        results.append((match ^ (m is None)))
        if show:
            print("-" * 60)
            print(string)
            if m:
                for i, (k, v) in enumerate(m.groupdict().items()):
                    print(f"{i}. {k, v}")
            else:
                print(f"NOT MATCHED!")

    return results


def test():
    sep = r'/.'
    
    # key: the name of the parameter in d  =m.match()
    # pattetn:  for key or None to indicate not separator
    # optional or repetition: '' (mandatory), '?' (could be missing), etc
    # cast to function: if valud musy be casted to any type (e.g. float)
    fields = {
        'provider': (None, '', None),
        'local_symbol': (None, '', None),
        'type': (None, '', None),
        'timeframe': (TIMEFRAME, '', None),
        'date1': (DATE, '', None),
        'date2': (DATE, '?', None),
        'date3': (DATE, '?', None),
        'ext': ('xz|gz', '?', None),
    }

    data = [
        (True, "ib/ESU8/bar/1s/20180903-070000.xz"),
        (False, "ib/ESU8/bar/1s/30180903-070000.xz"),
        (True, "ib/ESU8/bar/1s/20180903-070000.20180903-235959.xz"),
        (True, "ib/ESU8/bar/1s/20180903-070000.20190101-090000.20190601-100000.xz"),
        (False, "ib/ESU8/bar/1s/20180903-070000.20190101-090000.20190601-100000.csv"),
    ]

    pattern = build_regexp(fields, sep, )
    result = test_regexp(pattern, data, show=True)

    print(result)
    print(f"Result: {all(result)}")

    assert all(result)

    # tets multiopcions
    d = match_patterns(data[0][1], pattern)
    assert d
    print(d)


if __name__ == '__main__':
    test()


