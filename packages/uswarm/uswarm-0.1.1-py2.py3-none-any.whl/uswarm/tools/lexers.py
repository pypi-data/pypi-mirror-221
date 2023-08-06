"""Lexers for AI / ML texts analysis.

"""
import re

# ---------------------------------------------
# Get tokens and creating maps
# ---------------------------------------------
REG_ES_PLURAL = """(?imux)
(?P<root>.*)
(?P<end>[a-u]s)
$
"""


def singular(word):
    m = re.match(REG_ES_PLURAL, word)
    if m:
        return m.groups()[0]
    return word

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

def normalize_string(string,**kw):
    return string.translate(TRX_MAP).lower()

def normalize_string_2(string,**kw):
    return string.translate(TRX_MAP).lower(), {}


def tokens(string, regexp=None, min_len=3):
    regexp = regexp or REG_TOKENS
    regexp = regexp.replace("min_len", str(min_len))

    string = normalize_string(string)
    tokens = re.findall(regexp, string)
    #tokens = [x.lower() for x in tokens]
    #tokens = [normalize_string(x) for x in tokens]
    #tokens = [singular(x) for x in tokens]
    #tokens = [x for x in tokens if len(x) >=3]

    return tokens

def stokens(string, regexp=None, min_len=3, ignored=None):
    tks = tokens(string, regexp, min_len)
    tks = set(tks)
    tks = tks.difference(ignored) if ignored else tks
    return tks

def ltokens(string, regexp=None, min_len=3, ignored=None):
    tks = list(stokens(string, regexp, min_len, ignored))
    tks.sort()
    return tks


