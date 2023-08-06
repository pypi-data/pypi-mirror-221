# from multiprocessing import Process as Fiber
# from threading import Thread as Fiber

import re
from typing import List, Set, Dict, Tuple, Optional, Union

import os
import sys
import itertools
from typing import Dict
from datetime import datetime, timedelta
from abc import abstractmethod


import arrow

import pandas as pd


from uswarm.tools import soft, fileiter, expandpath
from uswarm.tools.containers import opendf, savedf
from uswarm.tools.files import iRecordStorage, IncrementalCSV
from uswarm.tools.iterators import df_concat, df_glue, df_join

# --------------------------------------------------
# Log
# --------------------------------------------------
# from uswarm.tools.logs import logger
from uswarm.tools.logs import logger

log = logger(__name__)


# --------------------------------------------------
# Definitions
# --------------------------------------------------
def update_df(base, new, sanitize=True):
    if new is None:
        dirty = False
        df = base
    else:
        dirty = True
        if base is None:
            df = new
        else:
            df = pd.concat([base, new], copy=False, verify_integrity=False)

    if sanitize and isinstance(df, pd.DataFrame):
        # drop suplicated rows
        df = df[~df.index.duplicated(keep="first")]
        # sort df
        df.sort_index(inplace=True)
    return df, dirty


# --------------------------------------------------
# Dataframe
# --------------------------------------------------

MAIN = "main"
JOURNAL = "journal"


