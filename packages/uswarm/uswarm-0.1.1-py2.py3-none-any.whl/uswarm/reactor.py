"""Reactor Model support.

Provides:

- [x] base reactor.
- [x] nested reactors.
- [ ] workers
- [ ] adasd
- [ ] adasd


"""

import time
import os
from datetime import datetime
import inspect
import hashlib
import re
import types

# import copy
import pickle
from weakref import WeakKeyDictionary as wdict
from urllib import parse

from asyncio import (
    run,
    sleep,
    gather,
    get_event_loop,
    get_running_loop,
    create_task,
    ensure_future,
    # Protocol,
    Future,
    Task,
    Event,
)

from async_timeout import timeout

from .tools.containers import Dom
from .tools.calls import scall
from .tools.logs import iLog
from .parsers import dict_decode

# --------------------------------------------------------------------
# Internal Helpers
# --------------------------------------------------------------------
def get_calling_function(level=1, skip_modules=None):
    """finds the calling function in many decent cases."""
    # stack = inspect.stack(context)
    # fr = sys._getframe(level)   # inspect.stack()[1][0]
    skip_modules = set(skip_modules or [])
    stack = inspect.stack()
    while level < len(stack):
        fr = stack[level][0]
        co = fr.f_code
        for i, get in enumerate(
            [
                lambda: fr.f_globals[co.co_name],
                lambda: getattr(fr.f_locals["self"], co.co_name),
                lambda: getattr(fr.f_locals["cls"], co.co_name),
                lambda: fr.f_back.f_locals[co.co_name],  # nested
                lambda: fr.f_back.f_locals["func"],  # decorators
                lambda: fr.f_back.f_locals["meth"],
                lambda: fr.f_back.f_locals["f"],
            ]
        ):
            try:
                func = get()
            except (KeyError, AttributeError):
                pass
            else:
                if hasattr(func, "__code__") and func.__code__ == co:
                    if func.__module__ not in skip_modules:
                        return func
        level += 1
    raise AttributeError("func not found")


# --------------------------------------------------------------------
# Progress and Tracking
# --------------------------------------------------------------------


class Status:
    __slots__ = "p0", "t0", "p1", "t1", "p2", "t2", "item"

    def __init__(self, p0=0, p2=100, item=None, t0=None, p1=None):
        self.p0 = p0
        self.p1 = p1 or self.p0
        self.p2 = p2

        self.t0 = t0 or time.time()
        self.t1 = self.t0
        self.t2 = self.t0 + 1  # just debug

        self.item = item

    @property
    def T2(self):
        return datetime.fromtimestamp(self.t2)

    def update(self, p1=None, item=None):
        if p1 is not None:
            self.p1 = p1
            self.t1 = time.time()

        if item is not None:
            self.item = item

        progress = self.p1 - self.p0
        elapsed = self.t1 - self.t0
        speed = progress / elapsed

        if speed != 0.0:
            remain = self.p2 - self.p1
            delta = remain / speed
            self.t2 += ((self.t1 + delta) - self.t2) / 5  # fast smooth avg
        return self.t2

    def __str__(self):
        progress = 100 * (self.p1 - self.p0) / (self.p2 - self.p0)
        n = int(progress / 5)  # 20 chars bar
        bar = "x" * n + "-" * (20 - n)

        return f"[{bar}] {progress:02.3} % ETA: {self.T2}"


class Progress:
    """A generic progress class."""

    def __init__(self):
        self.state = {}

    def add(self, task, p0=0, t0=None, p2=100, item=None):
        t0 = t0 or time.time()
        status = self.state[task] = Status(p0, p2, item, t0)
        return status

    def get(self, task):
        return self.state.get(task)

    def update(self, task, p1):
        state = self.state.get(task)
        if state:
            eta = state.update(p1)
            print(f"{task}: {state}")


# --------------------------------------------------------------------
# Message
# --------------------------------------------------------------------

reg_uri = re.compile(
    r"""
    (?P<fservice>
        (?P<fscheme>
        (?P<direction>[<|>])?(?P<scheme>[^:/]*))
        ://
        (?P<xhost>
           (
                (?P<auth>
                   (?P<user>[^:@/]*?)
                   (:(?P<password>[^@/]*?))?
                )
            @)?
           (?P<host>[^@:/?]*)
           (:(?P<port>\d+))?
        )
    )?

    (?P<path>/[^?]*)?
    (\?(?P<query>[^#]*))?
    (\#(?P<fragment>.*))?
    """,
    re.VERBOSE | re.I | re.DOTALL,
)


