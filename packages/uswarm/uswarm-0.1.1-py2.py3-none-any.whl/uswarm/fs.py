"""Main Vitual File System (VFS) module.

"""

import os
import re
import time
import yaml
import pickle
import lzma as xz


class iVFS:
    """The Interface for Virtual File System."""

    def __init__(self):
        """Base class init"""
        raise NotImplementedError()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.path}')"

    def mount(self, path, vfs):
        """Mount (attach) a VFS into parent."""
        raise NotImplementedError()

    def umount(self, path):
        """Umount (dettach) a VFS into parent."""
        raise NotImplementedError()

    def delete(self, path):
        """Delete an item from VFS."""
        raise NotImplementedError()

    def access(self, path):
        """Get access level of an item."""
        raise NotImplementedError()

    def find(self, top, name=".*", topdown=True, klass=None):
        raise NotImplementedError()

    def flush(self, path="/"):
        """Force all not saved data to be flused to disk."""
        raise NotImplementedError()

    # item storage interface
    def get(self, path):
        """Retrieve an item in VFS."""
        raise NotImplementedError()

    def put(self, path, item, **kw):
        """Store an item in VFS."""
        raise NotImplementedError()

    def update(self, path, item, **kw):
        """Update an item in VFS. In some VFS may be possible updating partially an item."""
        raise NotImplementedError()


class Root(iVFS):
    """The Absolute Genial Root Unique Point."""

    def __init__(self):
        """Base class init"""
        self.mounts = []  #: sorted mount points
        self._notifications = {}
        self._locks = {}

    def mount(self, path, vfs):
        """Mount (attach) a VFS into parent."""
        assert isinstance(vfs, VFS)
        self.mounts.append((path, vfs))
        self.mounts.sort(key=lambda x: len(x[0].split("/")), reverse=True)

    def get_vfs(self, path, strict=True):
        """Try to get the VFS that handle a path."""
        for p, vfs in self.mounts:
            if (strict and p == path) or (not strict and p in path):
                return p, vfs
        return '', None

    def umount(self, path):
        """Umount (dettach) a VFS into parent."""
        for i, (p, vfs) in enumerate(list(self.mounts)):
            if p == path:
                vfs.flush()
                self.mounts.pop(i)
                break
        else:
            raise RuntimeError(f"{path}: Not mounted in system")

    def put(self, path, item, **kw):
        """Store an item in VFS."""
        self._lock(path)
        vfs, rel = self._find_vfs(path)
        r = vfs.put(rel, item, **kw)
        self._notify(path, "put")
        return r

    def get(self, path):
        """Retrieve an item in VFS."""
        self._lock(path)
        vfs, rel = self._find_vfs(path)
        r = vfs.get(rel)
        self._notify(path, "get")
        return r

    def update(self, path, item, **kw):
        """Update an item in VFS. In some VFS may be possible updating partially an item."""
        self._lock(path)
        vfs, rel = self._find_vfs(path)
        r = vfs.update(rel, item, **kw)
        self._notify(path, "update")
        return r

    def delete(self, path):
        """Delete an item from VFS."""
        self._lock(path)
        vfs, rel = self._find_vfs(path)
        r = vfs.delete(rel)
        self._notify(path, "delete")
        return r

    def find(self, path, name=".*", topdown=True, klass=None):
        candidates = list(self.mounts)
        if topdown:
            candidates.reverse()

        for top, vfs in candidates:
            rel = path.split(top)
            if len(rel) > 1:
                rel = top.join(rel[1:])
                for sub, item in vfs.find(rel, name, topdown, klass):
                    yield top + sub, item

    def notify(self, regexp, callback, events=".*"):
        """Notify when there's an event in FS.

        - regexp: absolute/relative matching path.
        - callback to be invoked (not async by now).
        - events: regexp of which events we're interested.

        callback = None, clean the callback.
        """
        if callback:
            holder = self._notifications.setdefault(regexp, dict())
            holder.setdefault(events, list()).append(callback)
        else:
            holder = self._notifications.get(regexp, {})
            holder.pop(events, None)
            if not holder:
                self._notifications.pop(regexp)

    def _notify(self, path, event):
        """Dispatch notification callbacks on events on VFS."""
        for regexp, holder in self._notifications.items():
            if re.match(regexp, path):
                for ev, callbacks in holder.items():
                    if re.match(ev, event):
                        for func in callbacks:
                            func(path, event)

    def access(self, path):
        """Get access level of an item."""
        vfs, rel = self._find_vfs(path)
        return vfs.access(rel)

    def flush(self, path="/"):
        """Force all not saved data to be flused to disk."""
        vfs, rel = self._find_vfs(path)
        return vfs.flush(rel)

    def lock(self, path, agent=None):
        """Lock an item by an agent.
        In multi-threaded processes sharing the same VFS
        a mechanims for locking the access to an item is needed.

        We assume that a reactor async model is used here, so there is
        not necessary to implement such mechanims inside a reactor.
        """
        holder = self._locks.setdefault(path, dict())
        holder[agent] = time.time()

    def unlock(self, path, agent=None):
        """unLock an item by an agent or None for all."""
        holder = self._locks.get(path, {})
        holder.pop(agent, None)
        if not agent or not holder:
            self._locks.pop(path)

    def _lock(self, path):
        for regexp, holder in self._locks.items():
            if re.match(regexp, path):
                agents = []
                for agent, t0 in holder.items():
                    self._notify(path, "locked")
                    agents.append(agent)

                raise RuntimeError(f"{path} is locked by: {agents}")

    def _find_vfs(self, path):
        """Find the mounted VfS that handles the path."""
        assert os.path.isabs(path), "path must be an absolute path at root level"
        for top, vfs in self.mounts:
            rel = path.split(top)
            if len(rel) > 1:
                rel = top.join(rel[1:])
                return vfs, rel

        raise RuntimeError(f"{path}: No such file or directory")