class Dataframe(iRecordStorage):
    """Dataframes manages data in rows usind pandas datafames under the hood.

    Main features are:

    - store data in plain cvs text format (compressed with xz by default).
    - allow to update internal dataframe with other pandas dataframes.
    - fast adding of new records avoiding pandas slow operations.
    - exposes internal dataframe handling internal merges and sort index when is needed.

    Due to performance issues adding new records on pandas dataframes we use a separate
    jounaling file to store the data as is received and rebuild the data when is required
    by an external agent.

    So the rules of thumb are:

    - Dataframe class holds devices at the same time: pandas df and IncrementalCSV.
    - Writting records goes to IncrementalCSV and feed memory delta cache.
    - Writing requires having the global dataframe lock so none can corrupt the storage.
    - Exposing dataframe rebuild pandas dataframe with the deltas cached in memory.
    - Saving (commit) Dataframe implies merging all data and removing journal file at the end.
    - Journal file acts as backup of all information received not commited.


    FINAL NOTES:

    assets:

    - all pd.df in different formats
    - created and loaded from disk on __init__()
       - load all PATTERN_REGEXP matching files
       - update self.meta[] from regexp.

    - there are some key conventions for assets: MAIN, JOURNAL
    - MAIN: get the *consolidated* df: cause join
       - self.df --> self.assets[MAIN]

    def write_delta(self, delta):
        dev = self.assets.get(JOURNAL) or self._new_df(JOURNAL)
        dev.write_delta(delta)
        self._dirty[JOURNAL] = True

    def commit(self):
        # Merge JOURNAL with MAIN and save result to disk.
        dev = self.assets.get(JOURNAL)
        if isinstance(dev, self.DEVICE_FACTORY[JOURNAL]):
            dev.close()

        self._load_df(JOURNAL)
        self._merge(JOURNAL, MAIN)
        self._save_df(MAIN)
        self._remove_df(JOURNAL)


    - sort assets by priority: from base to lastest journal
    - create new journal when is needed
    - commit should collapse them all before saving in MAIN format (typically '.xz')
    - modify low_level df disk methods:_new_df, _load_df, _save_df, _remove_df
    - modify _merge(source, target)
    - use _dirty as well

    Conclussion:

    - [ ] monotone crescend keys:
      - [ ] record or delta keys is assumed going monotone cresceding.

    - [ ] commit:
      - [ ] must retire *journal*
      - [ ] next writting attempt will open a new df
      - [ ] now we can join *main* and *journal* using whatever technic safely.

    - [ ] streaming:
      - [ ] streaming is locked until commit is done.

    - [ ] df property:
      - [ ] force commit and present a *snapshot* of the current cluster data.


    - [ ] _new_df:
      - [ ] find last used sequence.
      - [ ] next writing will create (sequence + 1)

    # ---------------------------

    - [x] set all meta data in df.attrs field
      - [ ] path:
        - [ ] remove()
        - [ ] _new_df()
        - [ ] _load_df()
        - [ ] _save_df()
        - [ ] _remove_df()

      - [ ] _dirty:
        - [ ] @df
        - [ ] write_record()
        - [ ] write_delta()
        - [ ] _load_df()
        - [ ] _save_df()
        - [ ] _remove_df()
        - [ ] _merge()
        - [ ] _save_df()

    - [ ] meta:
        - [ ] _save_df()


    - [ ] file clusters name contains sequence number as well.

          20220511-0050000_20220512-0050000.0000.csv
          20220511-0050000_20220512-0050000.0001.csv.gz

          or not

          20220511-0050000_20220512-0050000.csv
          20220511-0050000_20220512-0050000.csv.xz

    - [ ] define default meta-params per sequence or regexp 'd' matching (or lack of)
    - [ ]

    """

    # humand boundaries
    PATTERN_REGEXP = {
        # 20220511-0050000_20220512-0050000.csv.xz
        MAIN: r"(?P<root>.*?)(?P<start>[\d\-:]+)_(?P<end>[\d\-:]+).(?P<ext>csv)(?P<cmp>\.(xz|gz))$",
        # _20220511-0050000_20220512-0050000.csv
        # JOURNAL: r"(?P<root>.*?)_(?P<start>[\d\-:]+)_(?P<end>[\d\-:]+).(?P<ext>csv)(?P<cmp>)$",
        JOURNAL: r"(?P<root>.*?)(?P<start>[\d\-:]+)_(?P<end>[\d\-:]+)(\.(?P<seq>\d+)).(?P<ext>csv)(?P<cmp>\.(xz|gz))?$",
    }
    PATTERN_RENDER = {
        MAIN: "{root}{start}_{end}.{ext}{cmp}",
        JOURNAL: "{root}{start}_{end}.{seq}.{ext}",
    }
    # storage facctory.
    DEVICE_FACTORY = {
        # MAIN: Dataframe,  # is a fast-forward declaration.
        JOURNAL: IncrementalCSV,
    }
    DUMPER_DEFAULTS = {
        "csv": {},
    }
    DEVICE_DEFAULTS = {
        MAIN: {},
        JOURNAL: {"mode": "a", "_use_lock_": False},
    }
    OPTIONS = {
        "parse_dates": ["date"],
        "infer_datetime_format": True,
    }

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.DEVICE_FACTORY[MAIN] = cls

    def __init__(self, path, **kw):
        """Open a dataframe from disk.

        User can specify a path to a journal (csv) or compressed (xz) dataframe.

        - [x] open the given path.
        - [x] load what is missing.
        - [x] Merge journal data into main dataframe.
        - Merging implies closing dataframe and reopen again.

        """
        self.meta = {}

        self.assets = {}
        self.path = {}
        self._dirty = {}

        # extract cluster meta info
        path = expandpath(path)
        for kind, pattern in self.PATTERN_REGEXP.items():
            m = re.search(pattern, path)
            if m:
                d = m.groupdict()
                soft(d, path=path, seq="0000", cmp=".xz")
                self.meta.update(d)
                self.path[kind] = path
                break  # mutual exclusive

        # making a commit will merge all pending jounals
        # into main df, and start with a fresh situation.
        self.commit()

    # --------------------------------------------------
    # Writting support
    # --------------------------------------------------
    def write_record(self, record):
        """write a record into DataFrame.
        - Write record into Journal.

        """
        dev = self.assets.get(JOURNAL) or self._new_journal()
        dev.write_record(record)
        self._dirty[JOURNAL] = True

    def write_delta(self, delta):
        """write a delta into DataFrame.
        - Write record into Journal.

        """
        dev = self.assets.get(JOURNAL) or self._new_journal()
        dev.write_delta(delta)
        self._dirty[JOURNAL] = True

    # --------------------------------------------------
    # Storage support
    # --------------------------------------------------
    @property
    def df(self):
        # TODO: check journal existence and merge if needed.
        self._dirty.get(JOURNAL) and self.commit()
        return self.assets.get(MAIN)

    def commit(self):
        """Commit data to disk.

        - Drop journal device, so if someone wants to write it will
          create a new journal device for the next writtings.
        - Merge ALL journal files within MAIN and save result to disk.

        """
        # Merge JOURNAL with MAIN and save result to disk.
        # Don't create a new empty JOURNAL. Let others create when is needed

        dev = self.assets.pop(JOURNAL, None)
        if dev:
            assert isinstance(dev, self.DEVICE_FACTORY[JOURNAL])
            dev.close()

        def collapse():
            used = self._merge_journals()
            self._save_df()
            for path in used:
                os.path.exists(path) and os.unlink(path)
            self._dirty[JOURNAL] = False

        collapse()
        # p = Fiber(target=collapse)
        # p.start()
        ##p.join()
        # foo = 1

    def remove(self):
        """Delete MAIN and all JOURNAL files related to this particular
        dataframe."""
        files = [path for path, d in self._find_journals()]
        path = self.path.get(MAIN)
        path and files.append(path)
        for path in files:
            os.path.exists(path) and os.unlink(path)

    # low level storage methods ------------------------
    def _find_journals(self):
        kind = JOURNAL

        def match(d):
            # return all([d[k] == self.meta[k] for k in ('start', 'end', 'root')])
            for k in ("start", "end", "root"):
                if d[k] != self.meta[k]:
                    return False
            return True

        candidates = [
            (path, d)
            for path, d in fileiter(
                self.meta["root"], regexp=self.PATTERN_REGEXP[kind], info="d"
            )
            if match(d)
        ]
        candidates.sort()
        return candidates

    def _new_journal(self):
        """
        - find the next valid sequence for the new journal file.
        - assets[JOURNAL] points to then new device
        - setup initil parameters for the new device
        """
        kind = JOURNAL
        candidates = self._find_journals()
        if candidates:
            path, d = candidates[-1]
            d["seq"] = f"{int(d['seq'])+1:04}"
        else:
            d = dict(self.meta)
            d["seq"] = f"{0:04}"
        path = self.PATTERN_RENDER[kind].format_map(d)

        # open the journal device
        self.path[kind] = path
        dev = self.DEVICE_FACTORY[kind](path, **self.DEVICE_DEFAULTS[kind])
        self.assets[kind] = dev
        return dev

    def _load_df(self, path, sort=True):
        df = opendf(path, **self.OPTIONS)
        if isinstance(df, pd.DataFrame):
            index, columns = self._build_structure(df.columns)
            df.set_index(index, inplace=True)
            sort and df.sort_index(inplace=True)
        return df

    def _save_df(self):
        kind = MAIN
        if not self._dirty.get(kind):
            return  # has not been modified since last write_record
        df = self.assets.get(kind)
        if isinstance(df, pd.DataFrame):
            func = getattr(df, f"to_{self.meta['ext']}", None)
            if func:
                path = self.PATTERN_RENDER[kind].format_map(self.meta)
                func(
                    path,
                    **self.DUMPER_DEFAULTS.get(self.meta["ext"], {}),
                    **self.DUMPER_DEFAULTS.get(kind, {}),
                )
                self._dirty[kind] = False

    # --------------------------------------------------
    # Data manipulation support
    # --------------------------------------------------
    def _merge_journals(self):
        used = []
        main = self.assets.get(MAIN)
        if main is None:
            main = self._load_df(self.PATTERN_RENDER[MAIN].format_map(self.meta))

        for path, d in self._find_journals():
            df = self._load_df(path, sort=False)
            main, dirty = update_df(main, df)
            used.append(path)
            if dirty and isinstance(main, pd.DataFrame):
                self._dirty[MAIN] = True
                main.sort_index(inplace=True)

        self.assets[MAIN] = main
        return used

    # --------------------------------------------------
    # TODO: REVIEW
    # --------------------------------------------------
    def _old_write_record(self, record: dict):
        """this metodh is obsoleted as DataFrame is ALWAYS written on the
        journal device and then merge when its pandas df is required by someone.
        """
        assert False
        if self._df is None:
            columns = []
            index, columns = self._build_structure(record)
            if isinstance(index, list):
                columns.extend(index)
            else:
                columns.append(index)

            # self.reindex(self.columns.tolist() + indexes + columns, axis=1)
            self._df = pd.DataFrame(data=[record], columns=columns)
            self._df.set_index(index, inplace=True)
        else:
            keys, values = [], dict(record)
            for name in self._df.index.names:
                keys.append(values.pop(name))

            if len(keys) > 1:
                self._df.loc[keys] = values
            else:
                self._df.loc[keys[0]] = values
        self._need_sort = True

    def _old_update_df(self, df):
        """Used?"""
        if self._df is None:
            self._df = df
        else:
            self._df = pd.concat([self._df, df], copy=False, verify_integrity=False)

        # drop_duplicates ignore indexes that is exactty what I want
        # self._df.drop_duplicates(inplace=True, keep="first")

        self._df = self._df[~self._df.index.duplicated(keep="first")]
        self._sort()

    def _old_sort(self):
        if self._need_sort:
            self._df.sort_index(inplace=True)
            self._need_sort = False