def parse_uri(uri, bind=None, expand_query=True, **kw):
    """Extended version for parsing uris:

    Return includes:

    - *query_*: dict with all query parameters splited

    If `bind` is passed, *localhost* will be replace by argument.

    """
    m = reg_uri.match(uri)
    if m:
        for k, v in m.groupdict().items():
            if k not in kw or v is not None:
                kw[k] = v
        if bind:
            kw["host"] = kw["host"].replace("localhost", bind)
        if kw["port"]:
            kw["port"] = int(kw["port"])
            kw["address"] = tuple([kw["host"], kw["port"]])
        if kw["query"]:
            kw["query_"] = q = dict(
                parse.parse_qsl(kw["query"], keep_blank_values=True)
            )
            if expand_query:
                kw.update(q)
    return kw


def build_uri(
    fscheme="",
    direction="",
    scheme="",
    host="",
    port="",
    path="",
    query="",
    fragment="",
    **kw,
):
    """Generate a URI based on individual parameters"""
    uri = ""
    if fscheme:
        uri += fscheme
    else:
        if not direction:
            uri += scheme
        else:
            uri += f"{direction}{scheme}"
    if uri:
        uri += "://"

    host = host or f"{uuid.getnode():x}"
    uri += host

    if port:
        uri += f":{port}"
    if path:
        uri += f"{path}"

    if isinstance(query, dict):
        query = "&".join([f"{k}={v}" for k, v in query.items()])

    if isinstance(query, str):
        uri += f"?{query}"

    if fragment:
        uri += f"#{fragment}"

    return uri


def soft(self, **kw):
    """A smart update that only set the value if was missing in the target dict."""
    for k, v in kw.items():
        if self.get(k, None) is None:
            self[k] = v


class Encoder:
    def __call__(self, data):
        return bytes(data, "utf-8")


class Decoder:
    def __call__(self, data):
        return data.decode("utf-8")


RID_HEADER = "X-Request-ID"
NOT_VALID_ID = "X-Not-Valid-ID"
DELETE_AT = "X-Delete-At"
TIMEOUT_AT = "X-Timeout-At"
TIMEOUT_CALLBACKS = "X-Timeout-Callbacks"
PARTIAL_KEY = "X-Partial-Key"
DONT_INDEX = "X-Do-Not-Index"
PROGRESS_CONTROL = "X-Progress-Control"

RESPONSE_NONE = 0
RESPONSE_SINGLE = 1
RESPONSE_MULTIPLE = 2

RESPONSE_SUBSCRIPTION = -1
RESPONSE_NO_DATA = "<no-data>"


class Message:
    """Base class for Reactor messages."""

    def __init__(self, api, **kw):
        self.api = api
        self.header = kw  # everything not used in constructor is a header
        self.body = None
        self.dom = {}

    def decode(self, raw):
        return raw.decode("utf-8")

    def parse(self, dec):
        """Decode Message:
        Example:
        self.dom = dict_decode(list(dec), list(self.body))
        return self.dom

        """
        self.dom = dict_decode(list(dec), list(self.body))
        return self.dom

    def get_rid(self):
        return self.header.get(RID_HEADER)

    def get_handler_code(self):
        """return the mid seaching in self._fields"""
        return self.header["code"]


class Response(Future, Message):
    """Message that can be used as a *Future* value."""

    def __init__(self, loop, req, meta, rid, **kw):
        Future.__init__(self, loop=loop)
        Message.__init__(self, **kw)
        self.req = req
        self.meta = meta
        self.rid = rid

        # prepare body 'holder' based on response type
        klass = meta[1]
        if klass:
            self.body = klass()
        else:
            self.body = klass

    def feed(self, message):
        pass  # raise NotImplementedError("override")

    def completed(self, result=RESPONSE_NO_DATA):
        if not self.done():
            if not self.body:
                if result == RESPONSE_NO_DATA:
                    self.body = self.dom
                else:
                    self.body = result
            self.set_result(self.body)
        else:
            foo = 1
        return self

    def _get_mid(self):
        """return the mid seaching in self._fields"""
        return "default"


