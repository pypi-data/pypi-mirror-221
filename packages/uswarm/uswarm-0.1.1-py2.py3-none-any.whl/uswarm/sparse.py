# -*- coding: utf-8 -*-
"""
This module provides support for large sparse files that stores
its information in *blocks* for faster read acess.

Sparse files stores *records* that contains a *key* which is used
for creating blocks containing a range of suchs keys.

Records are stored using compressed csv format with lzma
('xz' command line suite).

Tipical examples are historical or transactions records using
date as key for indexing.

User may set a prefereable block size in disk and Sparse file will
provide a metrics for the real used size as compression is not
deterministic.

Reallocation of the blocks to approach a better size fitting is
possible, but may require long time for big data files.

TODO: use other compression format but 'xz'.

"""
import os
import glob
import time
import re
import random
import lzma as xz
import tempfile
import fcntl

from collections import OrderedDict
from datetime import datetime

from arrow import Arrow, parser

try:
    from StringIO import StringIO, FileIO
except ImportError:
    from io import StringIO, FileIO


from uswarm.tools import (
    expandpath,
    fileiter,
    soft,
    supdate,
    _find_match,
    _prepare_test_regext,
)
from uswarm.tools.containers import build_set, linear_containers
from uswarm.tools.converters import (
    Date,
    Str,
    Float,
    date_normal,
    short_float,
    date_with_miliseconds,
    item_normal,
)
from uswarm.tools.system import pid_of
from uswarm.tools.units import timeframe2delta, parse_date, parse_arrow, neg_delta


# --------------------------------------------------
# logger
# --------------------------------------------------
from uswarm.tools.logs import logger, exception, debug, info, warn

log = logger(__name__)



COMPRESSOR = {
    "xz": xz.compress,
}

DECOMPRESSOR = {
    "xz": xz.decompress,
}

MODES = {
    "rt": "rb",
    "r": "rb",
    "wt": "wb",
    "w": "wb",
}


# ------------------------------------------------
# Sparse files
# ------------------------------------------------