# --------------------------------------------------
# Repository
# --------------------------------------------------
class iClusterBoundary:
    """A helpeclass for handling cluster boundaries."""

    GRID_SIZE = 1
    GRID_SIZE2 = GRID_SIZE / 2
    CLUSTER_SIZE = 1000

    # --------------------------------------------------
    # Boundaries
    # --------------------------------------------------
    def iboundaries(self, wkey):
        """Get the internal boundaries from the given wkey."""
        ikey0 = self.wkey2ikey(wkey)
        ikey0 -= ikey0 % self.CLUSTER_SIZE
        ikey1 = ikey0 + self.CLUSTER_SIZE
        return ikey0, ikey1

    def wboundaries(self, wkey):
        """Get the *wave* boundaries from the given wkey."""
        ikey0, ikey1 = self.iboundaries(wkey)
        return self.ikey2wkey(ikey0), self.ikey2wkey(ikey1)

    def hboundaries(self, iboundaries):
        """Get the *human* boundaries from the given ikey."""
        return [self.wkey2human(self.ikey2wkey(x)) for x in iboundaries]

    # --------------------------------------------------
    # wkeys, ikeys
    # --------------------------------------------------
    @abstractmethod
    def wkey2ikey(self, wkey):
        """Get the ikey related to a wkey optinaly snap-to-nearest grid."""

    @abstractmethod
    def ikey2wkey(self, ikey):
        """Get the wrelated key to a ikey."""

    @abstractmethod
    def normalize_wkey(self, wkey):
        """Cast external wkey to the right type used as *wave* key.
        i.e. : (str|arrow|datetime) -> pd.Timestamp
        """

    # --------------------------------------------------
    # Human representation of wkeys
    # --------------------------------------------------
    @abstractmethod
    def wkey2human(self, wkey):
        """Formally used to naming cluster in storage, but not limited to.

        i.e. lets wkeys being dates.
        >>> wkey = arrow.now()
        >>> wkey
        <Arrow [2022-04-18T14:08:28.894971+02:00]>
        >>> node.grid_size
        1  # 1 seg grid
        >>> node.wkey2human(wkey)
        '20220418-140828+02:00'

        """

    @abstractmethod
    def human2wkey(self, human):
        """Inverse wkey2human operation."""

    # --------------------------------------------------
    # grid and clustering
    # --------------------------------------------------
    @abstractmethod
    def next_wkeys(self, wsince, n=1):
        """Get an ordered serie of wkeys with 'grid' distance between points."""

    @abstractmethod
    def next_ikeys(self, isince, n=1):
        """Get a ordered serie of wkeys with 'grid' distance between points."""