# --------------------------------------------------------------------
# Dispatcher
# --------------------------------------------------------------------
class Dispatcher(iLog):
    """Dispatcher Base class.

    This class create a map of handlers functions
    to be fired on incoming events.

    Features:

    - 3rd party message codes to human ID mapping using paths
    - handler subtypes: error handler, etc.
    - some automation mapping members to event codes

    This class must be derived and implement a '_dispatch()' method


    """

    #: define the messages that are checked and will be not
    #: traced or paused in debugger.
    DEBUG_IGNORE_MID_IN = set([])
    DEBUG_IGNORE_MID_OUT = set([])

    #: The default incoming class used as holder of the new
    #: incoming message from peer
    INCOMING_KLASS = Message

    #: Human MSG_ID mapping.
    #: Maps the messages *mid* codes with a internally
    #: portable *path* incoming request.
    #: This unify custom protocol messages with more
    #: generalized *paths* that will be handled by app.
    #: so different protocols may be handled wit the same
    #: callback function with minors cares.
    in_mapping = {
        # IN.MANAGED_ACCTS: '/accounts', # 15
    }

    #: This is is the map for printing incoming *mid* human names.
    incoming_mid_name = {}

    #: This map define the parser for each incoming message.
    #: messages are sorted for easily add new ones
    #: [retire, dom-path, types]
    extract = {
        "default": (True, "", (("payload", str),)),
    }

    def __init__(self, dom=None, **env):
        super().__init__()
        self.handler = {}
        self._handler_code = {}

        # Dom and Info
        self.env = env
        if dom is None:
            dom = Dom()
            self.dom = dom
        self.dom = dom

    # ----------------------------------
    # Dispatcher
    # ----------------------------------
    def _compile(self):
        # compile templates
        template = {}
        for key, (
            rid,
            body,
            pattern,
            extra,
            callbacks,
            tracking,
        ) in self.template.items():
            callbacks = tuple([getattr(self, cb) for cb in callbacks])
            template[key] = (rid, body, pattern, extra, callbacks, tracking)
        self.template = template

        # link error code handlers
        rexp = re.compile(r"_handler_code_(?P<code>\d+)(_(?P<text>.*)$)?")
        for name in dir(self):
            m = rexp.match(name)
            if m:
                d = m.groupdict()
                code, text = int(d["code"]), d["text"]
                if text:
                    text = text.replace("_", "\s+")

                # print(f" + handle [{code}]({text})")
                handlers = self._handler_code.setdefault(code, dict())
                handlers[text] = getattr(self, name)

    def _dispatch(self, msg, debug=True):
        """Try to dispatch a completed incoming message.
        A waiting response may need several messages to
        be 100% complete (e.g. HTTP 206 partials)
        """
        mid = msg.get_handler_code()
        if mid not in self.DEBUG_IGNORE_MID_IN:
            foo = 1

        if mid in (14,):
            # print (f">> received mid: {mid}")
            foo = 1  # news bulleting

        # parse message
        path = self.in_mapping.get(mid, mid)
        retire, dom_patch, dec = self.extract.get(path) or self.extract["default"]
        dom = msg.parse(dec)
        # debug:
        if debug:
            if mid not in self.DEBUG_IGNORE_MID_IN:
                print("-" * 30)
                print(f"<<< {self.incoming_mid_name[mid]} : # {mid}")
                print("-" * 30)
                for key, value in dom.items():
                    try:
                        value = str(value)
                        print(f"< {key:12} := {value[:30]} ({len(value)}) bytes")

                    except Exception:
                        value = "(unable to convert value to string"
                        print(f"< {key:12} := {value[:30]} ('??') bytes")
                        foo = 1

        rid = msg.get_rid()  # we need to compute rid BEFORE calling handler
        rid = self.handler[mid](msg) or rid

        # try to find any waiting response
        # related to the just incoming message

        # getting the last rid sent as fallback value
        # rid = msg.get_rid() # or self._next_rid

        # and feed the waiting response (if any)
        # TODO: check if must remove the request or not
        res = self.waiting.get(rid)

        # try to complete and update DOM
        if dom_patch is not None:  # TODO: relative path apply
            env = dict(self.env)
            if res:
                env.update(res.req)
            env.pop("path", None)
            # t0 = time.time()
            # aux1 = copy.deepcopy(msg.dom)
            # t1 = time.time()
            # we need to *isolate* msg.dom
            # because patch may alter msg.dom
            # and client side may expect msd.dom still be
            # unmodified
            # pickle is around 50 times faster than deepcopy
            aux2 = pickle.loads(pickle.dumps(msg.dom))
            # t2 = time.time()
            # e1 = t1 - t0
            # e2 = t2 - t1

            self.dom.patch(path, dom_patch, aux2, **env)

        if res:
            res.feed(msg)  # try to complete
            if retire:
                # Mark fo deletion and not retire inmediately
                # This allows to receive 'post-errors' related
                # to the same reques before it is theoretical
                # finished (e.g. cancel a subscription that is not
                # really subscribe, etc)
                res.header[DELETE_AT] = self.time + 1
                # res = self.waiting.pop(rid)
                res.completed(dom)

    def _populate_handlers(self):
        """Populate incoming messages handlers.
        TODO: populte most by instrospection and regexp
        """
        self.handler[None] = self._nop

    def parse(self, msg):
        """Parse raw and generaty a body (payload)"""
        assert False, "retire"
        path = self.in_mapping.get(msg.get_handler_code())
        types = self.extract.get(path) or self.extract["default"]
        dom = msg.parse(types)
        # print(f"  - result: {dom}")

    def g(self, path, **env):
        """Get an item from DOM."""
        env = self.env
        env.pop("path", None)
        return self.dom.g(path, **env)

    # ---------------------------------------------------
    # handlers
    # ---------------------------------------------------
    def _nop(self, msg):  # None
        "do nothing handler"