class SparseFile:

    """
    Sparse file uses a folder to store all data blocks.

    It also uses some private sub-folders for temporal operations
    or showing some warnings about miss-uses: journal, review, etc.

    *Open a file within Repository.*

    The mode can be 'r' (default), 'w', 'x' or 'a' for reading,
    writing, exclusive creation or appending.  The file will be created if it
    doesn't exist when opened for writing or appending; it will be truncated
    when opened for writing.  A FileExistsError will be raised when file already
    exists and trying to create a new one, preventing overwrites.

    Opening a file for creating implies behaves in a similar way to 'w'.
    Add a '+' to the mode to allow simultaneous reading and writing.

    A custom opener can be used by passing a callable as *opener*.

    The underlying file descriptor for the file object is then obtained by
    calling opener with (*name*, *flags*).

    *opener* must return an open file descriptor (passing os.open as *opener*
    results in functionality similar to passing None).

    As repository can handle different types of data, a file within repository
    may have different encoders and decoders to write and read ``Items``
    from disk.

    """

    KEY = 0
    DECODER = {"default": [str]}  # decoders by klass
    ENCODER = {"default": [str]}  # encoders by klass

    def __init__(
        self, query, mode, repository, allow_overwriting=True, *args, **kwargs
    ):

        self.query = query
        self._encoders = query.get(
            "encoders", self.ENCODER.get(query["klass"]) or self.ENCODER["default"]
        )
        self._decoders = query.get(
            "decoders", self.DECODER.get(query["klass"]) or self.DECODER["default"]
        )
        self.KEY = query.get("pkey", self.KEY)

        self.mode = mode
        self.repository = repository
        self.allow_overwriting = allow_overwriting

        self._last_key = None

        # boundaries
        self._bound_left = self._bound_right = None
        self._delta = self._get_delta(**query)
        begin = query.get("being")
        begin and self._set_boundary(begin)

        # file and underlying files
        # depending on opening mode (r, w)
        self._journal_path = None
        self._journal_file = None
        self._read_path = None
        self._read_file = None
        self._read_record = None
        self._read_line = None

        self.write = self._write_1st_time

        self._closed = False

    def __iter__(self):
        return self.read_records()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.close()
        elif exc_type in (OverwrittenError,):
            self._close_by_exception()
        else:
            foo = 1

    def _close_by_exception(self):
        """Invoked on exception"""
        self._journal_file and self._journal_file.close()
        self._read_file and self._read_file.close()

        if self.mode not in ("r", "rt") and self._read_path != self._journal_path:
            os.unlink(self._journal_path)

    # --------------------------------------------
    # Writable methods
    # --------------------------------------------
    def writable(self):
        """True if file was opened in a write mode."""
        return self.mode in ("w", "a", "at", "ab", "wt", "w+")

    def write(self, record):
        raise RuntimeError("must be replaced on run time.")

    def _write_regular(self, record):
        """*Write a record into cluster.*

        - [x] get the key from record
        - [x] check if we need to create a new cluster or can write in current one
            - [x] close and create a new underlying cluster

        - [ ] check GAP with underlying.
              copy all existing records from underlying until current key
        - [ ] check that current record matchs with underlying

        - [ ] encode record into writable form
        - [ ] append to the end of cluster
        """
        key = self._get_key(record)
        if key and key > self._bound_right:
            self._open_block(key)

        # Fast-Fwd: copy all records from read
        # to journal file until reach the same key
        self._fast_forward(key)

        if self._last_key and key <= self._last_key:
            # should be monotone crescend? -> review
            self._add_review_record(record)
        else:
            # add record to cluster
            if self._read_file and not self.allow_overwriting:
                # check that underlying record and current one match
                # otherwise it will raise an exception
                record = self._read_record.__class__(record)
                if record != self._read_record:
                    raise OverwrittenError(
                        f"Overwritting mismatched records is not allowed {record} and {self._read_record}"
                    )
            # write th file and move 'last' key.
            self._journal_file.write(self._encode(record))
            self._last_key = key

    def _write_1st_time(self, record):
        """Is used only 1st time when no records has been writen.
        Just to simplify / make faster writing operations.
        """
        key = self._get_key(record)
        self._open_block(key)
        assert self._bound_left
        assert self._bound_right

        self.write = self._write_regular
        self.write(record)

    def close(self):
        self._close()
        self._closed = True

    @property
    def closed(self):
        return self._closed

    def flush(self):
        """Flush content by closing an open the file in the same position."""
        # self.close()
        assert self._last_key
        self._open_block(self._last_key)

    # --------------------------------------------
    # xxxx methods
    # --------------------------------------------
    def _get_delta(self, **query):
        raise NotImplementedError()

    def _open_block(self, key):
        if self._journal_file is not None:
            # TODO: move underlying too?
            self._close()

        assert self._journal_file is None
        assert self._read_file is None

        # set the new boundaries
        self._set_boundary(key)

        repo = self.repository

        #
        # Prepare the reading file
        self.query, self._read_path = repo._get_path(
            self.query,
            "rt",
            begin=self._bound_left,
            end=self._bound_right,
        )

        if os.path.exists(self._read_path):
            self._read_file = self._open(self._read_path, "rt")
        self._read_line = self._read_record = None

        #
        # Prepare the writing file
        if self.writable():
            # check if journal is currentlt used by any other process
            self._journal_path = self._read_path.replace(repo.root, repo.journal)
            # check journal file is locked, then raise an exception
            # is still locker by a process 10 sec later.
            if os.path.exists(self._journal_path):
                for _ in range(20):
                    # seach a process that is using this journal
                    # and wait until none is using this journal file.
                    for pinfo in pid_of(self._journal_path):
                        time.sleep(0.5)
                        break
                    else:  # is not used by anyone
                        break
                else:
                    raise JournalLocked(
                        f"Journal File: {self._file_path} is locked by pids: {pinfo}"
                    )

            self._journal_file = self._open(self._journal_path, self.mode)

        else:  # both cluster files are the same. # TODO: why ???
            self._journal_file = self._read_file
            self._journal_path = self._read_path

    def _get_key(self, record):
        return record[self.KEY]

    def _shift_cluster(self, steps=1):
        """*Move the working cluster to the next (steps) cluster.*

        - Close current underlying file.
        - Open the next cluster underlying jumping *steps* on the ``right``.
        - Negative steps meand moving to the left.
        - steps=0 forces to re-open current cluster (e.g. 1st time use).

        Note: We asume that ``product`` operation is defined for the
              object defined as key (e.g. datetime)
        """
        if self._journal_file is not None:
            # TODO: move underlying too?
            self._close()

        self._last_key = None
        repo = self.repository
        bound_xleft = repo.stats.get("begin")
        bound_xright = repo.stats.get("end")

        self._bound_left = self._bound_left or bound_xleft

        # we assume used keys has the product operation define for them.
        # otherwise we need iterate loop
        if steps >= 0:
            delta = self._delta
        else:
            delta = neg_delta(self._delta)

        # move current window until we found a
        # cluster where we can read from
        for _ in range(abs(steps)):
            self._bound_left = self._shift_keys(self._bound_left, delta)

        self._set_boundary(self._bound_left)
        if not self.writable() and (
            self._bound_left is None
            or self._bound_right is None
            or self._bound_left> bound_xright
            or self._bound_right < bound_xleft
        ):
            self._closed = True
            return

        # do not alter original query
        # self.query['begin'], self.query['end'] = self.bound_left, self.bound_right

        # Prepare the underlying cluster
        query, self._read_path = repo._get_path(
            self.query, "rt", begin=self._bound_left, end=self._bound_right
        )

        self._read_line = self._read_record = None
        self._delta = self._get_delta(**query)

        if os.path.exists(self._read_path):
            # open underlying and read first record if exists
            self._read_file = self._open(self._read_path, "rt")
        else:
            assert not self.writable()
            self._read_file = None

        if self.writable():
            if self._bound_left:  # is set, then open the cluster
                # check if journal is currentlt used by any other process
                self._journal_path = self._read_path.replace(repo.root, repo.journal)

                # journal file is locked, then raise an exception
                # is still locker by a process for the nex 10 secs.
                if os.path.exists(self._journal_path):
                    for _ in range(20):
                        for pinfo in pid_of(self._journal_path):
                            time.sleep(0.5)
                            break
                        else:  # is not used by anyone
                            break
                    else:
                        raise JournalLocked(
                            f"Journal File: {self._file_path} is locked by pids: {pinfo}"
                        )

                self._journal_file = self._open(self._journal_path, self.mode)
            else:
                # delay the file creation until we know the cluster in the 1st write attempt
                self._journal_file = self._journal_path = None
        else:  # both cluster files are the same. # TODO: why ???
            self._journal_file = self._read_file
            self._journal_path = self._read_path

    def _open(self, path, mode):
        """Low level opening method.
        # TODO: open file specific format, appart 'xz' fmt
        """
        os.makedirs(os.path.dirname(path), exist_ok=True)
        file = xz.open(path, mode)
        return file

    def _close(self):
        """Close the current cluster.

        A closed file cannot be used for further I/O operations.  close() may be
        called more than once without error."""
        # info("-- Closing file")
        if self._read_file:
            if self.mode not in ("r", "rt"):
                # debug(">> Flushing underlying into journal before closing")
                self._fast_forward(self._bound_right)
            self._read_file.close()
            self._read_file = None

        if self._journal_file:
            self._journal_file.close()
            self._journal_file = None

        if self.mode not in ("r", "rt") and self._read_path != self._journal_path:
            # debug(f">> CL: moving journal to {self._underlaying_path}")
            os.renames(self._journal_path, self._read_path)
            # self._file_path = self._underlaying_path

        # self._last_key = None

    # -------------------------------------------

    def _set_boundary(self, key):
        raise NotImplementedError()

    def _get_block_info(self, **query):
        raise NotImplementedError()

    def _shift_keys(self, key, delta):
        """Default method for moving keys based on offset.
        Other subclassses may use different aritmetic.
        """
        return key and (key + delta)

    def _boundary_clusters(self):
        raise NotImplementedError()

    def _get_sanity_path(self, build=True):
        repo = self.repository
        path = os.path.join(repo.review, repo.SANITY.format(**self.query))
        build and os.makedirs(os.path.dirname(path), exist_ok=True)
        return path

    def _add_review_record(self, record):
        """Add a record to review. Reasons:
        - key was lower that head of the cluster (writing must be monotone crescend)
        """
        with open(self._get_sanity_path(), "at") as file:
            line = self._encode(record)
            file.write(f"{line}")

    # specific functions -----------------------

    def _fast_forward(self, key, dump_current=False):
        """*Move records from underlying to working file until key is reached.*"""

        while True:
            # we always need the parsed record to compare keys
            self._read_record = self._get_read_record()
            if self._read_record:
                rkey = self._get_key(self._read_record)
                if rkey < key:
                    self._journal_file.write(self._read_line)
                    continue
            break

    # def _fast_forward_org(self, key):
    # """*Move records from underlying to working file until key is reached.*"""
    # if not self._read_record:
    # for self._read_record in self._underlaying_reader:
    # break

    # if self._read_record:
    # rkey = self._get_key(self._read_record)
    # if rkey < key:
    # for self._read_record in self._underlaying_reader:
    # rkey = self._get_key(self._read_record)
    # if rkey >= key:
    # break
    ## print(f">> FF: {self._underlaying_line}", end='')
    # self._journal_file.write(self._read_line)
    ## print(f">> FF: {key} Done!")

    def read_records(self):
        if self._journal_file is None:
            self._shift_cluster(0)
            # self._set_boundaries(**self.query)
            # assert self._bound_left
            # assert self._bound_right

        while self._journal_file:
            try:
                line = self._journal_file.readline()
                while line:
                    record = self._decode(line)
                    yield record
                    line = self._journal_file.readline()
            except EOFError as why:
                print(f"ERROR in file: {why}, continue!")
            self._shift_cluster()
        foo = 1

    def _get_read_record(self):
        try:
            self._read_line = self._read_file.readline()
            record = self._decode(self._read_line)
            return record
        except Exception as why:
            pass
            # print(f"ERROR in file: {why}, continue!")

    def _encode(self, record):
        """default (cvs) encoding a record to be written into cluster"""
        data = []
        l = len(self._encoders)
        for i, item in enumerate(record):
            func = self._encoders[i] if i < l else self._encoders[-1]
            data.append(func(item))

        line = f"{(','.join(data))}\n"
        return line

    def _decode(self, row):
        """default (csv) decoding a line to extract the record stored in the line"""
        record = []
        l = len(self._decoders)
        for i, value in enumerate(row.split(",")):
            func = self._decoders[i] if i < l else self._decoders[-1]
            record.append(func(value))
        return record


