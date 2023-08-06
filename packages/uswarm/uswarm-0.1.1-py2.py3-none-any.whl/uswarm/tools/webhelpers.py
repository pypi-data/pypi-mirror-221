"""
- [x] opener for xls, xlsx, csv, pickle formats into pandas dataframe.
- [x] convert any input file into lighting pickle format.
- [x] have a look to the final CSV format structure.
- [ ] create a DB with all data needed per record.
- [ ] build *descriptores* (dc.subject[es_ES] column) inference.
- [ ] use dc.identifier[es_ES] as index in all dataframe.

"""
import os
import re
import time


import numpy as np
import pandas as pd
import pickle

from uswarm.tools import fileiter

# ---------------------------------------------
# Loaders
# ---------------------------------------------
opener = {
    ".xls": pd.read_excel,
    ".xlsx": pd.read_excel,
    ".csv": pd.read_csv,
    ".pickle": pd.read_pickle,
}


def openfile(path, **kw):
    # print(f"Opening: {path}")
    _, ext = os.path.splitext(path)
    t0 = time.time()
    df = opener[ext](path, **kw)
    t1 = time.time()
    elapsed = t1 - t0
    # print(elapsed)
    return df


# ---------------------------------------------
# Normalize Data
# ---------------------------------------------

IMG_KEY = """(?imux)
(?P<key>70_\d{7})
$"""


def normalize_df(df, cols=None, inplace=True):
    """Normalize a input DF into own style:

    - Index by '70_xxx' field (INDEX_COLUMNS)
    - [ ] find key column by regexp on name
    - [ ] check that values match regexp on values

    """
    # find the common key used to match records accross
    # all data files
    cols = cols or INDEX_COLUMNS_MAP
    index = locate_columns(df, cols)
    if index:
        try:
            sample = df[index]  # .dropna()
            test = sample.astype(str).str.match(IMG_KEY)
            failed = test[~test]
            bad = failed.count()
            n = sample.count()

            r = (n - bad) / n

            if r > 0.80:
                if r < 1.0:
                    print(f"Warning: dataframe has {bad} badformed IMG_KEY record")
                    print(df[~test][["id", index]])
                    print("Skipping bad records ...")
                    df = df[test]
                assert df[index].str.match(IMG_KEY).all()
                df.set_index(index, inplace=inplace)
                return df
        except Exception as why:
            pass
    # print(f"Warning: can not find IMG_KEY column in datafile")
    # print(df.head())
    return df


# ---------------------------------------------
# Learning Samples
# ---------------------------------------------


# ---------------------------------------------
# Get tokens and creating maps
# ---------------------------------------------
REG_TOKENS = """(?imux)
([a-z|á-ú]{min_len,20})
"""

TRX_MAP = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u",
    "Á": "A",
    "É": "E",
    "Í": "I",
    "Ó": "O",
    "Ú": "U",
}

TRX_MAP = str.maketrans(TRX_MAP)


def tokens(string, regexp=None, min_len=3):
    regexp = regexp or REG_TOKENS
    regexp = regexp.replace("min_len", str(min_len))
    tokens = [
        singular(x.lower().translate(TRX_MAP)) for x in re.findall(regexp, string)
    ]

    return set(tokens)


def ltokens(string, regexp=None, min_len=3):
    tks = list(tokens(string, regexp, min_len))
    tks.sort()
    return tks


REG_ES_PLURAL = """(?imux)
(?P<root>.*?)
(?P<end>[a-u]?s)
$
"""


def singular(word):
    m = re.match(REG_ES_PLURAL, word)
    if m:
        return m.groups()[0]
    return word


# ---------------------------------------------
# Get Tasks groups
# ---------------------------------------------

TASK_FOLDER = """(?imux)
(?P<root>(PROCESADO)/
  (?P<tid>\d+
  [^/]+
  )
  #.*?
)
/
(?P<filename>
  (?P<basename>
    #(?!rea).*
    (\d+).*
  )
  (?P<ext>\.(pickle))
)
$"""

MASTER_TASK_FOLDER = """(?imux)
(?P<root>(PROCESADO)/
  (?P<tid>
  #05
  \d+
  [^/]+
  )
  #.*?
)
/
(?P<filename>
  (?P<basename>
    #(?!rea).*
    (\d+).*
  )
  (?P<ext>\.(xlsx))
)
$"""


def find_tasks():
    for path, d in fileiter(top, regexp=TASK_FOLDER, exclude=EXCLUDE, info="d"):
        # print(f"Found {path}")
        yield path, d


def find_master_tasks():
    for path, d in fileiter(top, regexp=MASTER_TASK_FOLDER, exclude=EXCLUDE, info="d"):
        # print(f"Found {path}")
        yield path, d


REA_FILE = """(?imux)
(?P<basename>rea(?P<surname>.*?))
(?P<ext>\.(pickle))
$"""