class VFS(iVFS):
    """The main Virtual File System class."""

    def __init__(self):
        """Base class init"""
        self.root = {}

    def update(self, path, item, **kw):
        """Update an item in VFS.
        Uses put when there is not better way."""

        return self.put(path, item, **kw)

    def access(self, path):
        """Get access level of an item."""
        return path in self.root


class VolatileVFS(VFS):
    """Pure RAM storage that will lost all changes on unmount.
    Just for testing purposes.
    """

    def __init__(self):
        """VolatileVFS class init"""
        super().__init__()

    def put(self, path, item, **kw):
        """Store an item in VFS."""
        aux = self.root[path] = item
        func = getattr(aux, "update", None)
        func and func(kw)

    def get(self, path):
        """Retrieve an item in VFS."""
        return self.root[path]

    def delete(self, path):
        """Delete an item from VFS."""
        return self.root.pop(path)

    def flush(self, path="/"):
        """Force all not saved data to be flused to disk."""
        pass

    def find(self, top, name=".*", topdown=True, klass=None):
        """
        TODO: overlapped volumes may return 2 items with the same path
        as a volume does not anything about what has returned
        nested (child) volume.

        """
        root = self.root
        candidates = list(root.keys())
        candidates.sort(key=lambda x: len(x.split("/")), reverse=topdown)

        regexp = re.compile(f"{top}/{name}")
        for path in candidates:
            if regexp.match(path):
                yield path, root[path]


def yaml_load(path):
    return yaml.load(open(path, "r"), Loader=yaml.Loader)


def yaml_dump(data, path):
    yaml.dump(data, open(path, "wt"), default_flow_style=False, allow_unicode=True)


def pickle_load(path):
    return pickle.load(path)


def pickle_dump(data, path):
    pickle.dump(data, path)


class SolidVFS(VolatileVFS):
    """A RAM storage that will save and load state from a single
    file on disk.

    Based on VolatileVFS but adding persistence.

    Support YAML (human intervention), Pickle format (efficiency).
    """

    LOAD = {
        ".yaml": yaml_load,
        ".yml": yaml_load,
        ".pkl": pickle_load,
        ".pickle": pickle_load,
    }
    DUMP = {
        ".yaml": yaml_dump,
        ".yml": yaml_dump,
        ".pkl": yaml_dump,
        ".pickle": yaml_dump,
    }

    @classmethod
    def load(cls, path):
        SolidVFS.LOAD[os.path.splitext(path)[-1]](path)

    @classmethod
    def dump(cls, data, path):
        SolidVFS.DUMP[os.path.splitext(path)[-1]](data, path)

    def __init__(self, path="volume.yml"):
        """SolidVFS class init"""
        super().__init__()
        self.path = path
        base, ext = os.path.splitext(path)
        if os.path.exists(self.path):
            self.root = self.LOAD[ext](path)

        foo = 1

    def flush(self, path="/"):
        """Force all not saved data to be flused to disk."""
        base, ext = os.path.splitext(self.path)
        self.DUMP[ext](self.root, self.path)

    def notify(self, regexp, callback, events=".*"):
        """Notify when there's an event in FS.

        - regexp: absolute/relative matching path.
        - callback to be invoked (not async by now).
        - events: regexp of which events we're interested.
        """
        raise NotImplementedError()


