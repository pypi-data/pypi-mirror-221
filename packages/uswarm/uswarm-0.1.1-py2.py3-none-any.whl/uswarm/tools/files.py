"""Helpers for dealing with files.

CSV files
-----------------------


"""
import arrow
import os
import re
import time
import pickle
import yaml
import threading
import functools
import random

from abc import abstractmethod
from itertools import count

from functools import partial
from io import FileIO, StringIO

import lzma as xz
import pandas as pd

# from .calls import scall

DUMPERS = {
    ".yaml": (partial(yaml.dump, default_flow_style=False), "w"),
    ".pickle": (partial(pickle.dump, protocol=-1), "wb"),
}

LOADERS = {
    ".yaml": (partial(yaml.load, Loader=yaml.Loader), "r"),
    ".pickle": (pickle.load, "rb"),
}

ALIASES = {
    ".yml": ".yaml",
}

# ----------------------------------------------------------
# Handler same base files with different extensions
# ----------------------------------------------------------


def get_file_dates(basepath, extensions=None):
    extensions = LOADERS.keys() if extensions is None else extensions
    result = {}
    for ext in extensions:
        path = f"{basepath}{ext}"
        if os.access(path, os.F_OK):
            result[path] = os.stat(path).st_mtime
        else:
            result[path] = 0
    return result


def get_newest_file(basepath, extensions=None):
    dates = get_file_dates(basepath, extensions)
    older = max(dates.values())

    for path, updated in dates.items():
        if updated == older:
            return path


def load_newest_file(basepath, extensions=None):
    return load(get_newest_file(basepath, extensions))


# ----------------------------------------------------------
# Handler same base files with different extensions
# ----------------------------------------------------------


def dump(data, file):
    name, ext = os.path.splitext(file)
    func, mode = DUMPERS[ALIASES.get(ext, ext)]
    func(data, open(file, mode))


def load(file):
    name, ext = os.path.splitext(file)
    func, mode = LOADERS[ALIASES.get(ext, ext)]
    try:
        data = func(open(file, mode))
    except EOFError:
        data = None
    return data


# ----------------------------------------------------------
# Locks
# ----------------------------------------------------------


class iLock:
    def __init__(self, *args, **kw):
        pass

    def adquire_lock(self):
        pass

    def release_lock(self):
        pass

    def remove(self):
        pass


class FSLock(iLock):
    def __init__(self, lock_file=None, grace: int = 40000, *args, **kw):
        super().__init__(*args, **kw)
        self.lock_file = lock_file or f"/tmp/lock-file.{time.perf_counter_ns()}.lock"
        self.grace = grace

        t1 = time.perf_counter_ns()
        self.unique = f"{t1} {os.getpid()}\n"

    def adquire_lock(self):
        lock_file = self.lock_file
        t1 = time.perf_counter_ns()
        unique = self.unique
        while True:
            try:
                existing = open(lock_file, "r").read()
                if existing != unique:
                    t0 = int(existing)
                    while True:
                        t1 = time.perf_counter_ns()
                        if t0 - t1 < 0:
                            print(f"force unlock")
                            break
                        time.sleep(random.random() * 0.1)
                else:
                    break  # lock adquire
            except FileNotFoundError as why:
                pass
            except Exception as why:
                time.sleep(random.random() * 0.1)

            t1 += self.grace  # 40 ms
            unique = f"{t1} {os.getpid()}\n"
            open(lock_file, "w").write(unique)

        # lock adquire
        self.unique = unique

    def release_lock(self):
        os.unlink(self.lock_file)

    def remove(self):
        self.lock_file and os.unlink(self.lock_file)