class iClusterStorage:
    def __init__(
        self,
        soft_cluster_len: int = 20,
        hard_cluster_len: int = 40,
        klass: iRecordStorage = None,
        bounds: iClusterBoundary = None,
        index_klass=None,
        *args,
        **kw,
    ):
        assert klass is not None

        # clusters contains the information found about all available clusters storage.
        self.cluster_info = {}

        # assets holds cluster devices by its kind (i.e JOURNAL, MAIN, etc)
        self.klass = klass
        self.bounds = bounds
        self.index_klass = index_klass
        self.clusters: iRecordStorage = {}
        self.soft_cluster_len = soft_cluster_len
        self.hard_cluster_len = hard_cluster_len

    # --------------------------------------------------
    # Clustering support
    # --------------------------------------------------
    def analyze_cluster_info(self, commit=False):
        if not self.cluster_info:
            # try to capture existing data from disk
            self._explore_clusters()

        # Discussion: repository clusters may belong to multiple
        # *kinds* (i.e journal, main, etc), but trying to open a
        # cluster (device) for 1st time cause all *kinds* may
        # condense and collapse into *main* category, so we are
        # forcing to move all data to *main* kind to maintain the
        # the data coherence.
        result = {}
        selector = {-1, 0}
        for kind, clusters in self.cluster_info.items():
            iboundaries = list(clusters)
            iboundaries.sort()
            for idx in selector:
                try:
                    ibounds = iboundaries[idx]
                except IndexError:
                    continue

                if ibounds not in result:
                    dev = self._open_cluster(ibounds)
                    # 'main' category is supposed to be ALWAYS
                    # loaded when dev is opened for 1st time.
                    df = dev.assets[MAIN]
                    for idx2 in selector:
                        result.setdefault(idx, {})[idx2] = df.iloc[idx2]

                    if commit and kind in (JOURNAL, ):
                        dev.commit()
        return result

    @abstractmethod
    def _explore_clusters(self):
        """try to gather cluster info from persistence system
        (filsystem, database, etc).
        """

    @abstractmethod
    def _open_cluster(self, ibounds):
        """try to gather cluster instance from persistence system
        (filsystem, database, etc)."""