# --------------------------------------------------------------------
# Requester
# --------------------------------------------------------------------


class Requester:
    """Base class for agents that can send requests and wait for them."""

    #: The default response class used as holder of any data
    #: received and processed by protocol Dispatcher.
    RESPONSE_KLASS = Response

    #: This is is the map for printing outgoing *mid* human names.
    outgoing_mid_name = {}

    #: render tenplates for outgoing messages
    template = {}

    def __init__(self, name, executor=None, loop=None, **env):
        self.name = name
        self.executor = executor

        # Waiting responses and Progress Tracking
        self.waiting = {}  # responses in waiting to be filled
        self.oob_waiting = {}  # special cases before fisnish a request
        self._tracking = Progress()

        # Loop
        self.loop = None  # get_running_loop()
        if loop:
            self._set_loop(loop)

    def _set_loop(self, loop):
        self.loop = loop
        # for name in "handshaking", "disconnection":
        # assert getattr(self, name) is None, "must be defined prior set"
        # setattr(self, name, loop.create_future())

    # -----------------------------------------------
    # Public API: get/post/cancel
    # -----------------------------------------------

    async def get(self, url, **req):
        # assert self.handshaking.done()
        req = self._create_request(url, **req)
        res = await self._send(req)
        # if res and self.dom is not None:
        # self.dom.update(res.result().body)
        return res

    async def _get_generic(self, **req):
        """Performs a generic GET request trying to minimize
        user code.

        REQ path is guessed by name of calling funcion.

        TODO: regexp extract sub-paths
        TODO: use this trick for 'cancel' or sub-specialize 'paths'
        """
        args = "&".join([f"{k}={v}" for k, v in req.items()])
        path = req.get("path")
        if path is None:
            func = get_calling_function(2)
            m = re.match(r"(?P<cmd>[^_]*)_(?P<path>.*)", func.__name__)
            if m:
                d = m.groupdict()
                soft(req, **d)
            else:
                raise RuntimeError(
                    f"You can not call _get_generic from {func}."
                    "Review func name format to match: cmd_path(_sub_paths)?"
                )

            # path is relative here, so we add a initial ''
            path = [""] + req["path"].split("_")
            req["path"] = "/".join(path)
        else:
            soft(req, cmd="get")

        sub_path = req.get("sub_path")
        if sub_path:
            path = req["path"].split("/")
            path.extend(sub_path.split("_"))
            req["path"] = "/".join(path)

        url = req["path"]
        if args:
            url = f"{url}?{args}"

        # TODO: use command here: get, post, cancel, etc.
        func = getattr(self, req["cmd"])
        result = await func(url)
        return result

    async def post(self, url):
        raise RuntimeError("need overriding")

    async def cancel(self, url, **req):
        # assert self.handshaking.done()
        req = self._create_request(url, **req)
        rid = self._find_request(url, **req)

        req["path"] = f"{req['path']}/cancel"
        req["rid"] = rid

        res = await self._send(req)
        # if res and self.dom is not None:
        # self.dom.update(res.result().body)
        return res

    async def _send(self, req):
        """Create a request message to peer.

        Handles:

        - when need a response.
        - duplicated requests (searching in cache for a valid time)

        """
        # get request meta-info
        meta = self.template.get(req["path"]) or self.template["default"]
        wait, body, template, extra, callbacks, tracking = meta
        soft(req, **extra)

        # check fo duplicated requests
        # we use 1st raw generation to get the hash code
        # (skipping rid as is unknown at this point)
        raw = self._render_request(req, template)
        sign = hashlib.md5(raw).hexdigest()
        crid = self._cache.get(sign)
        if crid:  # TODO: is a 'alive-cache' indeed !
            print("REUSING an alive request with same parameters")
            # same request still exists in cache.
            # Don't duplicate request
            return self.waiting.get(crid)

        # send request to remote peer
        if wait:
            # need to create a new response holder and raw data
            rid = self._new_rid(sign)
            req[RID_HEADER] = req["rid"] = rid
            res = self._create_response(req, meta, rid)

            # track request if needed
            status = self._track_request(req, meta)
            res.header[PROGRESS_CONTROL] = status

            raw = self._render_request(req, template, debug=True)
            self._write(raw)
            # wait for response to be completed
            # or continue in case of stream subscription
            if wait > 0:
                # TODO: more general in meta
                res.header[TIMEOUT_AT] = self.time + 20
                await res
            return res
        else:
            raw = self._render_request(req, template)
            self._write(raw)

    # -----------------------------------------------
    # Tracking Responses
    # -----------------------------------------------
    def _track_request(self, req, meta):
        """
        chackout if tracking info is passed:
        - _pos_ = {name of param as cursor or value}
        - _start_ = {name or value}
        - _end_ = {name or value}
        - _ignore_ = list of any additional value that must be ignored for
                   create the hash key of request.

        When _start_ or _end_ is passed, create or update tracker
        when _pos_ is passed, updat the tracking position

        Tracker position is added in response instance to be checker
        by user at the end of request.


        """

        def resolve(name):
            try:
                value = req.get(name)
                value = req.get(value) or eval(value)
                return value
            except:
                pass

        pos = resolve("_pos_")
        if pos is not None:
            start = resolve("_start_")
            end = resolve("_end_")

            # create a 'hash' url as key for progress task
            ignore = set(req.get("_ignore_", []))
            ignore.update(meta[-1].values())  # some known 'volatile' params
            tmp = {k: v for (k, v) in req.items() if not (k in ignore or k[0] == "_")}

            # remove all known 'volatile' params
            query = tmp["query"] = {}
            for k, v in tmp["query_"].items():
                if not (k in ignore or k[0] == "_"):
                    query[k] = v
            url = build_uri(**tmp)

            if start is not None:
                status = self._tracking.get(url)
                if not status:
                    status = self._tracking.add(url, p0=start, p2=end)
            else:
                status = self._tracking.get(url)

            if status:
                status.update(pos)
                print(f"Tracking: {status}: task: {url}")
            else:
                print(f"Tracking not found for {url}")
            return status

        # try:
        # extractor = meta[-1]
        # progress = { k: req.get(v, '') for k, v in extractor.items() }
        # line = '. '.join([ f"{k}: {progress[k]}" for k in extractor ])
        # print(f"{line}")
        # except Exception as why:
        # print(f"{why}")
        foo = 1

    # -----------------------------------------------
    # Executor / Transort
    # -----------------------------------------------
    # def connect_executor(self, executor):
    # assert isinstance(executor, Executor)
    # self.executor = executor
    # self._set_handshaking_requirements()

    # -----------------------------------------------
    # Internal
    # -----------------------------------------------
    def _render_request(self, req, template, debug=False):
        """Render the request based on template protocol definition."""
        self._expand_request(req)

        raw = self.encoder(template.format(**req))
        req["raw"] = raw

        return raw

    def _expand_special_fields(self, data):
        return data

    def _create_request(self, url, _message_klass=None, **req):
        if _message_klass:
            self._change_message_klass(_message_klass)

        soft(req, **parse_uri(url))
        soft(req, **self.env)
        req["_url_"] = url

        return req

    def _find_request(self, url="", **req):
        url_ = parse_uri(url)
        soft(req, **url_)

        # get request meta-info
        meta = self.template.get(req["path"]) or self.template["default"]
        wait, body, template, extra, callbacks, tracking = meta
        soft(req, **extra)

        # check fo duplicated requests
        # we use 1st raw generation to get the hash code
        # (skipping rid as is unknown at this point)
        raw = self._render_request(req, template)
        sign = hashlib.md5(raw).hexdigest()
        crid = self._cache.get(sign)
        return crid

    def _expand_request(self, req):
        req = self._expand_special_fields(req)

    def _create_response(self, req, meta, rid=None, klass=None):
        """Create a reponse holder instance waiting for remote peer answer.

        A different response class can be passed for different response
        behavior.

        User can predefined the rid to be used if procotol needs it
        or generate a new one internally.
        """
        klass = klass or self.RESPONSE_KLASS
        self.waiting[rid] = res = klass(
            api=self, loop=self.loop, req=req, meta=meta, rid=rid
        )
        return res

    def _new_rid(self, sign):
        """Generate a new rid based on signature.

        Depending on protocol, sign can be used as rid (e.g. HTTP)
        or more generally we need to create a new one (e.g. TWS)
        """
        self._next_rid += 1

        rid = self._next_rid
        self._cache[sign] = rid  # TODO: drop done responses (timeout or direct drop)

        return rid

    def _change_message_klass(self, klass):
        assert issubclass(klass, Message)
        self.INCOMING_KLASS = klass


