"""H-Sync module.

This module provides support for synchronize two data sets.

Data set are organized like a FileSystem.

Every element in system is addressed by a *path* and belongs
to a parent *group* that acts like a folder for the belonging
elements.


The idea behind is to consider an alternative representation of
any system and map it into a *virtual file-system* with is an
easier problem.

::

    +--------------+               +-------------------+
    |              |               |                   |
    |   Complex    |    <mapping>  |      Virtual      |
    |   System     |-------------->|    File System    |
    |      A       |               |        A          |
    |              |               |                   |
    +--------------+               +-------------------+
                                             |
                                             | <sync>
                                             v
    +--------------+               +-------------------+
    |              |               |                   |
    |    Complex   |    <mapping>  |      Virtual      |
    |    System    |<--------------|    File System    |
    |      B       |               |        B          |
    |              |               |                   |
    +--------------+               +-------------------+


The *path* of an element identify a local name and the group
that the element belongs (basename and dirname).

The *value* of the element is anything that represent the internal
status of the element: can be just raw data, or meta-data that will
be used to synchronize the element using an external mechanism.

In order to generalize the whole idea, let's consider the value of
the element as the *meta-data* of the element.


Element Status
----------------

In order to fit the requirements for *H-Sync*, the system must support the
following operations:

- NEW: when a new element appears in the system for 1st time and a placeholder
      is created.
- SETTLE: The 1st fresh-update to allocate in the placehoder.
  Next changes in element will be tagged as UPDATE.
- UPDATE: when an existing element has modified its meta-data.
- REPLACED: when another element is stored in an existing *path* overwriting
      the old element.
- MOVED: when an element if moved from a group to another group (and name).
- DELETED: when the element is removed from group and is not longer accessible
      using *path*
- ALIVE: when an element *resurrect* in the last location.

Element must provide an unique *uid* in its *meta-date* like *inode* in Unix
file-system, so*H-Sync* can track the element across the whole system.

If system can not provide such *uid* then a serial can be used, but *H-Sync*
may fail when an element is new, just has been deleted and resurrected or
simply moved.

Providing such *uid*s for elements will allow to have multiples *path*s
pointing to the same element *e*, in the same way *hard-link* in a Unix
file-system.


::

    +-------------+
    |   /foo/bar  |----------+
    +-------------+          |
                             |
                             v
                     +---------------+
                     | uid: xxxxxx   |
                     | data: {...}   |
                     +---------------+
                             ^
                             |
    +-------------+          |
    |  /buzz/bass |----------+
    +-------------+


Journaling
------------

*H-Sync* tracks what happens with elements and keep changes in a journal log.

Using this journal, two different systems can exchange its *delta* changes
since last time they *see* each other and try to close the gap between them
as much as possible.


::

    +---------+
    |         |
    |         |     +-------+-------+    +---------+
    |  Delta  |     |       |       |    |         |
    |    B    |     |       |       |    |  Delta  |
    |         |<----| Mixer | Mixer |--->|    A    |
    +---------+     |   A   |   B   |    |         |
                    |       |       |    |         |
    +---------+     |       |       |    +---------+
    |         |     |       |       |
    |         |     |       |       |    +---------+
    |  Delta  |---->|       |       |<---|         |
    |    A    |     |       |       |    |  Delta  |
    |         |     |       |       |    |    B    |
    +---------+     +-------+-------+    +---------+
    |         |                          |         |
    |         |                          |         |
    |  Hist   |                          |  Hist   |
    | Journal |                          | Journal |
    |   ...   |                          |   ...   |
    |         |                          |         |
    |         |                          |         |
    +---------+                          +---------+



Operations
------------

When system *B* receive changes from system *A* then *B* analyze the change and
determines how to sync the element *e*:

- FAST_FORWARD: a clean update: *e* has been modified in *B* but not in *A*.

- SYNC: a clean update: *e* has been modified in *A* but not in *B*.

- VALUE_CONFLICT: *A* and *B* have modified *meta-data* if a way only value
is possible. System needs to *merge* the *meta-data* and resolve the conflict.

- OWNER_CONFLICT: The *A* makes a valid change for *e* but *B* has made a
change that destroy the *e* structure integrity such delete, move or resurrect.
This conflict is also known as *owner* conflict as usually the way to solve
the conflict is to keep the change from the *higher* system so the change will
spread across all connected *lower* systems.

- INTERNAL_ERROR: when *e* last state and delta from *A* is not compatible with
any reasonable change.

----

TODO:

- [x] get FS changes and update status archive.
- [x] Use 2 generators for recent update files and other files.
- [ ] track last sync between machines if it's really necessary.
- [ ] compute clock time-delta with remote hosts.
- [ ] detect 'mv' files (inode is the same)
- [x] when a folder is 'updated' that means a file is modified inside, \
      so we can speed up the process lunching a generator just for this folder

"""
import time
import pickle
import yaml
#import lzma as xz
#import bz2
#import gzip as gz