class iRepository(iRecordStorage, iClusterStorage):
    """A Repository to store a single type of data (aka *record*) using
    *clusters* organized by interval bounds.


    A Repository can deal with indiidual records or bunch of records (aka *deltas*).

    - Data are stored in clusters.
    - User uses wkeys to index its own data.
    - There is a mapping between user keys (wkey) and integer (monotonic) internal key.
    - There is a mapping between user keys and human-readable user keys.
    - Clusters contains a range of internal keys defined by cluster-size.
    - Cluster storage path if build from human-readable keys.
    - wkey is got from a record attribute considered as the *key*.

    Parameters:
    - CLUSTER_LEN: number of ikeys stored in a single cluster.
    - GRID_SIZE: size of the ikey grid. Default is 1.
                 when a grid_size > 1, records are allocated in the nearest ikey point.

    """

    PATTERN_REGEXP = r"(?P<root>.*?)(?P<start>[\d\-:]+)_(?P<end>[\d\-:]+).csv.xz"
    PATTERN_RENDER = "{root}{start}_{end}.csv.xz"
    DEVICE_DEFAULTS = {}

    EXTRA_PARAMS = {  # TODO: remove, not used here
        "parse_dates": ["date"],
        "infer_datetime_format": True,
    }

    # HUMAN_FTM = "%Y%m%d-%H5%M%S%z"

    def __init__(
        self,
        klass: iRecordStorage = Dataframe,
        *args,
        **kw,
    ):

        super().__init__(klass=klass, *args, **kw)
        # records related information

        self.index = None
        self.columns = None

    # --------------------------------------------------
    # Writting support
    # --------------------------------------------------
    def write_record(self, record: Dict):
        """Write a record into repository.
        - create index and columns on 1st call if not already.
        - get the *cell* that will hold the record.
        - update the cell accross active devices ('journal', 'file', etc)
        - if there is no active deviec for this *cell*, open a 'journal' one and update using it.

        NOTE: this method assume record is a dictionary.
        For writting deltas a new function will be necessary.

        """
        if not self.columns:
            # get the index name
            self.index, self.columns = self._build_structure(record)

        wkey = record[self.index]
        iboundaries = self.bounds.iboundaries(wkey)
        dev = self.clusters.get(iboundaries)
        if dev is None:
            dev = self.clusters[iboundaries] = self._open_cluster(iboundaries)
        dev.write_record(record)

    def write_delta(self, delta):
        """Write delta into repository.
        delta is a dataframe of several records.
        """
        bounds = self.bounds
        while delta.shape[0] > 0:
            wkey0 = delta.index[0]
            iboundaries = bounds.iboundaries(wkey0)
            wkey1 = bounds.ikey2wkey(iboundaries[1])
            mask = delta.index.values < wkey1
            df = delta[mask]
            dev = self.clusters.get(iboundaries)
            if dev is None:
                dev = self.clusters[iboundaries] = self._open_cluster(iboundaries)
            dev.write_delta(df)
            delta = delta[~mask]

    # --------------------------------------------------
    # Clustering support
    # --------------------------------------------------
    def _open_cluster(self, ibounds):
        dev = self.clusters.get(ibounds)
        if dev is None:
            self._revise_limits()
        return dev

    def _revise_limits(self):
        if len(self.clusters) > self.hard_cluster_len:
            while len(self.clusters) > self.soft_cluster_len:
                ibound, dev = self.clusters.popitem()
                dev.commit()

    # --------------------------------------------------
    # Storage support
    # --------------------------------------------------
    def commit(self, explore=False):
        """Commit any pending data to the storage."""
        if explore:
            self.analyze_cluster_info(commit=True)
            # for ibounds in self.cluster_info[JOURNAL]:
            # dev = self._open_cluster(ibounds)
            # dev.commit()
            # foo = 1
        else:
            for dev in self.clusters.values():
                dev.commit()

    # --------------------------------------------------
    # iSync capabilities.
    # --------------------------------------------------
    def __getitem__(self, subscript):
        if isinstance(subscript, slice):
            # do your handling for a slice object:
            assert subscript.step in (None, 1)
            yield from self.get_records(subscript.start, subscript.stop)
        else:
            for record in self.get_deltas(subscript):
                yield record
                break  # just 1

    # records ------------------------------------------
    def row2record(self, row):
        record = dict(row.items())
        record[self.index] = row.name
        return record

    def get_records(self, start_key, end_key=None):
        for df in self.get_deltas(start_key, end_key):
            for idx, row in df.iterrows():
                record = self.row2record(row)
                yield record

    # deltas ------------------------------------------
    def get_deltas(self, start_key, end_key=None):
        """Return a iterator with all data from starting key:
        - [ ] get the *boudaries* that will hold the starting key.
        - [ ] return an interator that filter dataframes from
              starting and end keys.
        - [ ] allow re-query same dataframe before moving to the next one
              allowing df to be fed while returning data to caller level.
        """
        bounds = self.bounds

        start_key = bounds.normalize_wkey(start_key)
        ib0 = bounds.iboundaries(start_key)
        if end_key is None:
            ib1 = [sys.maxsize, sys.maxsize]
            query = f"index >= @start_key"
        else:
            end_key = bounds.normalize_wkey(end_key)
            ib1 = bounds.iboundaries(end_key)
            query = f"index >= @start_key AND index < @end_key"

        # context for dataframe query
        ctx = {"end_key": end_key, "start_key": start_key}

        # build a chain of iterators until EOF or reach end_key
        while ib0[0] < ib1[1]:
            dev = self.clusters.get(ib0)
            if dev is None:
                dev = self._open_cluster(ib0)  # don't keep in cluster cache
                # dev is sorted when comes from disk

            # using Walrus Operator to avoiding invoke twice the '.df' property
            while (df0 := dev.df) is not None:  # has data
                df = df0.query(query, local_dict=ctx)
                if df.shape[0] > 0:
                    yield df
                    # df can be modified meanwhile with new data
                    # so we need to query again, but modifing the boundaries of the query.
                    ctx["start_key"] = df.iloc[-1].name
                    query = query.replace(">=", ">")
                else:
                    ib0 = ib0[1], ib0[1] + bounds.CLUSTER_SIZE
                    break  # no more data in this dataframes, exiting...
            else:
                break  # no more dataframes, exiting...
        foo = 1

    def _old_get_from(self, start_key, end_key=None):
        """Return a iterator with all data from starting key:
        - [x] get the *cell* that will hold the starting key.
        - [x] *collapse* journal (if exists) into Dataframe.
        - [x] return an interator that filter dataframes form
              starting and end keys.
        - [x] allow re-query same dataframe before moving to the next one
              allowing df to be fed while returning data to caller level.

        """
        start_key = self.normalize_key(start_key)
        end_key = self.normalize_key(end_key)

        if end_key is None:
            end_cell = sys.maxsize
            query = f"index >= @start_key"
        else:
            end_cell = self._key2cell(end_key) + 1
            query = f"index >= @start_key AND index < @end_key"
        # build a chain of iterators until EOF or reach end_key
        ctx = {"end_key": end_key}
        cell = self._key2cell(start_key)
        ctx["start_key"] = start_key
        while cell < end_cell:
            self._commit(JOURNAL, cell)
            for dev in self._open_cluster(MAIN, cell):
                while dev._df is not None:
                    df = dev._df.query(query, local_dict=ctx)
                    for idx, row in df.iterrows():
                        record = self.row2record(row)
                        yield record
                    if df.shape[0] > 0:
                        ctx["start_key"] = record[self.index] + timedelta(
                            microseconds=1
                        )
                    else:
                        break  # this dataframe is exhausted
                else:
                    cell = end_cell  # no more dataframes, exiting...
                cell += 1
        foo = 1