class Repository:
    """
    Basic support of repository of big data, oriented for
    - Fast reading
    - Fast distributed synching
    - Low disk usage
    - Information are stored in clusters.
    - Based on query, repository knows in which clusters data should be located.

    Writting process may be slow, but is ok if the other goals are got.

    Initial approach is to handle large respositories supported by
    chung files that contains the information in a sparse scheme.

    Then an user open a "dataframe" that contains the query of the subset
    of data required and the virtual file provide the information stream.

    Typical use cases could be:

    - CSV files for Scientific Machine Learning process using Scikit (or Dask)
    - CSV files for historical market data
    - etc.

    Example:

    file = repository.open('ESH0.bar.20200301-113000.20200305-230000.5s.csv', 'r')

    then repository provide a file-alike object that can be read getting
    the desired data-stream.

    Note that file names contains the "query" to be analized, the file
    doesn't need to exists.

    The query params are extracted from filename or may be provide using
    extra key-arguments in open(), but is less portable.

    Several regular expressions may be configured in resposotory to extract
    these query-parameters.

    repository.add_pattern(r'....')

    """

    # Just to indicate the type or options that a query parameters can be
    PARAMS = OrderedDict(
        klass=["FOO", "BAR", "BUZZ"],
        begin="date",
        end="date",
        ext=["xz"],
        cmp=["xz"],
        fmt=["csv"],
    )

    # Note: all params must be supplied in query (don't use None as defaults)
    # This is only an example, subclassing must define a specific one
    PATH = {
        "default": "{klass_name}/{key1}/{key21}.{key22}.{ext}",
    }
    DEFAULT_QUERY = {
        "default": {
            "pkey": 0,
            "fmt": "csv",
            "ext": "xz",
            "cmp": "xz",
        },
    }

    SANITY = "{klass}/{key1}/{key21}.{key22}.{ext}"

    DEFAULT_CLUSTER_SIZE = 3600
    CLUSTER_SIZE = {}

    CONVERTER = {
        # datetime: 'item.strftime("%Y%m%d-%H%M%S")',
        "begin": [
            ("dt1", 'item.strftime("%Y%m%d-%H%M%S")'),
            ("date1", 'item.strftime("%Y%m%d")'),
            ("time1", 'item.strftime("%H%M%S")'),
        ],
        "end": [
            ("dt2", 'item.strftime("%Y%m%d-%H%M%S")'),
            ("date2", 'item.strftime("%Y%m%d")'),
            ("time2", 'item.strftime("%H%M%S")'),
        ],
        "klass_name": [
            ("klass", "self.ALIASES.get(item, item)"),
        ],
    }
    for label, items in list(CONVERTER.items()):
        for i, (name, exp) in enumerate(items):
            CONVERTER[label][i] = (name, compile(exp, "<input>", "eval"))

    PARSER = {}

    ALIASES = {}

    DEFAULT_FACTORY = None  #: need to be redefined

    def __init__(self, root, patterns=None, allow_overwriting=True, *args, **kw):
        super().__init__(*args, **kw)

        self.FACTORY = {}

        root = expandpath(root)
        os.makedirs(root, exist_ok=True)
        self.root = root
        self.stats = {}

        # working paths
        self.journal = expandpath(os.path.join(self.root, "__journal__"))
        self.review = expandpath(os.path.join(self.root, "__review__"))
        self.unknown = expandpath(os.path.join(self.root, "__unknown__"))

        self.patterns = build_set(patterns)
        self.allow_overwriting = allow_overwriting

        self._add_patterns(
            r"""(?imux)
            (?P<klass_name>[^./-]+)
            ([./-](?P<sub>[^./-]+))?
            ([./-](?P<fmt>(csv)))?
            ([./-](?P<ext>(xz)))?
            $
        """
        )

    def _inspect_repository(self, clean=False):
        if clean:
            self.stats.clear()

        stats = self.stats
        # stvfs = None
        blksize = None
        required = set(["date1", "time1", "time2"])

        for path, d in fileiter(self.root, self.patterns, info="d", relative=True):
            if not required.intersection(d):
                continue

            begin, end = self._get_boundaries(d)

            stats["begin"] = min(stats.get("begin", begin), begin)
            stats["end"] = max(stats.get("end", end), end)
            stats["files"] = stats.get("files", 0) + 1

            fpath = os.path.join(self.root, path)
            st = os.stat(fpath)

            # cummulative stats
            for name in "st_size", "st_blocks", "st_blksize":
                stats[name] = stats.get(name, 0) + getattr(st, name)

            # stvfs = stvfs or os.statvfs(fpath)
            blksize = blksize or st.st_blksize

        # blksize: is the efficient block size in bytes that
        # OS uses every time the file needs to grow up.
        # this may be used to *reassign* chunks by increasing
        # the delta-resolution used by this repository.
        if blksize:
            stats["blksize"] = blksize
        return stats

    def open(self, path="", mode="rt", query=None, **kw):
        """Open a file for reading/writing repository info

        'path' is only used to extract parameters parsing name

        In 'read' mode:

        - [ ] compute cluster names
        - [ ] try to reach head of the stream
        - [ ] raise an Exception everytime a GAP in data is not found

        In 'write' mode:
        - [ ] Compute cluster names (and remmenber date boundaries if they are specified)
        - [ ] try to lock the journal file associated to current cluster
        - [ ] Raise FileLockException is somene is using

        """
        self.stats = self.stats or self._inspect_repository()

        q = self._extract_params(path)
        q.update(query or {})
        q.update(kw)

        q = self._convert_query(q)

        assert q, f"can not extract any field from {path}"

        stream = self._new_stream(q, mode)
        assert isinstance(stream, SparseFile)
        assert stream._journal_path is None
        return stream

    # ------------------------------------------------------
    # Pattern extraction from filename
    # ------------------------------------------------------
    def _add_patterns(self, *regexp):
        """Add a pattern for extracting fields from path name."""
        regexp = build_set(
            [
                re.compile(r, re.DOTALL | re.I | re.VERBOSE)
                for r in linear_containers(regexp)
            ]
        )
        self.patterns.update(regexp)

    def _extract_params(self, filename):
        "Extract query parameters analyzing filename"
        m = _find_match(filename, self.patterns)
        assert m, f"{filename} does not match any pattern extraction rule"

        return self._parse_query(m.groupdict())

    def _parse_query(self, query):
        """Convert known query parameters"""
        result = query.__class__()
        for name, item in query.items():
            func = self.PARSER.get(name, None)
            if func:
                item = func(item)
            # name = self.ALIASES.get(name, name)
            # item = self.ALIASES.get(item, item)
            result[name] = item
        return result

    def _convert_query(self, query):
        """Convert query values when is defined a converter"""
        result = query.__class__(query)

        # check mandatory parameters
        required = set(["begin", "end"])
        sample = [result.get(k) for k in required]

        if not any(sample):
            # user do not provide 'begin' boundary
            # we need to inspect repositoy
            stats = self.stats or self._inspect_repository()
            for k in required:
                result[k] = stats.get(k) and parse_arrow(stats[k])

        # convert values only when is defined for key
        for label in set(self.CONVERTER.keys()).intersection(result):
            # create 'item' in local stack.
            # 'item' is the convention name for converter expressions.
            item = result[label]
            if item is None:
                continue

            # broadcast same item into many names using converter expressions
            for name, exp in self.CONVERTER[label]:
                result[name] = eval(exp)

        # update with default values form class
        soft(result, **self.DEFAULT_QUERY.get(result["klass"], {}))
        soft(result, **self.DEFAULT_QUERY["default"])

        return result

    def _get_boundaries(self, query):
        return query["key1"], query["key2"]

    # ------------------------------------------------------
    # Stream handling
    # ------------------------------------------------------

    def _new_stream(self, query, mode="r"):
        """Creates a new SparseFile from query specs."""

        # safe mode for opening historical files
        mode = {"w": "wt", "r": "rt"}.get(mode, mode)

        factory = self.FACTORY.get(query["klass"], self.DEFAULT_FACTORY)
        stream = factory(
            query,
            mode,
            repository=self,
            allow_overwriting=self.allow_overwriting,
        )
        return stream

    # ------------------------------------------------------
    # Boundary handling
    # ------------------------------------------------------
    def _boundary_clusters(self, *q, **query):
        left = right = None
        for path, info in self._get_clusters(*q, **query):
            left = left or info
            right = info
        return left, right

    def _find_clusters(self, query):
        raise NotImplementedError(r"must be implemented")

    # ------------------------------------------------------
    # REView ....
    # ------------------------------------------------------

    def check_sanity(self, max_elements=-1, max_time=600):
        """Performs sanity tasks for a period of time or maximum of elements"""

    def _apply_aliases(self, query):
        for k, v in list(query.items()):
            query[k] = self.ALIASES.get(k, {}).get(v, v)

    def _get_path(self, query, mode="r", build=False, root=None, **kw):
        """*Get the path of a cluster based on query and mode.*"""
        # update query params
        # data = soft(query, **self.DEFAULT_QUERY)
        query.update(kw)

        # we need a 2nd converter call to convert parameters
        # related with 'begin', 'end' in the 1st writing.
        data = self._convert_query(query)

        # build path
        fmt = self.PATH.get(data["klass"]) or self.PATH["default"]
        path = fmt.format(**data)
        root = root or self.journal
        if mode in ("w", "wt"):
            path = os.path.join(root, path)
            if build:
                dirname, name = os.path.split(path)
                os.makedirs(dirname, exist_ok=True)
        else:
            path = os.path.join(self.root, path)

        return data, path