from gutools.tools import expandpath, round_robin, fileiter, parse_uri, utask_queue, uTask, NOP
from lswarm.loop import Layer, Network, expose, STATE_READY, MERGE_ADD

# ----------------------------------------------------------
# Element Status
# ----------------------------------------------------------

ZERO = None
NEW='N'
UPDATED='U'
REPLACED='R'
MOVED='M'
SETTLE='S'
DELETED='D'
ALIVE = 'A'

class Element():
    """Represent the base element in a synchronizable system.
    """
    __slots__ = 'uid', 'data', 'status'

    def __init__(self, uid, data=None, status=None):
        self.uid = uid
        "the unique identifier of the element in the system."

        self.data = data
        "the *meta-data* associated with element."

        self.status = status
        "the element's status."

    def __str__(self):
        # return f"E:({self.uid}, {self.state}, {self.info}, {self.created}, {self.modified}, {self.data})"
        return f"E:({self.uid}[{self.status}]: {self.data})"

    def __repr__(self):
        return self.__str__()

class System():
    """This class represent a base system with synchronization capabilities.

    The changes in system may be get by polling of by direct event invokation.

    Polling:

    1. begin_scan: any pre-scan actions
    2. call analyze() for all elements in system
    3. end_scan: any post-scan actions

    TODO: scan only a subset of the system. Need to modify begin_scan()

    Direct:

    1. call analyze() directly if real system support notification changes.


    Changes are stored in a journal list to share with other systems.

    Jounal changes can be:

    - value changes: element data have been modified: new or update
    - structural changes: element has been delete, replaced, moved or settle

    Trash is used to *resurrect* elements, not to recoved the element data, so
    when an element is deleted and later its uid is used we can detect that element
    is not just new, but resurrected.


    """
    def __init__(self, compact=True):

        self._element = dict()
        "<uid: element> map"

        self._group = dict()
        "<root: <name: uid>> map"

        self._journal = list()
        "[time, uid, change] list of changes ordered by time"

        self._compact = compact
        "journal compacted or not"

        self._trash = dict()
        "<uid: element> deleted map. Used to locate elements that has been moved or resurrected"

        self.__cache = dict()
        self.__scan = dict()
        "<root: set(names)> map to detect when an element has been moved or deleted"

    # Scan groups
    def begin_scan(self, root):
        """Prepare for start a scan:

        - create list of any element in system to detect deleted elements.
        """
        # self.__scan[root] = set([e.uid for e in self._group.get(root, {}).values])
        self.__scan[root] = set([name for name in self._group.get(root, {})])

    def add(self, path, element):
        """Check if a new journal entry must be written
        comparing the element with existing data:

        - NEW: when element is new in system but is not yet allocated.
        - If element already exists:
            - UPDATED: when uid match but data has been modifed
            - REPLACED: when uid does not match but previous element exists
            - NEW: when uid doesn't match and element was deleted or moved.
        - If element does not exists yet:
            - MOVED: an element with same uid was in the trash bin,
                     but path has changed
            - SETTLE: when is the 1st time we see thisso uid. SO we *link*
                     this path to uid

        Finally:

        - store element by uid
        - remove any existing eleent is scan list (element has been seen)

        TODO: apply hooks/triggers
        """
        # Check if element is new in system by uid
        uid = element.uid
        e0 = self._element.get(uid)
        if not e0:
            self._journal_value(NEW, element, uid)

        # Locate the placeholder for current element in path
        root, group, name, e = self._get_placeholder(path)

        # Check if the placeholder was already used
        if e:
            if e.uid == uid:
                if e.data != element.data:
                    self._journal_value(UPDATED, element, uid)
            elif e.status in (SETTLE, UPDATED, ):
                # 4. Else the element in placehoder is (deleted)
                self._journal_struct(REPLACED, element, path, uid)
        else:
            # check if the element was in the trash
            # is recovered from trash (just the last same one uid)
            # or is a new element placed in structure for 1st time
            path0 = self._trash.pop(uid, None)
            if path0:
                if path0 == path:
                    self._journal_struct(ALIVE, element, uid, path)
                else:
                    self._journal_struct(MOVED, element, path, path0)
            else:
                self._journal_struct(SETTLE, element, path, uid)

        # store element in System
        self._element[uid] = element
        group[name] = uid

        # remove element from group scan (if any)
        scan = self.__scan.get(root, None)
        if scan and name in scan:
            scan.remove(name)

        return element

    def end_scan(self, root):
        """End scan process:

        Detect elements that has been not seen when scan has finished
        and delete them.
        """
        for name in self.__scan.pop(root, set()):
            self.delete(f'{root}/{name}')

    # Global operations
    def gc(self):
        """Clean any element in trash bin."""
        self._trash.clear()

        # garbage collector of deleted elements
        universe = set()
        for root, group in self._group.items():
            universe.update(group.values())

        # remove all non-referenced elements
        for uid in universe.symmetric_difference(self._element):
            self._element.pop(uid)


    def find(self, uid, fast=True):
        """Try to find an element by uid.

        First use a uid cache by default to avoid a full scan in the structure.
        """
        if uid in self.__cache and fast:
            return self.__cache[uid]
        else:
            for root, group in self._group.items():
                for name, _uid in group.items():
                    if _uid == uid:
                        self.__cache[uid] = root, group, name  # TODO: use a list to store hardlinks?
                        return self.__cache[uid]

    # Direct operations
    def get(self, path):
        root, group, name, element = self._get_placeholder(path)
        return element

    def move(self, old, new):
        """Move an element from a location to another location:

        - find both placeholders
        - delete old placehoder and decrease references
        - update new placehoder with last one

        """
        r1, g1, n1, e1 = self._get_placeholder(old)
        assert e1 is not None

        r2, g2, n2, e2 = self._get_placeholder(new)

        g1.pop(n1)
        g2[n2] = e1.uid
        self._journal_struct(MOVED, e1, new, old)

        return e1

    def delete(self, path):
        """Delete the element located by path and store (uid: path) value in trash container."""
        # Locate the placeholder for the element
        root, group, name, e = self._get_placeholder(path)
        assert e, "Must exists to be deleted!"
        group.pop(name)
        self._journal_struct(DELETED, e, path, None)

        self._trash[e.uid] = path

    def link(self, old, new):
        """Create an *hard* link"""
        r1, g1, n1, e1 = self._get_placeholder(old)
        assert e1 is not None
        self.add(new, e1)

    def group(self, root):
        """Create a new group (*folder* equivalent)."""
        if root not in self._group:
            self._group[root] = Group(self, root)
        return self._group[root]

    # internal helpers
    def _get_placeholder(self, path):
        """Try to find the group name, group instance,
        element name and element associated with path.

        Return None when element or group does not exists.
        """
        path = path.split('/')
        name = path.pop()
        root = '/'.join(path)

        group = self.group(root)
        euid = group.get(name)
        element = self._element.get(euid)
        return root, group, name, element



    # load/save state
    def dump(self, fmt='yaml'):
        """Get a dump of internal state of system."""
        if fmt in ('yaml', 'yml'):
            return yaml.dump(self)
        return pickle.dumps(self)

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __getstate__(self):
        d0 = self.__dict__
        d1 = dict([(k, d0[k]) for k in d0 if '__' not in k])
        return d1

    # jounaling operations
    def _journal_value(self, operation, element, uid):
        """Add a value change in journal"""
        #raw = pickle.dumps(element.data)
        raw = yaml.dump(element.data)  # clean for debugging
        element.status = operation
        if self._compact:
            # try to reuse the last valid value changed for uid
            for record in reversed(self._journal):
                if record[2] == uid and record[1] in (NEW, SETTLE, UPDATED):
                    record[3] = raw
                    return

        record = list([time.time(), operation, uid, raw])
        self._journal.append(record)

    def _journal_struct(self, operation, element, path, arg1, arg2=None):
        """Add a structural change in journal"""
        #raw1 = pickle.dumps(arg1)
        #raw2 = pickle.dumps(arg2)

        element.status = operation

        raw1 = yaml.dump(arg1)  #  clean for debugging
        raw2 = yaml.dump(arg2)  #  clean for debugging

        record = list([time.time(), operation, path, raw1, raw2])
        self._journal.append(record)