class iFolderRepository(iRepository):
    def __init__(self, root="/tmp/repo", *args, **kw):
        super().__init__(*args, **kw)

        # repostory related information
        self.root = root.rstrip("/") + "/"  # repository location

    # --------------------------------------------------
    # Clustering support
    # --------------------------------------------------
    def _explore_clusters(self):
        bounds = self.bounds
        """ "build a list of existing clusters (journal:csv and main.xz)"""
        for kind, pattern in self.klass.PATTERN_REGEXP.items():
            clusters = self.cluster_info.setdefault(kind, {})
            for filename, d in fileiter(self.root, pattern):
                wkey = bounds.human2wkey(d["start"])
                iboundaries = bounds.iboundaries(wkey)
                clusters[iboundaries] = filename

                # check that boundaries are ok
                wkey1 = bounds.human2wkey(d["end"])
                iboundaries1 = bounds.iboundaries(wkey1)
                assert iboundaries[1] == iboundaries1[0]

    def _open_cluster(self, ibounds):
        dev = super()._open_cluster(ibounds)
        if dev is None:
            human = {
                k: v for k, v in zip(["start", "end"], self.bounds.hboundaries(ibounds))
            }
            human["root"] = self.root
            path = self.PATTERN_RENDER.format_map(human)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            dev = self.klass(path, **self.DEVICE_DEFAULTS)
            self.clusters[ibounds] = dev
        return dev