def find_rea(top):
    for path, d in fileiter(top, regexp=REA_FILE, exclude=EXCLUDE, info="d"):
        # print(f"Found {path}")
        yield path, d


INDEX_COLUMNS = set(["dc.identifier[es_ES]", "SIGNATURA"])

INFERENCE_TITLE = "dc.title[es_ES]"
INFERENCE_DENOM = "iaph.bien.denominacion[es_ES]"
INFERENCE_DESC = "dc.subject[es_ES]"

DESCRIPTOR_COLUMNS = set([INFERENCE_DESC])


INFERENCE_SOURCE_COLUMNS = set([INFERENCE_TITLE, INFERENCE_DENOM])
INFERENCE_COLUMNS = set(list(DESCRIPTOR_COLUMNS) + list(INFERENCE_SOURCE_COLUMNS))


INSPECT_COLUMNS = set(["dc.date.accessioned", "dc.contributor.author[es_ES]"])


top = "."
INPUTS = """(?imux)
.*
(?P<ext>(xls|xlsx|csv|pickle))
$"""

EXCLUDE_SYNC = """(?imux)
(?P<sync>\.sync/)
.*
"""
EXCLUDE_UPLOAD = """(?imux)
(?P<upload>upload/)
.*
"""

EXCLUDE = [EXCLUDE_SYNC, EXCLUDE_UPLOAD]

SAMPLE = """(?imux)
(learning|training)-data
.*?
/
(?P<name>sample\..*?)
(?P<ext>(pickle))
$"""

IGNORE = """(?imux)
.*?
(?P<name>ignore-words)
.*?
(?P<ext>(pickle))
$"""


def convert_to_pickle():
    # covert all data files to pickle format
    for path, d in fileiter(top, regexp=INPUTS, exclude=EXCLUDE, info="d"):
        if "upload" in path:
            continue
        base, ext = os.path.splitext(path)
        filename = base + ".pickle"
        if (
            ext not in (".pickle",)
            and not os.path.exists(filename)
            or os.stat(path).st_mtime > os.stat(filename).st_mtime
        ):
            # print(f"Converting: {path} -> {filename}")
            # sig = hashlib.md5(bytes(path, 'utf-8')).hexdigest()

            df = openfile(path)
            df = normalize_df(df)
            df.to_pickle(filename)
            continue

        # df = openfile(filename)

        # print(df)
        # df.dropna(subset=['SIGNATURA',], inplace=True)
        # df.set_index('SIGNATURA', inplace=True)
        # print(df)
        # print(df.axes)

        # filename = hashlib.md5(bytes(path, 'utf-8')).hexdigest()

        # df.to_pickle('filename.pickle')


# ---------------------------------------------
# get tokens and resuls maps
# ---------------------------------------------


def create_maps():

    ignored_words = set()
    for path, d in fileiter(top, regexp=IGNORE, exclude=EXCLUDE, info="d"):
        df = openfile(path)
        ignored_words.update(df["IGNORED"])

    assert ignored_words, "Can not load any IGNORED files"

    # TODO: select columns by regexp, not columns definition
    # TODO: just assert column name is in know candidate columns.
    # all_desc = set()
    # all_tokens = set()
    # inference_map = {}
    # token_desc = {}

    for path, d in fileiter(top, regexp=SAMPLE, info="d"):
        all_desc = set()
        all_tokens = set()
        inference_map = {}
        token_desc = {}

        df = openfile(path)
        descriptor = DESCRIPTOR_COLUMNS.intersection(df.columns)
        assert (
            len(descriptor) == 1
        ), f"Can no select a descriptor from {DESCRIPTOR_COLUMNS}"
        descriptor = descriptor.pop()

        desc = df[descriptor]

        # check records with missing descriptors
        missing = df[desc.isna()][INSPECT_COLUMNS]
        if missing.size > 0:
            print("= Records with Missing descriptors =================")
            print(missing)
            print(f"missing descriptor in {missing.shape[0]} in records")

        # print(descriptors)
        # kk = descriptors.head()

        df_inference = df[~desc.isna()][INFERENCE_COLUMNS]
        df_inference.fillna("", inplace=True)

        for index, row in df_inference.iterrows():
            title = row[INFERENCE_TITLE]
            denom = row[INFERENCE_DENOM]

            desc = [x.strip() for x in row[INFERENCE_DESC].split("||")]

            # TODO: give different weights to each type of tokens
            title = tokens(title).difference(ignored_words)
            denom = tokens(denom).difference(ignored_words)

            # print(f"{title} {denom} : {desc}")

            all_tokens.update(title)
            all_tokens.update(denom)

            tks = list(set(list(title) + list(denom)))
            tks.sort()
            tks = tuple(tks)

            all_desc.update(desc)
            for d in desc:
                holder = inference_map.setdefault(d, dict())
                for word in tks:
                    holder[word] = holder.get(word, 0) + 1

            for word in tks:
                holder = token_desc.setdefault(word, dict())
                for d in desc:
                    holder[d] = holder.get(d, 0) + 1

            foo = 1
        foo = 1

        basename, _ = os.path.splitext(path)

        with open(f"{basename}.descriptors.txt", "wt") as f:
            aux = list(all_desc)
            aux.sort()
            f.write("\n".join(aux))

        pickle.dump(inference_map, open(f"{basename}.inference_map.pickle", "wb"))
        pickle.dump(token_desc, open(f"{basename}.token_desc.pickle", "wb"))

    foo = 1


