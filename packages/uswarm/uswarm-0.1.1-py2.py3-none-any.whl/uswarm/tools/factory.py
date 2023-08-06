import inspect
import re

from weakref import WeakValueDictionary, WeakSet


from ..tools import (
    parse_uri,
    soft,
    zip_like,
)
from ..tools.abc import Any
from ..tools.iterators import snake_case

# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger

log = logger(__name__)

# --------------------------------------------------
# iFactory
# --------------------------------------------------


class iFactory(Any):
    """Base class for self-registering and creating instances by URI."""

    FACTORY = {}  # factory patterns.
    INSTANCES = {}  # already created instances
    ALIASES = {}  # alternative name for a instance
    REV_ALIASES = {}  # reverse map of aliases

    # URI_REGISTERING = None

    def __init_subclass__(cls, **kwargs):
        """Auto-register all Resource classes."""
        super().__init_subclass__(**kwargs)
        allocator = getattr(cls, "allocator", None)
        deallocator = getattr(cls, "deallocator", None)

        for pattern in [cls.__name__, f"{snake_case(cls.__name__, separator='-')}://"]:
            cls.register_factory(
                pattern=pattern, allocator=allocator, deallocator=deallocator
            )

        foo = 1

        uris = getattr(cls, "URI_REGISTERING", [])
        for _, pattern, _ in zip_like(uris):
            if isinstance(pattern, str):
                cls.register_factory(
                    pattern=pattern, allocator=allocator, deallocator=deallocator
                )

    @classmethod
    def register_factory(
        cls, pattern, allocator=None, deallocator=None, klass=None, **defaults
    ):
        klass = klass or cls
        cls.FACTORY[pattern] = allocator, deallocator, klass, defaults
        # print(f"+ Factory: {pattern}: {klass}, ...")
        # foo =1

    # --------------------------------------------------
    # allocate / deallocate
    # --------------------------------------------------
    @classmethod
    def allocate(cls, uri, alias=None, **kwargs):
        """Allocate a resource based on uri.
        Iterate by
        uri determine the nature of the resource.

        clock:// ...
        tcp://....
        ssl://....
        ssh://....
        tws://....
        """
        candidates, found = {}, False
        try:
            if uri in cls.INSTANCES:
                found = True
                return cls.INSTANCES[uri]

            if uri in cls.ALIASES:
                return cls.allocate(cls.ALIASES[uri], **kwargs)

            # search the best candidates
            for pattern in cls.FACTORY:
                m = re.match(pattern, uri)
                if m:
                    candidates[pattern] = m.groupdict()

            # select the best candidates
            sort = list(candidates)
            sort.sort(key=lambda x: (len(candidates[x]), len(x)), reverse=True)
            _uri = parse_uri(uri)
            # auto include parents
            if "parents" not in kwargs:
                frame = inspect.stack()[1][0]
                parent = frame.f_locals.get("self")
                if isinstance(parent, iFactory):
                    kwargs["parents"] = [parent]

            for pattern in sort:
                allocator, deallocator, klass, defaults = cls.FACTORY[pattern]
                kw = dict(_uri)
                kw.update(candidates[pattern])  # hard
                kw.update(kwargs)  # hard
                soft(kw, **defaults)  # soft

                # allocator must:
                # 1. find resource holder container in kernel.resource (usually by fscheme).
                # 2. holders may be dict (default case index by uri) or lists (i.e. timers).
                # 3. check if resource is already allocated.
                # 4. create and initialize the resource to be ready to receive kernel events.
                # 5. place the resource in holder
                allocator = allocator or klass
                instance = allocator(uri=uri, **kw)
                if instance is None:
                    log.error(f"Allocating Failled, uri: <{uri}>")
                else:
                    cls.INSTANCES[uri] = instance

                    found = True
                    return instance
            raise RuntimeError(f"missing function for allocating '{uri}' instance")
        except Exception as why:
            print(f"Exception: {why}")

        finally:
            # try to find quickly the most used factories
            if found:
                if alias:
                    cls.ALIASES[alias] = uri
                    cls.REV_ALIASES.setdefault(uri, set()).add(alias)

    @classmethod
    def deallocate(cls, *args, **kw):
        pass

    # subclasses may implement this methods if more fine
    # control is desired instead call constructor
    # @classmethod
    # def allocator(cls, **kw):
    # pass

    # @classmethod
    # def deallocator(cls, **kw):
    # pass

    def __init__(self, uri: str, parents=[], *args, **kw):
        self.uri = uri
        self._uri = parse_uri(uri)

        # is the last and deepest level
        # # need to call without parameters (error: super() ...)
        # object.__init__() takes exactly one argument (the instance to initialize)
        super().__init__()

        # --------------------------------------------------
        # Parent / Child relationship
        # --------------------------------------------------
        self.children = WeakSet()
        self.parents = WeakSet(parents)
        for parent in parents:
            parent.children.add(self)

        # TODO: used as cache?
        self.family = (
            WeakValueDictionary()
        )  #: resources that are *family* (parent and siblins)

    # --------------------------------------------------
    # Resources Collaboration
    # --------------------------------------------------
    def get_family(self, down=2, up=2, result=None):
        """Rebuilt family."""
        if result is None:
            result = self.family

        result[self.uri] = self

        if down > 0:
            for child in self.children:
                if child.uri not in result:  # avoid any cycles anyhow
                    result.update(child.get_family(down - 1, up, result))

        if up > 0:
            for parent in self.parents:
                if parent.uri not in result:  # avoid any cycles anyhow
                    result.update(parent.get_family(down, up - 1, result))

        return result

    def find_resource(self, uri):
        if not self.family:
            self.get_family()

        return self.family.get(uri)

    def find_resources(self, pattern=None, klass=None, down=None, up=None):
        if not self.family or down is not None or up is not None:
            self.get_family(down or 2, up or 2)

        for resource in self.family.values():
            if (
                pattern
                and re.match(pattern, resource.uri)
                or isinstance(resource, klass)
            ):
                yield resource