# ------------------------------------


class DateSparseFile(SparseFile):
    """A sparse file organized by date as key."""

    ENCODER = {"default": [date_normal, short_float]}  # decoders by klass
    DECODER = {"default": [parse_arrow, float]}  # encoders by klass

    def _get_delta(self, **query):
        delta = timeframe2delta(query["timeframe"], dict)
        return delta

    def _get_boundary(self, key):
        delta = self._delta
        assert delta
        unit = list(delta.keys())[0]

        if isinstance(key, datetime):
            key = Arrow.fromtimestamp(key.timestamp())

        assert isinstance(key, Arrow)

        # [) bounds
        return  key.span(unit)

    def _set_boundary(self, key):
        self._bound_left, self._bound_right = self._get_boundary(key)

    def _shift_keys(self, key, delta):
        """Default method for moving keys based on offset.
        Other subclassses may use different aritmetic.
        """
        return key and key.shift(**delta)


class DateRepository(Repository):
    DEFAULT_FACTORY = DateSparseFile

    PATH = {
        "default": "{klass}/{date1}/{time1}-{time2}.{timeframe}.{fmt}.{ext}",
    }
    supdate(
        Repository.DEFAULT_QUERY,
        {
            "default": {
                "timeframe": "1d",
            },
        },
    )

    Repository.ALIASES.update(
        {
            "trades": "trade",
        }
    )
    """A repository Factory based on date."""

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self._add_patterns(
            # bar.1s/20180903/070000-080000.1h.xz
            r"""(?imux)
            (?P<klass_name>[^./-]+)[^./-]
            (?P<sub>[^./-]+)[^./-]

            (?P<date1>(?P<year1>\d{4})-?(?P<month1>\d{2})-?(?P<day1>\d{2}))(\.|/)
            (?P<time1>(?P<hour1>\d{2}):?(?P<min1>\d{2}):?(?P<sec1>\d{2})(\.(?P<usec1>\d+))?)(\.|/|-)
            (?P<time2>(?P<hour2>\d{2}):?(?P<min2>\d{2}):?(?P<sec2>\d{2})(\.(?P<usec2>\d+))?)(\.|/|-)

            #?P<timeframe>\d+[smhd])(\.|/-)
            ((?P<fmt>(csv))(\.|/|-))?

            (?P<ext>[^.]+)
            $
            """,
        )

    def _get_boundaries(self, query):
        query.setdefault("date2", query["date1"])  #: in missing case
        query["key1"] = dt1 = "{date1}-{time1}".format_map(query)
        query["key2"] = dt1 = "{date2}-{time2}".format_map(query)

        begin = parse_arrow(dt1)
        end = parse_arrow(dt2)
        return begin, end


class HistoricalFile_Review_Delete(SparseFile):
    """Represent a File in the Repository."""

    DATE_FORMAT = "%Y%m%d-%H%M%S"
    DECODER = {
        "bar": [Date, Float, Float, Float, Float, Float],
        "depth": [
            Date,
        ],  # TODO: implement
        "tick": [
            Date,
        ],  # TODO: implement
    }
    ENCODER = {
        "bar": [
            date_normal,
            item_normal,
            item_normal,
            item_normal,
            item_normal,
            item_normal,
        ],
        "depth": [
            Date,
        ],  # TODO: implement
        "tick": [
            date_with_miliseconds,
            item_normal,
            item_normal,
            item_normal,
            item_normal,
            item_normal,
        ],  # TODO: implement
    }  # encoders by klass

    """
    """

    def _encode(self, record):
        """encode a record to be written into cluster"""
        line = f"{(','.join([self._encoders[i](item) for i, item in enumerate(record)]))}\n"
        return line

    def _decode(self, row):
        """Decode a line to extract the record stored in the line"""
        record = [self._decoders[i](value) for i, value in enumerate(row.split(","))]
        return record

    def __init__(self, query, mode, *args, **kw):
        """
        query may contains:

        {'ext': 'xz',
        'cmp': 'xz',
        'fmt': 'csv',
        'handler': 'bar',
        'kind': None,
        'klass': 'bar',
        'local_symbol': 'ESM9',
        'provider': 'ib'}


        """
        super().__init__(query, mode, *args, **kw)

        # self.timeframe = timeframe2delta(query.get('timeframe', '1s'))
        self.delta = timeframe2delta(query.get("timeframe") or "1s")

    def _boundary_clusters(self):
        q = dict(
            [
                (k, v)
                for k, v in self.query.items()
                if k in ("provider", "klass", "local_symbol", "timeframe", "ext")
            ]
        )

        return self.repository._boundary_clusters(**q)