class FileVFS(VolatileVFS):
    """Map file system into accesible items from VFS.

    - get return a open stream.
    - put store a stream or string or bytes.
    """

    COMPRESSOR = {
        ".xz": xz.compress,
    }

    DECOMPRESSOR = {
        ".xz": xz.decompress,
    }

    STREAM = {
        ".xz": xz.open,
        "default": open,
    }
    MODE = {
        ".xz": "binary",
        "default": "text",
    }

    MODE_TYPE = {
        "binary": {
            "rt": "rb",
            "r": "rb",
            "wt": "wb",
            "w": "wb",
        },
        "text": {
            "rt": "rt",
            "r": "r",
            "wt": "wt",
            "w": "w",
        },
    }

    def __init__(self, path):
        """FileVFS class init"""
        super().__init__()
        self.path = path
        self.streams = {}

    def put(self, path, item, mode="w", **kw):
        """Store an raw item into VFS."""
        with self._open(path, mode) as stream:
            raw = bytes(str(item), "utf-8")  # TODO: different encodings
            stream.write(raw)
        self._close(path)

    def get(self, path):
        """Retrieve an item in VFS."""
        return self._open(path, "r")

    def delete(self, path):
        """Delete an item from VFS."""
        path, ext = self._expand_path(path)
        os.unlink(path)

    def flush(self, path="/"):
        """Force all not saved data to be flused to disk.
        We can use 'fd.flush' for regular files but using
        '.xz' extension does not work, so we need to close
        and reopen the file.
        """
        path, ext = self._expand_path(path)
        if path in self.streams:
            stream, mode = self.streams.pop(path)
            if ext in (".xz",):  # these extensions does not suppor flushing
                _, mode = self._close(path)
                stream = self._open(path, mode)
            else:
                stream.flush()
            return stream, mode

        raise RuntimeError(f"{path} unknown opened file")

    def find(self, top, name=".*", topdown=True, klass=None):
        """
        TODO: overlapped volumes may return 2 items with the same path
        as a volume does not anything about what has returned
        nested (child) volume.

        """
        # TODO: implement
        raise NotImplementedError()
        root = self.root
        candidates = list(root.keys())
        candidates.sort(key=lambda x: len(x.split("/")), reverse=topdown)

        regexp = re.compile(f"{top}/{name}")
        for path in candidates:
            if regexp.match(path):
                yield path, root[path]

    def _open(self, path, mode):
        """Low level open"""
        path, ext = self._expand_path(path)

        m = self.MODE.get(ext) or self.MODE["default"]
        mode = self.MODE_TYPE[m].get(mode, mode)

        stream = None
        if path in self.streams:
            stream, m = self.streams[path]
            if stream.closed:
                stream = None

        if stream:
            if m != mode:
                raise RuntimeError(f"{path} is already opened with different mode {m}")
        else:
            opener = self.STREAM.get(ext) or self.STREAM["default"]
            stream = opener(path, mode)
            self.streams[path] = stream, mode

        return stream

    def _close(self, path):
        path, ext = self._expand_path(path)
        if path in self.streams:
            stream, mode = self.streams.pop(path)
            stream.close()
            return stream, mode
        raise RuntimeError(f"{path} unknown opened file")

    def _expand_path(self, path):
        base, ext = os.path.splitext(path)
        if os.path.isabs(path):
            path = f"{self.path}{path}"
        else:
            path = f"{self.path}/{path}"

        return path, ext


class RepositoryVFS(VFS):
    """A repository that store items on disk in a *clustered* manner.
    This is the base of any storage that requires store huge number
    of items on disk with fast loading access.
    """