# --------------------------------------------------------------------
# Worker
# --------------------------------------------------------------------
WORKER_EXIT = "exit"


class Worker(Requester, Dispatcher):
    """Represent a worker abstraction.
    All workers share an unique context to communicate themselves

    """

    # [Response-Klass, Template, default-parameters]
    template = {
        "default": (
            RESPONSE_NONE,
            None,
            """No render templates has been defined.""",
            {},
        ),
    }

    ctx = dict()

    @classmethod
    def clear(cls):
        "Clear the shared context"
        cls.ctx.clear()

    def __init__(self, **env):
        self.reactor = None

        Requester.__init__(self, **env)
        Dispatcher.__init__(self, **env)

        self.delay = 1
        self.running = False
        self.finished = False

        # hooks
        self._hooks = {}

    def attach(self, runner=None):
        runner = runner or self
        self.reactor.attach(runner)

    def detach(self, runner=None):
        runner = runner or self
        self.reactor.detach(runner)

    @property
    def time(self):
        return self.reactor.time

    async def main(self):
        """Main loop of worker

        - Create a check task for self-health supervision.
        - While reactor is running:
            - check if there are slots and pending task for execution
            - add task to loop
        """
        self.running = True
        self.finished = False
        # print(f"[{self.name}] >> main")
        await self._enter()
        while self.running:
            await self._do()
            await sleep(self.delay)
        await self._exit()
        self.finished = True

    async def _enter(self):
        # print(f"[{self.name}] Enter")
        if not self.loop:
            self._set_loop(get_running_loop())

    async def _do(self):
        """The main fiber for a base Worker."""

        # 1. Check for responses mark as 'dead'
        t0 = self.time
        for rid, res in list(self.waiting.items()):
            # print(f"Checking: {rid} timeout/deletion ...")
            if res.header.get(TIMEOUT_AT, t0) < t0:
                print(f"*** TIMEOUT for rid: {rid} !! (TODO: fire callbacks !!)")
                self.waiting.pop(rid)

            elif res.header.get(DELETE_AT, t0) < t0:
                # print(f"-- remove {rid} response ...")
                self.waiting.pop(rid)
                # drop signature cache

            await sleep(self.delay)

        # 2. Drop any signature that is not longer valid
        for sign, rid in list(self._cache.items()):
            if rid not in self.waiting:
                # print(f"-- remove {rid} signature: {sign} ...")
                self._cache.pop(sign)
                continue
            await sleep(self.delay)

    async def _exit(self):
        # print(f"[{self.name}] Exit")
        self._hook(WORKER_EXIT)
        self.detach()

    def stop(self):
        """Stop the worker"""
        # print(f"[{self.name}] Stopping {self.__class__.__name__}")
        self.running = False

        # uncomment
        # self.reactor.workers.pop(self)
        # will cause:
        # File "/home/agp/Documents/me/code/uswarm/uswarm/reactor.py", line 1639, in stop
        # for worker in self.workers:
        # File "/usr/lib/python3.9/weakref.py", line 460, in keys
        # for wr in self.data:
        # RuntimeError: dictionary changed size during iteration

    def add_hook(self, hook, func, *args, **kw):
        kw.setdefault("worker", self)
        self._hooks.setdefault(hook, list()).append(tuple([func, args, kw]))

    def _hook(self, hook, *args, **kw):
        for regexp, (func, args_, kw_) in self._hooks.items():
            if re.match(regexp, hook):
                _kw = dict(kw_)
                _kw.update(kw)
                _args = args or args_
                scall(func, *_args, **_kw)

    # Some execution policies
    def parallel(self, _max_=10, timeout=1000, **tasks):
        """
        1. create a running and pending task queues.
        2. while pending and running:
        3. try to start new tasks if we have room
        4. wait until any task is finished.
        5. save results
        6. return results dict
        """
        loop = self.loop
        todo = {ensure_future(f, loop=loop): url for url, f in tasks.items()}
        timeout_handle = None

        from asyncio.queues import (
            Queue,
        )  # Import here to avoid circular import problem.

        done = Queue(loop=loop)

        def _on_timeout():
            for f in todo:
                f.remove_done_callback(_on_completion)
                done.put_nowait(None)  # Queue a dummy value for _wait_for_one().
            todo.clear()  # Can't do todo.remove(f) in the loop.

        def _on_completion(f):
            if not todo:
                return  # _on_timeout() was here first.
            url = todo.pop(f)
            done.put_nowait((url, f))
            if not todo and timeout_handle is not None:
                timeout_handle.cancel()

        async def _wait_for_one():
            url, f = await done.get()
            if f is None:
                # Dummy value from _on_timeout().
                raise exceptions.TimeoutError
            return url, f.result()  # May raise f.exception().

        for f in todo.keys():
            f.add_done_callback(_on_completion)

        if todo and timeout is not None:
            timeout_handle = loop.call_later(timeout, _on_timeout)

        for _ in range(len(todo)):
            yield _wait_for_one()