class Group(dict):
    """A folder alike container for synchronizable systems.

    Thi class acts a helper to manage elements that belong to
    the same group in system and forwards all actions to system.

    """
    def __init__(self, __system__, __root__, *args, **kw):
        super().__init__(*args, **kw)
        self._system = __system__
        self._root = __root__

    def update(self, __m=None, **kwargs):
        if __m:
            for k, v in __m.items():
                self.add(k, v)
        for k, v in kwargs.items():
            self.add(k, v)


    def add(self, name, element):
        """add an element to group."""
        if name in self:
            self.remove(name)

        self._system.add(f"{self._root}/{name}", element)
        return element

    def remove(self, name):
        """remove an element from group."""
        self._system.delete(f"{self._root}/{name}")

    def show(self, name):
        """Retrieve an element by name."""
        uid = self[name]
        return self._system._element[uid]

    def walk(self):
        """Iterator for elements in group."""
        _sys = self._system
        for name, uid in self.items():
            yield name, _sys._element[uid]



# ----------------------------------------------------------
# Versoin Control Interfaces
# ----------------------------------------------------------

# Operations

FAST_FORWARD = 'FF'
SYNC = 'SY'
VALUE_CONFLICT = 'VC'
OWNER_CONFLICT = 'OC'
INTERNAL_ERROR = 'IE'