TIME_TYPE = Union[arrow.Arrow, pd.Timestamp]


class iDateBoundary(iClusterBoundary):
    """A base class that use time as wkey and pandas as data holder."""

    # HUMAN_FTM = "%Y%m%d-%H5%M%S%z"
    HUMAN_FTM = "%Y%m%d-%H%M%S"
    WKEY = "date"
    CLUSTER_SIZE = 24 * 3600 * 7

    # TODO: REVIEW
    TS_DEF = {
        "unit": "s",
        #'tz' : "Europe/Madrid",
        "tz": "Etc/UTC",
    }

    # --------------------------------------------------
    # wkeys, ikeys
    # --------------------------------------------------
    def wkey2ikey(self, wkey: TIME_TYPE):
        if isinstance(wkey, arrow.Arrow):
            ikey = wkey._datetime.timestamp()
        elif isinstance(wkey, pd.Timestamp):
            ikey = wkey.timestamp()

        ikey = int((ikey + self.GRID_SIZE2) // self.GRID_SIZE)
        return ikey

    def ikey2wkey(self, ikey):
        """Get the wrelated key to a ikey."""
        return pd.to_datetime(ikey, unit="s")

    def normalize_wkey(self, wkey):
        """Cast external wkey to the right type used as *wave* key.
        i.e. : (str|arrow|datetime) -> pd.Timestamp
        """
        if isinstance(wkey, str):
            wkey = pd.to_datetime(wkey, self.HUMAN_FTM)
        elif isinstance(wkey, arrow.Arrow):
            wkey = pd.to_datetime(wkey._datetime)
        assert isinstance(wkey, pd.Timestamp)
        return wkey

    # --------------------------------------------------
    # Human representation of wkeys
    # --------------------------------------------------

    def wkey2human(self, wkey: TIME_TYPE):
        """Formally used to naming cluster in storage, but not limited to.

        i.e. lets wkeys being dates.
        >>> wkey = arrow.now()
        >>> wkey
        <Arrow [2022-04-18T14:08:28.894971+02:00]>
        >>> node.grid_size
        1  # 1 seg grid
        >>> node.wkey2human(wkey)
        '20220418-140828+02:00'

        """
        human = wkey.strftime(self.HUMAN_FTM)
        return human

    def human2wkey(self, human):
        """Inverse wkey2human operation."""
        wkey = pd.to_datetime(human, format=self.HUMAN_FTM)
        return wkey

    # --------------------------------------------------
    # TODO: REVIEW
    # --------------------------------------------------

    # --------------------------------------------------
    # Pipeline / Workflow support
    # --------------------------------------------------

    # --------------------------------------------------
    # Request Synchronization from paren nodes
    # --------------------------------------------------


class DateRepository(iFolderRepository):
    """Convenience class to store date based datafames in folders."""

    def __init__(self, index_klass=pd.Timestamp, *args, **kw):
        kw.setdefault("bounds", iDateBoundary())
        super().__init__(index_klass=index_klass, *args, **kw)


class Device(Dataframe):
    pass


class SyntheticBroker(Device):
    @property
    def features(self):
        return [
            {"symbol": ["ES", "MES", "NQ", "MNQ"]},
            {"expiration": ["H2", "M2", "U2", "Z2"]},
            {
                "tf": [
                    "1s",
                    "5s",
                    "1m",
                    "2m",
                    "5m",
                    "10m",
                    "15m",
                    "20m",
                    "60m",
                    "240m",
                    "1d",
                ]
            },
        ]

    @property
    def capabilites(self):
        master = None
        for data in self.features:
            df = pd.DataFrame(data)
            master = df if master is None else master.join(df, how="cross")
        return master


class XXXX(Device):
    @property
    def features(self):
        return [
            {"symbol": ["NQ"]},
            {"expiration": ["H2", "M2", "U2", "Z2"]},
            {
                "tf": [
                    "1s",
                    "5s",
                    "1m",
                    "2m",
                    "5m",
                    "10m",
                    "15m",
                    "20m",
                    "60m",
                    "240m",
                    "1d",
                ]
            },
        ]

    @property
    def capabilites(self):
        master = None
        for data in self.features:
            df = pd.DataFrame(data)
            master = df if master is None else master.join(df, how="cross")
        return master


if __name__ == "__main__":

    timeframes = {"tf": ["1s", "5s", "1m", "20m", "60m", "1d"]}
    years = df_join({"year": range(2, 4)})

    m04 = df_join({"month": ["H", "M", "U", "Z"]})
    m12 = df_join(
        {"month": ["F", "G", "H", "J", "K", "M", "N", "Q", "U", "V", "X", "Z"]}
    )

    exp04 = df_glue(m04, years, name="expiration")
    exp12 = df_glue(m12, years, name="expiration")

    df1 = df_join({"symbol": ["ES", "NQ"]}, exp04, timeframes)
    df2 = df_join({"symbol": ["CL"]}, exp12, timeframes)

    # df1 = df_join({"symbol": ["ES"]}, {"expiration": ["H2", "Z2"]}, timeframes)
    # df2 = df_join(
    # {"symbol": ["CL"]}, {"expiration": ["F2", "G2", "H2", "J2", "Z2"]}, timeframes
    # )

    master = df_concat(df1, df2)
    master.to_csv("/tmp/kk.csv")

    broker = SyntheticBroker("/tmp/demo-broker.csv")
    cap = broker.capabilites
    print(cap)
    foo = 1