class HistoricalRepository_Review_Delete(Repository):
    """
    - Cluster size is set to 3600 records by design. This number can be modified
    - Using 1s timeframe:
       - 1 day will need 24 clusters.
       - 1 months around 500 clusters
       - 1 year 5760 clusters

    Typical compressed size using 'xz' format.

    Every time a 3rd party wants to write a file:

    - A cluster is created, with the whole range (dates) to cover in the journal folder.
    - Wait until 1st 'record' is written.
    - Dumps from original cluster all the data to the new one until date of new record
    - NOTE: wrtiting must be sequential
    - Now both cursors are synchronized
    - try to get the next record from original.
    - Is date match: check all fields match. Raise an exception otherwise.
    - Is orignal date is higher just ignore.
    - Write record into journal
    - Continue until writting channel:
      1. is closed, then dump the rest of the original cluster in journal until end and stop
      2. overpass the date for current cluster
    - then close and move journal cluster to repository
    - open a new cluster and repeat the same process from the begining


    """

    # Just to indicate the type or options that a query parameters can be
    PARAMS = OrderedDict(
        provider=["ib"],
        local_symbol=str,
        klass=["bar", "depth", "tick"],
        begin="date",
        end="date",
        timeframe=["1s"],
        ext=["xz"],
        cmp=["xz"],
        fmt=["csv"],
    )
    CLUSTER_SIZE = {
        "1s": 3600 * 24,  #  1s * 3600 * 24 : full day
        "10m": 24 * 60 / 10 * 5 * 20,  # a full month roughtly
    }

    DEFAULT_QUERY = {
        "pkey": 0,
        "provider": "ib",
        "fmt": "csv",
        "ext": "xz",
        "cmp": "xz",
    }
    # Note: all params must be supplied in query (don't use None as defaults)
    PATH = "{provider}/{local_symbol}/{klass}/{date1}/{time1}.{time2}.{timeframe}.{ext}"
    SANITY = "{provider}/{local_symbol}/{klass}/{timeframe}.{ext}"

    # {
    # '1s' : 3600 * 100,
    # '1m' : 3600 * 10,
    # '30m': 3600,
    # }
    DEFAULT_TIMEFRAME = "1s"

    PARSER = dict(Repository.PARSER)
    PARSER.update(begin=Date, end=Date)

    def __init__(self, root, inbox=None, done=None, *args, **kw):
        """
        patterns match criteria:

        'local_symbol': 'ESM9' # instrument local symbol
        'fmt': 'csv'           # internal format data, default: csv
        'cmp': 'xz'            # compression used in file, default: None
        'handler': 'bar'       # handler to deal with each record in file
        'ext': None            # related with ext

        others:

        'date1' ('year1', 'month1', 'day1')
        'time1' ('hour1', 'min1', 'sec1', 'usec1')

        'timeframe' : '1s'     # timeframe when apply (e.g. historical bars)
        'provider'  : 'ib'     # data provider


        """
        super().__init__(root, *args, **kw)
        self.ALIASES.setdefault("handler", dict()).update(
            {
                "tick-size": "tick-mixed",
            }
        )

        self.inbox = dict()  # label : path
        if isinstance(inbox, dict):
            self.inbox = inbox
        elif isinstance(inbox, str):
            self.inbox["user-defined"] = inbox
        elif inbox is None:
            self.inbox["default"] = expandpath(os.path.join(self.root, "__inbox__"))

        for label, path in self.inbox.items():
            os.makedirs(path, exist_ok=True)

        self._add_patterns(
            # ib/ESU8/bar/20180903/070000-080000.1s.xz
            r"""
            (?P<provider>[^./]+)(\.|/|-)
            (?P<local_symbol>[^./]+)(\.|/|-)
            (?P<klass>[^./]+)(\.|/|-)
            (?P<date1>(?P<year1>\d{4})-?(?P<month1>\d{2})-?(?P<day1>\d{2}))(\.|/)
            (?P<time1>(?P<hour1>\d{2}):?(?P<min1>\d{2}):?(?P<sec1>\d{2})(\.(?P<usec1>\d+))?)(\.|/|-)
            (?P<time2>(?P<hour2>\d{2}):?(?P<min2>\d{2}):?(?P<sec2>\d{2})(\.(?P<usec2>\d+))?)(\.|/|-)

            (?P<timeframe>\d+[smhd])(\.|/-)
            (?P<ext>[^.]+)
            $
            """,
            # ib/ESU8/bar/1s/20180903/070000-080000.xz
            r"""
            (?P<provider>[^./]+)(\.|/|-)
            (?P<local_symbol>[^./]+)(\.|/)
            (?P<klass>[^./]+)(\.|/)

            (?P<timeframe>\d+[smhd])(\.|/)

            (?P<begin>
              (?P<date1>
                  (?P<year1>\d{4})-?(?P<month1>\d{2})-?(?P<day1>\d{2})
              )-?
              (?P<time1>
              (?P<hour1>\d{2}):?(?P<min1>\d{2}):?(?P<sec1>\d{2})(\.(?P<usec1>\d+))?
              )
            )
            \.

            (?P<end>
              (?P<date2>
                  (?P<year2>\d{4})-?(?P<month2>\d{2})-?(?P<day2>\d{2})
              )-?
              (?P<time2>
              (?P<hour2>\d{2}):?(?P<min2>\d{2}):?(?P<sec2>\d{2})(\.(?P<usec2>\d+))?
              )
            )
            \.

            (?P<ext>[^.]+)
            $
            """,
            # ib/ESU8/bar/20180903-070000.20180903-080000.1s.xz
            r"""
        (?P<provider>[^./]+)(\.|/|-)
        (?P<local_symbol>[^./]+)(\.|/)
        (?P<klass>[^./]+)(\.|/)

        (?P<begin>
          (?P<date1>
              (?P<year1>\d{4})-?(?P<month1>\d{2})-?(?P<day1>\d{2})
          )-?
          (?P<time1>
          (?P<hour1>\d{2}):?(?P<min1>\d{2}):?(?P<sec1>\d{2})(\.(?P<usec1>\d+))?
          )
        )
        \.

        (?P<end>
          (?P<date2>
              (?P<year2>\d{4})-?(?P<month2>\d{2})-?(?P<day2>\d{2})
          )-?
          (?P<time2>
          (?P<hour2>\d{2}):?(?P<min2>\d{2}):?(?P<sec2>\d{2})(\.(?P<usec2>\d+))?
          )
        )
        \.

        (?P<timeframe>\d+[smhd])(\.|/)
        (?P<ext>[^.]+)
        $
        """,
            # ib/ESU8/bar/1s/20180903-070000.20180903-080000.xz
            r"""
        (?P<provider>[^./]+)(\.|/|-)
        (?P<local_symbol>[^./]+)(\.|/)
        (?P<klass>[^./]+)(\.|/)

        (?P<timeframe>\d+[smhd])(\.|/)

        (?P<begin>
          (?P<date1>
              (?P<year1>\d{4})-?(?P<month1>\d{2})-?(?P<day1>\d{2})
          )-?
          (?P<time1>
          (?P<hour1>\d{2}):?(?P<min1>\d{2}):?(?P<sec1>\d{2})(\.(?P<usec1>\d+))?
          )
        )
        \.

        (?P<end>
          (?P<date2>
              (?P<year2>\d{4})-?(?P<month2>\d{2})-?(?P<day2>\d{2})
          )-?
          (?P<time2>
          (?P<hour2>\d{2}):?(?P<min2>\d{2}):?(?P<sec2>\d{2})(\.(?P<usec2>\d+))?
          )
        )
        \.

        (?P<cmp>[^.]+)
        $
        """,
            # NT8-TWS bridge service
            # NQM0.tick-price.20200605
            # NQM0.tick-price.csv.20200605
            # NQM0.tick-price.csv.20200605.xz
            # NQM0.tick-mixed.csv.20200605.xz
            # M6EM0.market-depth.csv.20200611.xz
            # ESM0.historical-data.csv.20200611.xz
            r"""
        (?P<provider>[^./]+)(\.|/|-)
        (?P<local_symbol>[^./]+)(\.|/|-)
        (?P<handler>[^./]+)(\.|/|-)
        ((?P<fmt>(csv))(\.|/|-))?
        (?P<date1>(?P<year1>\d{4})-?(?P<month1>\d{2})-?(?P<day1>\d{2}))
        ((\.|/)((?P<cmp>(xz))))?
        $
        """,
            # ESM9.bar
            # ESM9.bar.csv
            # ESM9.bar.csv.xz
            r"""
        (?P<provider>[^./]+)(\.|/|-)
        (?P<local_symbol>[^./]+)(\.|/)
        (?P<klass>(bar))
        ((\.|/)(?P<fmt>(csv)))?
        ((\.|/)((?P<cmp>(xz))))?
        $
        """,
        )

        self.done = done or os.path.join(self.root, "..", "done")

        # importing files
        # regexp : data type
        # self.import_regexp = {
        # NQM0.tick-price.csv.20200605.xz
        # r'(?P<local_symbol>[^./]+)(\.|/)(?P<klass>[^./]+)(\.|/)(?P<fmt>csv)(\.|/)(?P<date>\d+)(\.|/)(?P<ext>.+)$': 'ticker',

        # ESM9.bar.csv
        # r'(?P<local_symbol>[^./]+)(\.|/)(?P<klass>(bar))(\.|/)((?P<kind>(csv))(\.|/))?(?P<ext>(xz|csv))$': 'bar',

        # r'/(?P<symbol>[^/]+?)\.(?P<ext>csv)$',
        # r"/(?P<symbol>[^/]+?)\.price\.(?P<begin>\d+-\d+-\d+)\.?P<end>\d+-\d+-\d+)\.csv\.(?P<ext>%(ext)s)$",
        # r"/(?P<symbol>[^/]+?)\.csv\.(?P<begin>\d+-\d+-\d+)\.(?P<end>\d+-\d+-\d+)\.(?P<ext>%(ext)s)$",
        # }

    def check_sanity(self, inbox=None, max_elements=-1, max_time=600):
        # infinite loop by restaring generator
        t0 = time.time()
        for request in self.next_query(
            round_robin(
                # self._review_layout(),
                # self._explore_review(),
                # self.import_csv(),
                self.import_ticks(),
                restart_exahusted=True,
            )
        ):
            if max_elements > 0 or time.time() - t0 < max_time:
                max_elements -= 1
            else:
                break  # max lmit reached
        else:
            foo = 1  # task queue empty
        foo = 1

    def _new_stream(self, query, mode="rt"):
        """Provide a IO instance that handle access to repository
        for reading or writing.

        query  may contains:

        {'ext': 'csv',
        'cmp': 'xz',
        'fmt': 'csv',
        'handler': 'bar',
        'kind': None,
        'klass': 'bar',
        'local_symbol': 'ESM9',
        'provider': 'ib'}


        - [ ] usually get the lower timetrame that is can multiply to reach required timeframe
        - [ ] can also *condense* the values and store for faster access (optional)


        - It also rebuild the necessary timeframes if doesn't exist yet.

        """
        # safe mode for opening historical files
        mode = {"w": "wt", "r": "rt"}.get(mode, mode)
        return HistoricalFile(
            query, mode, repository=self, allow_overwriting=self.allow_overwriting
        )

    def _find_clusters(self, sort=False, *q, **query):
        """Find clusters in repository disk that match some criteria.

        TODO: move to base class
        """
        if sort:
            result = [o for o in self._fileiter(*q, **query)]
            # result.sort(key=lambda x: x[1]['begin'])  # by date
            result.sort(key=lambda x: x[0])  # by name
        else:
            result = self._fileiter(*q, **query)

        for o in result:
            yield o

    # -------------------------------------------------------
    # Specific method for HistoricalRepository
    # -------------------------------------------------------

    def _get_cluster_report(self, *q, **query):
        result = dict(n_clusters=0, disk_size=0, files=[])
        for _, info in self._get_clusters(*q, **query):
            result["n_clusters"] += 1
            result["disk_size"] += info["disk_size"]
            result["files"].append(info["abspath"])

        return result

    def _get_clusters(self, *q, **query):
        """Get involved clusters (sorted) for the given query."""
        if q:
            q = dict(q[0])
            q.update(query)
        else:
            q = query

        # q.__class__ = Query  # bless with Query
        q = Query(q)
        q.soft(self.DEFAULT_QUERY)

        # TODO: unify keys with base repository
        # TODO: key1, key21, key22 = date1, time1, time2
        query = self._convert_query(q)
        date1 = query.get("date1", "000000")
        date2 = query.get("date2", "999999")
        time1 = query.get("time1", "000000")
        time2 = query.get("time2", "999999")
        begin = query.get("begin", f"{date1}-{time1}")
        end = query.get("end", f"{date2}-{time2}")

        for path, info in self._find_clusters(sort=True, **q):
            _begin = info.get("_begin", f"{info['date1']}-{info['time1']}")
            _end = info.get("_end", f"{info['date1']}-{info['time2']}")

            if not (_begin >= end or _end < begin):
                info["_end"] = _end
                info["end"] = Date(info["_end"])

                info["_begin"] = _begin
                info["begin"] = Date(info["_begin"])

                yield os.path.join(self.root, path), info

    def _boundary_clusters(self, *q, **query):
        left = right = None
        for path, info in self._get_clusters(*q, **query):
            left = left or info
            right = info
        return left, right

    def boundaries(self, *q, **query):
        left, right = self._boundary_clusters(*q, **query)

        #  open and get the keys from file
        if right:
            record = None
            for record in xz.open(right["abspath"], "rt"):
                pass
            if record:
                right = Date(record[0])

        if left:
            record = None
            for record in xz.open(left["abspath"], "rt"):
                break
            if record:
                left = Date(record[0])

        return left, right

    def _fileiter(self, *q, **query):
        if q:
            q = dict(q[0])
            q.update(query)
        else:
            q = query

        q = Query(q)
        q.soft(begin="*", end="*", date1="*", date2="*", time1="*", time2="*")
        q.soft(self.DEFAULT_QUERY)
        for k, v in list(q.items()):
            q[k] = _prepare_test_regext(wildcard=v)

        # make a 1st search
        for path, info in fileiter(
            self.root, regexp=self.patterns, info="d", relative=True
        ):

            for k, test in q.items():
                if k in info and not _find_match(info[k], test):
                    break
            else:
                info["path"] = path
                info["abspath"] = abspath = os.path.join(self.root, path)
                info["disk_size"] = os.stat(abspath).st_size
                info = Query(info)
                yield path, info
        foo = 1

    def _review_layout(self):
        """Restructure cluster layout when designer changes storage criteria.

        - [x] check that cluster size (dates) must be preserved, is just a cluster reallocation
        - [x] parse old name, build the next one and os.renames()
        """
        q = Query(begin="*", end="*", timeframe="*")
        t0 = time.time()
        for i, (path, query) in enumerate(self._fileiter(q)):
            query.soft(self.DEFAULT_QUERY)
            new_path = self.PATH.format(**query)
            if new_path != path:
                old = os.path.join(self.root, path)
                new = os.path.join(self.root, new_path)
                os.renames(path, new)

            yield NOP

            if not (i % 50):
                t1 = time.time()
                if t1 - t0 > 0.25:
                    yield NOP
                    t0 = t1
        foo = 1

    def _explore_review(self):
        "Explore REV files in __review__ folder to be processed"

        def data_files():  # "Iterare over REV files "
            "Iterare over REV files in all __review__'s"
            top = self.review
            regexp = [
                r"(?P<local_symbol>[^./]+)(\.|/)(?P<klass>[^./]+)(\.|/)(?P<timeframe>[^./]+)(\.|/)(?P<ext>rev)$",
            ]
            for path, info in fileiter(top, regexp, info="d"):
                debug(f"Analyzing: '{path}'")
                yield path, info

        def process(request):  # process a whole file
            def analyze_file(file):  # get REV info
                sample = file.read(1024)
                sniffer = csv.Sniffer()
                dialect = sniffer.sniff(sample)
                has_header = sniffer.has_header(sample)
                file.seek(0)
                return dialect, has_header

            path, query = request
            with open(path, "rt") as file:
                dialect, has_header = analyze_file(file)
                reader = READERS.get(query["ext"], csv.reader)(
                    sorted_lines(file), dialect
                )

                # open output file
                with self.open(mode="wt", **query) as output:
                    # get headers
                    if has_header:
                        for headers in reader:
                            break
                    else:
                        headers = None
                    # TODO: use headers ...
                    # headers = self.HEADERS.get(query.get('klass', 'bar'), headers)

                    # compute progress
                    # TODO: use delta <0 delta > 0 for reversing
                    self.start_progress(file, reverse=False)

                    # iterate over the whole file
                    # REV sanity is simply trying to import the file again ...
                    # TODO: check if we can use simply "import" feaure from repository to do this
                    for i, row in enumerate(reader):
                        record = HistoricalFile._decode(row)
                        output.write_record(record)
                        if not i % 2000:
                            if self.nice():
                                eta, remain = self.progress(file)
                                info(
                                    f"Writing: {i} records on {query['local_symbol']}: ETA: {eta}, remain: {remain}"
                                )
                                yield NOP  # be nice and return control

            # file processed, post-action here
            warn(f"Removing REV file: {path}")
            os.unlink(path)
            # - End -

        # main loop
        for request in data_files():
            for request in process(request):
                yield request
        foo = 1

    # -------------------------------------------------------
    # Method to be called from cli-api
    # -------------------------------------------------------

    def import_csv(self, inbox=None, progress_each=20000, **kw):
        "Explore CSV files in inbox to be processed"
        inbox = inbox or self.inbox
        if isinstance(inbox, str):
            inbox = [inbox]

        if isinstance(inbox, list):
            inbox = enumerate(inbox)
        elif isinstance(inbox, dict):
            inbox = inbox.items()

        def data_files():  # "Iterare over CSV files "
            "Iterare over CSV files in all inbox's"
            for label, top in inbox:
                top = expandpath(top)
                regexp = [
                    r"(?P<local_symbol>[^./]+)(\.|/)(?P<klass>[^./]+)(\.|/)(?P<ext>csv)$",
                    # r'/(?P<symbol>[^/]+?)\.(?P<ext>csv)$',
                    # r'/(?P<symbol>[^/]+?)\.(?P<ext>csv)$',
                    # r"/(?P<symbol>[^/]+?)\.price\.(?P<begin>\d+-\d+-\d+)\.?P<end>\d+-\d+-\d+)\.csv\.(?P<ext>%(ext)s)$",
                    # r"/(?P<symbol>[^/]+?)\.csv\.(?P<begin>\d+-\d+-\d+)\.(?P<end>\d+-\d+-\d+)\.(?P<ext>%(ext)s)$",
                ]

                for path, info in fileiter(top, regexp, info="d"):
                    debug(f"Analyzing: '{path}'")
                    yield path, info

        def process(request):  # process a whole file
            try:

                def analyze_file(file):  # get CSV info
                    sample = file.read(1024)
                    sniffer = csv.Sniffer()
                    dialect = sniffer.sniff(sample)
                    has_header = sniffer.has_header(sample)
                    file.seek(0)
                    return dialect, has_header

                def get_timeframe(file, reader):
                    # get timeframe from file
                    rows = list()
                    for i, row in enumerate(reader):
                        record = HistoricalFile._decode(row)
                        rows.append(record)
                        if i >= 1:
                            break

                    file.seek(0, os.SEEK_SET)
                    delta = rows[-1][0] - rows[0][0]
                    return delta2timeframe(delta), delta

                path, query = request
                with open(path, "rt") as file:
                    dialect, has_header = analyze_file(file)
                    reader = READERS.get(query["ext"], csv.reader)(file, dialect)

                    if "timeframe" not in query:
                        query["timeframe"], query["delta"] = get_timeframe(file, reader)

                    if query["delta"].total_seconds() < 0:
                        # reopen file in reverse order
                        reader = READERS.get(query["ext"], csv.reader)(
                            reversed_lines(file), dialect
                        )
                    else:
                        reader = READERS.get(query["ext"], csv.reader)(
                            direct_lines(file), dialect
                        )

                    with self.open(mode="wt", **query) as output:
                        # get headers
                        if has_header:
                            for headers in reader:
                                break
                        else:
                            headers = None
                        # TODO: use headers ...
                        # headers = self.HEADERS.get(query.get('klass', 'bar'), headers)

                        # compute progress
                        # TODO: use delta <0 delta > 0 for reversing
                        self.start_progress(file, reverse=True)

                        # iterate over the whole file
                        for i, row in enumerate(reader):
                            record = HistoricalFile._decode(row)
                            output.write_record(record)
                            if not i % progress_each:
                                if self.nice():
                                    progress = self.progress(file)
                                    info(
                                        f"Writing: {i} records on {query['local_symbol']}: {progress}"
                                    )
                                    yield file, progress  # be nice and return control

                # file processed, post-action here
                # move file to processed files
                new = os.path.join(self.done, os.path.basename(path))
                new = expandpath(new)
                debug(f"moving '{path}' to DONE folder: {new}")
                os.makedirs(os.path.dirname(new), exist_ok=True)
                os.rename(path, new)
                # - End -
            except Exception as why:
                # move to unknown
                new = os.path.join(self.unknown, os.path.basename(path))
                msg = f"ERROR: moving '{path}' to UNKOWN folder: {new}"
                print(msg)
                exception(msg)
                os.makedirs(os.path.dirname(new), exist_ok=True)
                os.rename(path, new)

        # main loop
        for request in data_files():
            for request in process(request):
                yield request

    def import_ticks(self, inbox=None, progress_each=20000, **kw):
        "Explore CSV files in inbox to be processed"
        inbox = inbox or self.inbox
        if isinstance(inbox, str):
            inbox = [inbox]

        if isinstance(inbox, list):
            inbox = enumerate(inbox)
        elif isinstance(inbox, dict):
            inbox = inbox.items()

        def data_files():  # "Iterare over CSV files "
            "Iterare over CSV tick-files files in all inbox's"
            for label, top in inbox:
                top = expandpath(top)
                regexp = {
                    # NQM0.tick-price.csv.20200605.xz
                    r"(?P<local_symbol>[^./]+)(\.|/)(?P<klass>[^./]+)(\.|/)(?P<fmt>csv)(\.|/)(?P<date>\d+)(\.|/)(?P<ext>.+)$": "ticker"
                    # r'/(?P<symbol>[^/]+?)\.(?P<ext>csv)$',
                    # r'/(?P<symbol>[^/]+?)\.(?P<ext>csv)$',
                    # r"/(?P<symbol>[^/]+?)\.price\.(?P<begin>\d+-\d+-\d+)\.?P<end>\d+-\d+-\d+)\.csv\.(?P<ext>%(ext)s)$",
                    # r"/(?P<symbol>[^/]+?)\.csv\.(?P<begin>\d+-\d+-\d+)\.(?P<end>\d+-\d+-\d+)\.(?P<ext>%(ext)s)$",
                }

                for path, key, info in fileiter(top, regexp, info="d"):
                    debug(f"Analyzing: '{path} : type: {key}'")
                    yield path, key, info

        def process(request):  # process a whole file
            try:

                def analyze_file(file):  # get CSV info
                    sample = file.read(1024)
                    sniffer = csv.Sniffer()
                    dialect = sniffer.sniff(sample)
                    has_header = sniffer.has_header(sample)
                    file.seek(0)
                    return dialect, has_header

                def get_timeframe(file, reader):
                    # get timeframe from file
                    rows = list()
                    for i, row in enumerate(reader):
                        record = HistoricalFile._decode(row)
                        rows.append(record)
                        if i >= 1:
                            break

                    file.seek(0, os.SEEK_SET)
                    delta = rows[-1][0] - rows[0][0]
                    return delta2timeframe(delta), delta

                path, key, query = request

                with xopen(path, "rt", encoding="utf-8", **query) as file:
                    dialect, has_header = analyze_file(file)
                    reader = READERS.get(query["ext"], csv.reader)(file, dialect)

                    if "timeframe" not in query:
                        query["timeframe"], query["delta"] = get_timeframe(file, reader)

                    if query["delta"].total_seconds() < 0:
                        # reopen file in reverse order
                        reader = READERS.get(query["ext"], csv.reader)(
                            reversed_lines(file), dialect
                        )
                    else:
                        reader = READERS.get(query["ext"], csv.reader)(
                            direct_lines(file), dialect
                        )

                    with self.open(mode="wt", **query) as output:
                        # get headers
                        if has_header:
                            for headers in reader:
                                break
                        else:
                            headers = None
                        # TODO: use headers ...
                        # headers = self.HEADERS.get(query.get('klass', 'bar'), headers)

                        # compute progress
                        # TODO: use delta <0 delta > 0 for reversing
                        self.start_progress(file, reverse=True)

                        # iterate over the whole file
                        for i, row in enumerate(reader):
                            record = HistoricalFile._decode(row)
                            output.write_record(record)
                            if not i % progress_each:
                                if self.nice():
                                    progress = self.progress(file)
                                    info(
                                        f"Writing: {i} records on {query['local_symbol']}: {progress}"
                                    )
                                    yield file, progress  # be nice and return control

                # file processed, post-action here
                # move file to processed files
                new = os.path.join(self.done, os.path.basename(path))
                new = expandpath(new)
                debug(f"moving '{path}' to DONE folder: {new}")
                os.makedirs(os.path.dirname(new), exist_ok=True)
                os.rename(path, new)
                # - End -
            except Exception as why:
                # move to unknown
                new = os.path.join(self.unknown, os.path.basename(path))
                msg = f"ERROR: moving '{path}' to UNKOWN folder: {new}"
                print(msg)
                exception(msg)
                os.makedirs(os.path.dirname(new), exist_ok=True)
                os.rename(path, new)

        # main loop
        for request in data_files():
            for request in process(request):
                yield request

    def explore(self, inbox=None, progress_each=20000, **kw):
        """Explore given inbox folders to process files

        - Files that match some regular expressions may provide the parsing method
        - Else, we must analize format and guess type of file.


        """
        for progress in self.next_query(
            round_robin(
                # self._review_layout(),
                # self._explore_review(),
                # self.import_csv(),
                self._explore_external_files(
                    inbox=inbox, progress_each=progress_each, **kw
                ),
                restart_exahusted=False,
            )
        ):
            yield progress
        foo = 1

    def _get_csv_info(self, file, query):
        sample = file.read(1024)
        file.seek(0)

        sniffer = csv.Sniffer()
        dialect = query["dialect"] = sniffer.sniff(sample)
        self.has_header = sniffer.has_header(sample)

        query["delim"], query["skipinitialspace"] = sniffer._guess_delimiter(
            sample, None
        )
        # query['quotechar'], query['doublequote'] = sniffer._guess_delimiter(sample, None)

        query["reader"] = READERS.get(query["ext"], csv.reader)(file, dialect)

        if self.has_header:
            for query["columns"] in query["reader"]:
                break
        else:
            # try to guess columns names
            pass

        # try to guess the 'date' or the 'key' columns

        if "timeframe" not in query:
            query["timeframe"], query["delta"] = get_timeframe(file, reader)

        if query["delta"].total_seconds() < 0:
            # reopen file in reverse order
            reader = READERS.get(query["ext"], csv.reader)(
                reversed_lines(file), dialect
            )
        else:
            reader = READERS.get(query["ext"], csv.reader)(direct_lines(file), dialect)

        return query

    def _explore_external_files(
        self, inbox=None, regexp=None, progress_each=20000, **kw
    ):
        "mover a clase base"
        for query in self._find_files2(inbox, regexp):
            print(query)
            try:
                with xopen(mode="rt", encoding="utf-8", **query) as file:
                    reader = CSVHistorical(file, query)
                    # open the right storage virtual 'file'
                    # and select the handler function for the record
                    with self.open(mode="wt", **query) as output:
                        query["progress"] = self.start_progress(
                            file, reverse=reader.reverse
                        )
                        handler = output.write_record

                        # iterate over the whole file
                        for i, record in enumerate(reader):
                            handler(record)

                            if not i % progress_each:
                                if self.nice():
                                    progress = self.progress(file)
                                    info(
                                        f"Writing: {i} records on {query['local_symbol']}: {progress}"
                                    )
                                    yield query  # be nice and return control

                # file processed, post-action here
                # move file to processed files
                path = query["path"]
                new = os.path.join(self.done, os.path.basename(path))
                new = expandpath(new)
                debug(f"moving '{path}' to DONE folder: {new}")
                os.makedirs(os.path.dirname(new), exist_ok=True)
                os.rename(path, new)
                # - End -
            except Exception as why:
                tb = exception()
                # move to unknown
                path = query["path"]
                new = os.path.join(self.unknown, os.path.basename(path))
                msg = f"ERROR: moving '{path}' to UNKOWN folder: {new}"
                print("-" * 80)
                print(msg)
                print(tb)
                os.makedirs(os.path.dirname(new), exist_ok=True)
                os.rename(path, new)
                # create a file with error traceback for later inspection
                open(f"{new}.traceback", "w").write(tb)
                print("-" * 80)

    def _find_files2(self, inbox=None, regexp=None):
        "mover a clase base"
        inbox = inbox or self.inbox
        regexp = regexp or self.patterns

        if not isinstance(inbox, dict):
            inbox = dict(enumerate(inbox))

        for label, top in inbox.items():
            top = expandpath(top)

            for path, query in fileiter(top, regexp, info="d"):
                query = Query(query)
                query.soft(path=path)
                self._apply_aliases(query)
                debug(f"Find file: '{query}'")
                yield query


# ------------------------------------------------
# Exception classes
# ------------------------------------------------


class KeyStorageException(Exception):
    """Base of all Repository Exceptions"""


class JournalLocked(KeyStorageException):
    """Raised when a second agent tries to write inthe same journaling cluster"""


class OverwrittenError(KeyStorageException):
    """Raised when trying to overwriten an existin record that doesn't match with new one."""