class iRecordStorage:
    order_idx_columns = ["id", "key", "date"]
    order_field_columns = []

    PATTERN_REGEXP = {
        # MAIN: r"(?P<start>[\d-:]+)_(?P<end>[\d-:]+).csv.xz",
        # JOURNAL: 'r"_(?P<start>[\d-:]+)_(?P<end>[\d-:]+).csv"',
    }
    PATTERN_RENDER = {
        # MAIN:"{start}_{end}.csv.xz",
        # JOURNAL:"_{start}_{end}.csv",
    }
    # storage facctory.
    DEVICE_FACTORY = {
        # MAIN: Dataframe,  # is a fast-forward declaration.
        # JOURNAL: IncrementalCSV,
    }
    DEVICE_DEFAULTS = {
        # MAIN: {},
        # JOURNAL: {"mode": "a", "_use_lock_": False},
    }

    path: str

    def __init_subclass__(cls, **kwargs):
        """Auto-register all Resource classes."""
        super().__init_subclass__(**kwargs)

        cls.DEVICE_FACTORY[cls.__name__] = cls

    # --------------------------------------------------
    # Struct support
    # --------------------------------------------------
    def _build_structure(self, keys):
        indexes = []
        columns = []
        # has idx?
        keys = [x for x in keys]
        for idx in set(self.order_idx_columns).intersection(keys):
            indexes.append(idx)
            keys.remove(idx)

        assert indexes, "No index has been defined!"

        # fields in same as preferece order_field_columns
        for idx in set(self.order_field_columns).intersection(keys):
            columns.append(idx)
            keys.remove(idx)

        # add the rest of the fields sorted by name
        keys.sort()
        columns.extend(keys)
        if len(indexes) == 1:
            return indexes[0], columns
        return indexes, columns

    @abstractmethod
    def _create_struct_like(self, record: dict):
        """Create a struct mimic the given record structure."""

    # --------------------------------------------------
    # Reading support
    # --------------------------------------------------
    @abstractmethod
    def read_record(self):
        """Read a single record from storage."""

    @abstractmethod
    def read_delta(self):
        """Read a bunch or records (delta) from storage."""

    # --------------------------------------------------
    # Writting support
    # --------------------------------------------------
    @abstractmethod
    def write_record(self, record: dict):
        """Write a single record into storage"""

    @abstractmethod
    def write_delta(self, delta):
        """Write a bunch or records (delta) into storage"""

    # --------------------------------------------------
    # Storage support
    # --------------------------------------------------
    def commit(self):
        """Commit any pending data to the storage."""
        pass

    @abstractmethod
    def remove(self):
        """Delete instance from storage."""