# Valid Operations

VALID_A_MODIFICATION = set([
    (ZERO, NEW),
    (UPDATED, UPDATED),
    (REPLACED, REPLACED),
    (NEW, UPDATED),
    (MOVED, ALIVE),
    (MOVED, NEW),
]
)

VALID_B_MODIFICATION = set([NEW, UPDATED, REPLACED, ])
WIERD_B_MODIFICATION = set([MOVED, DELETED, ALIVE, ])

def sync_op(self, lA, dA, dB):
    """Tries to guess the operation that *B* need to performs to in order
    close the GAP between A and B for a given element *e*.

    Arguments:

    - lA : last state of element from A
    - dA : delta of the element in A
    - dB : delta of the element in B

    The logic is as follows:

    - When there is not *delta* from *A* then is a *FAST_FORWARD* operation
    - When there is not *delta* from *B* then is a *SYNC* operation
    - If *delta A* if compatible with last known change for *e* and
      - *delta B* is value compatible change, then is a VALUE_CONFLICT
      - *delta B* is a not compatible change, then is a OWNER_CONFLICT

    Otherwise INTERNAL_ERROR is returned.
    """

    # 1. Fast Forward
    if dA is ZERO:
        return FAST_FORWARD

    # 2. Clean Sync from A to B
    if dB is ZERO:
        return SYNC

    if (lA, dA) in VALID_A_MODIFICATION:
        # 3. Value conflict due lack of synchronization
        if dB in VALID_B_MODIFICATION:
            return VALUE_CONFLICT
        elif db in WIERD_B_MODIFICATION:
            return OWNER_CONFLICT
    return INTERNAL_ERROR



class iVersionControl():
    """Version control alike interface. (e.g Git)
    """
    # - Deal with deltas and remote peer ------------------------
    def push(self, deltas, peer):
        """Apply some deltas from peer"""

    def resolve(self, conflict, a, b):
        """Decide how to close the GAP betwen peers and resolve discrepancy."""

    def foo(self):
        pass



class iAdapter():
    """Adapter of a real system to System (a Journaling System).

    Use case: TWS Adapter

    - [ ] Get users from

    Adapter provides:

    - knowledge of mapped real system.

    - maps ext

    """

    def begin_scan(self, group=None):
        """Begin a scan of a certain group in system.
        By default it scans the whole system.
        Only a group can be scanned at the same time.
        """

    def end_scan(self):
        """Inform that scan has finished."""

    def process(self, event, *args, **kw):
        """Process event from system """