# --------------------------------------------------------------------
# Executor: # TODO: delete?
# --------------------------------------------------------------------


class Executor:
    """
    TODO: delete ?
    Execute commands ...
    """

    def __init__(self, **env):
        pass


# --------------------------------------------------------------------
# Reactor
# --------------------------------------------------------------------


class Reactor(Worker):
    """Reactor handles the execution of coroutines allowing
    only a number of maximum running at the same time.
    """

    def __init__(self, name="<undefined reactor>", max_active: int = 20, **kw):
        super().__init__(name=name, **kw)
        self.active = wdict()
        self.workers = wdict()
        self.pending = []
        self.max_active = max_active
        self.t0 = 0

    def attach(self, runner):
        """Add a coroutine to queue execution"""
        if isinstance(runner, Worker):
            # can be re-entrant, but when is
            # finished
            assert not runner.running or runner in self.workers

            if runner.finished:
                self.warn(f"reusing [{runner.name}] worker after finished")
                if runner.reactor != self:
                    self.warn(
                        f"reused [{runner.name}] was running on another reactor"
                        f"[{runner.reactor.name}] instead current [{self.name}]"
                    )

            if runner not in self.workers:
                if runner.finished:
                    self.warn(f"reusing [{runner.name}] worker after finished")

                self.workers[runner] = True
                runner.reactor = self
                self.warn(f"adding [{runner.name}] to [{self.name}]")
                self.pending.append(runner.main())
            # print(f"[{self.name}] Add pending Worker: {runner}")
            else:
                self.warn(f"Skipping: [{runner.name}] is already on [{self.name}]")
                foo = 1
        else:
            # print(f"[{self.name}] Add pending task: {runner}")
            self.pending.append(runner)
        self.delay = 0.5

    def detach(self, runner=None):
        """Remove a coroutine to queue execution"""
        runner = runner or self
        if runner in self.workers:
            if isinstance(runner, Worker):
                # can be re-entrant, but when is
                # finished
                self.workers.pop(runner)
                # runner.reactor = self
                self.warn(f"detaching [{runner.name}] from [{self.name}]")
                # self.pending.append(runner.main())
                # print(f"[{self.name}] Add pending Worker: {runner}")
            else:
                self.warn(f"detaching [{runner}] from [{self.name}]")
                self.pending.pop(runner, None)
        elif self.reactor:
            # check if runner is running in parent reactor
            # (i.e. nested reactors)
            self.reactor.detach(runner)
        else:
            foo = 1
            self.warn(f"Ignoring detach [{runner.name}] from [{self.name}]")

        # self.delay = 0

    async def _enter(self):
        # print(f">> {self}: enter")
        await super()._enter()
        self.attach(self.check())
        self.delay = 0

    async def _do(self):
        while self.pending and len(self.active) < self.max_active:
            coro = self.pending.pop()
            task = create_task(coro)
            task = ensure_future(task)
            self.active[task] = True  # add to running tasks
            # print(f"[{self.name}] Create new task: {coro}")
        else:
            self.delay = min(self.delay + 0.1, 1.0)

    async def _exit(self):
        await super()._exit()
        timeout = self.time + 10
        l = 1
        while self.time < timeout and l > 0:
            await sleep(self.delay)
            l = len([w for w in self.workers if not w.finished])
            # print(f"[{self.name}] waiting for {l} workers")
        # print(f"[{self.name}] exit with {l} workers")
        foo = 1

    async def check(self):
        """Check health and whenever Reactor may stop.

        TODO: Review, workers attached to reactor running
        default main() fiber may run forever until they want
        to stop. Reactor can not guess when its workers shoul
        stop ot not (Reactor don't know anything about Worker
        nature).

        Reactor must stop when only self-check fiber is running.

        """
        repeat = countdown = 3
        # system_coros = self.main, self.check
        system_coros = (self.check,)

        system_codes = set([coro.__func__.__code__ for coro in system_coros])
        while self.running:
            await sleep(self.delay)

            # purge all done Future (Tasks) items
            pending_codes = set()
            for coro in list(self.active):
                assert isinstance(coro, Future), "coros must be wrapped into Tasks"
                if coro.done():
                    self.active.pop(coro)

            # check if only system_coros are running in reactor
            pending = list(self.active) + self.pending
            # codes = [aws.get_coro().cr_code for aws in pending]

            if len(pending) <= len(system_coros):
                assert len(self.pending) == 0
                pending_codes = set([coro.get_coro().cr_code for coro in self.active])

                if pending_codes.issubset(system_codes):
                    countdown -= 1
                    if countdown <= 0:
                        print(f"[{self.name}] no more fibers running")
                        self.running = False
            else:
                countdown = repeat

    async def main(self, *tasks):
        # print(f">> main: {self}")
        self.t0 = get_event_loop().time()
        # TODO: do not launch tasks until reactor is
        # TODO: ready and running (in _do loop)
        for task in tasks:
            self.attach(task)
        await gather(self._boostrap_fibers())

    def _boostrap_fibers(self):
        """Return ALL the fibers that reactor starts with"""
        return super().main()

    def run(self, *tasks):
        """Main entry point from outside loop"""
        # print(f">> run")
        return run(self.main(*tasks), debug=False)
        # print(f"<< run")

    def stop(self):
        """Stop the reactor and any child"""
        # print(f">> {self}: stop")

        if self.running:
            for worker in self.workers:
                worker.stop()
            super().stop()

    @property
    def time(self):
        return self.loop.time() - self.t0


# --------------------------------------------------------------------
# Sequencer
# --------------------------------------------------------------------


class Sequencer(Worker):
    """TODO: review ??"""

    def __init__(self, name="<undefined worker>", **env):
        # TODO: review constructor
        super().__init__()
        self.progress = Progress()

    async def _do(self):
        """The main fiber for a Sequencer."""
        for task in self._tasks():
            self._dispatch(task)

    def _tasks(self):
        for task in product(["A", "B"], [0, 1, 2, 3]):
            yield task