# create_maps()


COLUMNS_MAP = {
    "autoria": "dc\.contributor\.author\[es_ES\]",
    "denominacion": "iaph\.bien\.denominacion\[es_ES\]",
    "descriptor": "dc\.subject\[es_ES\]",
    "descripcion": "dc\.description\[es_ES\]",
    "derech": "dc\.rights\[es_ES\]",
    "derech_uri": "dc\.rights.uri\[es_ES\]",
    "ejecucion_fecha": "dc\.date\.issued(\[es_ES\])?",
    "formato": "dc\.format\[es_ES\]",
    "fuente": "dc\.source\[es_ES\]",
    "provincia": "iaph\.provincia\[es_ES\]",
    "municipio": "dc\.coverage.spatial\[es_ES\]",
    "titulo": "dc\.title\[es_ES\]",
    "tipo": "dc\.type\[es_ES\]",
}

INDEX_COLUMNS_MAP = set(
    [
        "(?imux)signatura",
        "(?imux)dc\.identifier\[es_ES\]",
    ]
)
ALIAS = {
    "type": "tipo",
}

REG_COLUMNS = """(?imux)
([0-9|a-z|_-]{min_len,200})
"""


def normalize_columns(*columns, regexp=None):
    # tokens('Derechos URI')
    # regexp = regexp or REG_COLUMNS
    columns = ["_".join(ltokens(col, regexp, 1)) for col in columns]
    columns = [ALIAS.get(k, k) for k in columns]
    return columns


def build_map(source, target, cols):
    cmap = {}
    # normalize columns names
    source.columns = normalize_columns(*source.columns)

    # check if there are missing columns
    src_cols = source.columns

    for left, rigth in cols.items():
        if left not in src_cols:
            # find col using reg exp
            # print(f"- Missing map : {left} --> {rigth}")
            continue

        if target is not None:
            tar_cols = target.columns

            for col in tar_cols:
                if re.match(rigth, col):
                    # print(f"+ Match columns: {left} --> {col}")
                    cmap[left] = col
                    break
            else:
                print(f"Can't find a match for {left} -> {rigth}")

    return cmap


def locate_columns(df, regexp):

    cmap = {}
    for col in df.columns:
        for reg in regexp:
            if re.match(reg, col):
                return col

    foo = 1


def patch_df(source, target, cmap):

    for idx, src in source.iterrows():
        # row = target.loc[idx]
        if idx in target.index:
            for k1, k2 in cmap.items():
                value = src[k1]
                # print(f"[{idx}]: {k1}={value} --> {k2}")
                target.loc[idx, k2] = value
                foo = 1
        foo = 1
    foo = 1


# ------------------------------
MASK_DESCRIPTORS = """(?imux)
(?P<root>(db)/
  (?P<tid>
  descriptors
  )
)
/
(?P<filename>
  (?P<basename>
    .+?
  )
  (?P<ext>\.(txt))
)
$"""


def find_descriptors():
    for path, d in fileiter(top, regexp=MASK_DESCRIPTORS, exclude=EXCLUDE, info="d"):
        # print(f"Found {path}")
        yield path, d


REG_DESCRIPTOR = """(?imux)
(?P<descriptor>
  (?P<text>
    [^:]+
  )
  ::
  (?P<cod1>
    \d+
  )
  ::
  (?P<cod2>
    \d+
  )
)
$"""

DESCRIPTORS = dict()
DESC_ALIASES = dict()

def parse_descriptor(line):
    m = re.match(REG_DESCRIPTOR, line)
    if m:
        d = m.groupdict()
        return d
    return {}

def sanitize(info):
    global DESC_ALIASES
    desc = info.get('desc')
    if desc:
        # check descriptors
        if not DESCRIPTORS:
            for path, d in find_descriptors():
                for line in open(path).readlines():
                    m = re.match(REG_DESCRIPTOR, line)
                    if m:
                        d = m.groupdict()
                        DESCRIPTORS[d['text']] = d['descriptor']
                    else:
                        print(f"DESC: don't match: {line.strip()}")
                        foo = 1
        if not DESC_ALIASES:
            aux= openfile('db/descriptors/aliases.csv', index_col='mala')
            aux = { k.strip() : v.strip() for k, v in aux.to_records() }


            DESC_ALIASES.update(aux)

            foo = 1

        foo = 1
    return info