class CSVFile(FileIO, iRecordStorage):
    """Support for reading CSV files.

    NOTE: It's recommended to use Dataframe class instead this one.
    """

    sep = ","
    casting = {
        "z": int,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.columns = []
        self.path = self.name

    # --------------------------------------------------
    # Iterator support
    # --------------------------------------------------
    def __iter__(self):
        return self.__next__()

    def __next__(self):
        try:
            while True:
                record = self.read_record()
                yield record
        except EOFError as why:
            pass  # finish iterator

    # --------------------------------------------------
    # Struct support
    # --------------------------------------------------
    def _create_struct_like(self, record: dict):
        """Create a struct mimic the given record structure."""
        index, columns = self._build_structure(record)
        if isinstance(index, list):
            self.columns.extend(index)
        else:
            self.columns.append(index)
        self.columns.extend(columns)
        # need to write the header line?

        if os.stat(self.name).st_size == 0:
            line = self.sep.join([str(k) for k in self.columns])
            line = bytes(f"{line}\n", "utf-8")
            self.write(line)

    def _analyze_header(self, header):
        """analyze the 1st line of a CSV heade file."""
        regexp = ["""(?P<name>[^",]+)"""]
        for reg in regexp:
            columns = [k.strip() for k in re.findall(reg, header)]
            if not columns:
                continue
            self.columns = [k for k in columns if k]
            assert self.columns, "file has no header!"
            # get sepatator
            header = header.replace(self.columns[0], "x")
            header = header.replace(self.columns[1], "x")
            m = re.match(r"x(?P<sep>[^x]+)x", header)
            self.sep = m.group(1)
            # TODO: strip sep and strip every field when reading?
            break

    # --------------------------------------------------
    # Reading support
    # --------------------------------------------------
    def read_record(self):
        if not self.columns:
            header = self.readline().decode("utf-8")
            self._analyze_header(header)
        line = self.readline().decode("utf-8").strip()
        if line:
            record = {}
            for i, value in enumerate(line.split(self.sep)):
                k = self.columns[i]
                record[k] = self.casting.get(k, str)(value)
            return record
        raise EOFError()

    # --------------------------------------------------
    # Storage support
    # --------------------------------------------------
    def remove(self):
        """Delete instance from storage."""
        super().remove()
        if not self.closed:
            self.close()
        os.path.exists(self.path) and os.unlink(self.path)

    # --------------------------------------------------
    # TODO: REVIEW
    # --------------------------------------------------
    def split(self, n=5, pattern="{basename}-{n}{ext}"):
        basename, ext = os.path.splitext(self.name)
        files = {}
        for n in range(n):
            filename = pattern.format(**locals())
            files[filename] = IncrementalCSV(filename, "w")


class IncrementalCSV(CSVFile):
    def __init__(self, *args, _use_lock_=True, **kwargs):
        super().__init__(*args, **kwargs)
        LOCK = FSLock if _use_lock_ else iLock
        self.lock = LOCK(f"{self.name}.lock", grace=60 * 10 ** 3)

    # --------------------------------------------------
    # Writting support
    # --------------------------------------------------
    def write_record(self, record: dict):
        if not self.columns:
            self._create_struct_like(record)

        line = self.sep.join([str(record[k]) for k in self.columns])
        line = bytes(f"{line}\n", "utf-8")
        self.write(line)

    def write_delta(self, delta):
        if delta.shape[0] <= 0:
            return
        if not self.columns:
            row = delta.iloc[0]
            record = row.to_dict()
            record[delta.index.name] = row.name
            self._create_struct_like(record)

        out = StringIO()
        delta.to_csv(out, header=False)
        raw = bytes(f"{out.getvalue()}", "utf-8")
        self.write(raw)
        foo = 1

    def write_record_safe(self, record: dict):
        if not self.columns:
            self._create_struct_like(record)
            # need to write the header line?
            self.lock.adquire_lock()
            if os.stat(self.name).st_size == 0:
                line = self.sep.join([str(k) for k in self.columns])
                line = bytes(f"{line}\n", "utf-8")
                self.write(line)
            # let the lock be re-adquired
            # so the 1st writer dumps header and 1st record

        line = self.sep.join([str(record[k]) for k in self.columns])
        line = bytes(f"{line}\n", "utf-8")
        try:
            self.lock.adquire_lock()
            self.write(line)
        finally:
            self.lock.release_lock()

    def write(self, line):
        """Overrride FileIO.write() method to use lock."""
        self.lock.adquire_lock()
        super().write(line)
        self.lock.release_lock()

    # --------------------------------------------------
    # Storage support
    # --------------------------------------------------
    def commit(self):
        """Commit any pending data to the storage."""
        self.flush()

    def remove(self):
        """Delete instance from storage."""
        super().remove()
        self.lock.remove()


def test_incremental_csv():
    filename = "/tmp/kk-incremental.csv"

    def greddy_writting(name, t1):

        t0 = time.time()
        time.sleep(t1 - t0)

        with IncrementalCSV(filename, mode="a") as f:
            for z in range(5):
                f.write_record_safe({"id": 1, "name": name, "z": z})
            foo = 1

    t0 = time.time() + 2
    for i in range(10):
        name = f"greedy-{i}"
        th = threading.Thread(
            name=name, target=functools.partial(greddy_writting, name, t0)
        )
        th.start()

    while th.is_alive():
        time.sleep(0.1)

    with CSVFile(filename, mode="r") as f:
        for record in f:
            print(f"record: {record}")

    with CSVFile(filename, mode="r") as f:
        f.split()

    print("-End-")


# ----------------------------------------------------------
# Fix Arrow and pandas.Timestamp YAML serialization
# ----------------------------------------------------------


def Arrow_representer(dumper, data):
    """Define the representer, responsible for serialization"""
    raw = str(data)
    return dumper.represent_scalar("!Arrow", raw)


yaml.add_representer(arrow.Arrow, Arrow_representer)


def Arrow_constructor(loader, node):
    """Arrow constructor"""
    value = loader.construct_scalar(node)
    # someNumber,sep,someString = value.partition("|")
    return arrow.get(value)


yaml.add_constructor("!Arrow", Arrow_constructor)

# -----


def pandas_timestamp_representer(dumper, data):
    """Define the representer, responsible for serialization"""
    raw = data.strftime("%Y%m%d-%H%M%S%z")
    return dumper.represent_scalar("!timestamp", raw)


yaml.add_representer(pd.Timestamp, pandas_timestamp_representer)


def pandas_timestamp_constructor(loader, node):
    """pd.timestamp constructor"""
    value = loader.construct_scalar(node)
    # someNumber,sep,someString = value.partition("|")
    return pd.to_datetime(value)


yaml.add_constructor("!timestamp", pandas_timestamp_constructor)


if __name__ == "__main__":
    test_incremental_csv()
