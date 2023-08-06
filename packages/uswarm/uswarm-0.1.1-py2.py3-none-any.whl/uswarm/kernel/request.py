import hashlib
import random
import re
from time import time

from uswarm.tools import (
    build_uri,
    get_blueprint,
    get_calling_function,
    parse_uri,
    soft,
)

# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger

log = logger(__name__)


def _signature(req):
    raw = bytes(str(req), "utf-8")
    return hashlib.md5(raw).hexdigest()


# ------------------------------------------------
# I/O Events / Messages / Channels
# ------------------------------------------------

DEFAULT_TIMEOUT = 9900  # 60 # 120 # 900 for debug

RID_HEADER = "rid"
NOT_VALID_ID = "x-not-valid-id"
DELETE_AT = "x-delete-at"
TIMEOUT_AT = "x-timeout-at"
REQ_TIMEOUT = "request-timeout"
REPLY_TO = "reply-to"
REPLY_FROM = "reply-from"
SERVER = "server"
X_COMMAND = "cmd"

TIMEOUT_CALLBACKS = "x-timeout-callbacks"
PARTIAL_KEY = "x-partial-Key"
DONT_INDEX = "x-do-not-index"
PROGRESS_CONTROL = "x-progress-control"

RESPONSE_NONE = 0
RESPONSE_SINGLE = 1
RESPONSE_MULTIPLE = 2

RESPONSE_SUBSCRIPTION = -1
RESPONSE_NO_DATA = "<no-data>"

# special headers (taken from RFC-2616)
CONTENT_LENGTH = "content-length"
X_CONTENT_LENGTH = "x-content-length"

CONTENT_ENCODING = "content-encoding"
CONTENT_TYPE = "content-type"

# base class for message interchange
Message = dict

EVENT_REQUEST = "<request>"
EVENT_RESPONSE = "<response>"
EVENT_TIMEOUT = "<timeout>"
X_EVENT = "x-event"
X_WAVE = "x-wave"

REPLY_TO_REQUEST = "reply-to-request"
RESEND_AGAIN = "resend-again"
REPLY_TO_WAVE = "reply-to-wave"


class iRequester:
    """Base interface for agents that can send requests and wait for them."""

    RESPONSE_KLASS = Message
    #: render tenplates for outgoing messages
    META_REQUEST = {  # TODO: change to "render"
        "default": (
            RESPONSE_SINGLE,
            dict,  #: container
            "",  #: no serialization render
            {},  #: default render params
            (),  #: callbacks
            {"current": "end"},  #: tracking
        ),
        # "/account/position": (
        # RESPONSE_MULTIPLE,
        # dict,
        # "{idx}\0{version}\0{rid}\0" "{account}\0{model_code}\0",
        # {
        # "idx": OUT.REQ_POSITIONS_MULTI,
        # "version": 1,
        # "rid": 0,
        # "account": "",  # TODO: checks if can be blank
        # "model_code": "",
        # },
        # (),
        # {"current": "end"},
        # ),
    }

    BLUEPRINT_KEYS = set(
        [
            "path",
        ]
    )

    uri: str

    def __init__(self):
        # self._uri = {}  # TODO: review
        # Waiting responses and Progress Tracking
        self._next_rid = 100
        # self._next_rid = random.randint(100, 1500)
        self.waiting = {}  # responses in waiting to be filled
        self._cache = {}

    @property
    def pending_responses(self):
        waiting = getattr(self, "waiting", {})
        return {rid: res for rid, res in waiting.items() if not res.get(DELETE_AT)}

    @property
    def pending_blueprints(self):

        pending = {}
        for rid, res in self.pending_responses.items():
            req = res.get('req')
            if req:
                pending[get_blueprint(req, self.BLUEPRINT_KEYS)] = rid
            else:
                foo = 1

        return pending

    # -----------------------------------------------
    # Public API: post/cancel
    # -----------------------------------------------

    def request(self, url, **req):
        req = self._create_request(url, **req)
        res = self._send(req)
        return res

    def answer(self, res):
        raise NotImplementedError()

    def cancel(self, url, **req):
        """Request a cancelation on an already send request."""
        req = self._create_request(url, **req)
        rid = self._find_request(url, **req)

        req["path"] = f"{req['path']}/cancel"
        req["rid"] = rid

        res = self._send(req)
        # TODO: remove from waiting responses?
        return res

    def _create_request(self, url, **req):
        """Create an unify request dict container based on keywords and uri."""

        _url = parse_uri(url)
        _url.update(_url.get("query_", {}))
        soft(req, **_url)
        soft(req, **self._uri)
        req["_url_"] = url

        self._expand_request(req)

        return req

    def _send(self, req):
        """Create a request message for peer.

        Handles:

        - when need a response.
        - duplicated requests (searching in cache for a valid time)

        """
        # get request meta-info
        meta = self.META_REQUEST.get(req["path"]) or self.META_REQUEST["default"]
        wait, body, template, extra, callbacks, tracking = meta
        soft(req, **extra)

        sign = _signature(req)
        rid = self._new_rid(sign)
        req[RID_HEADER] = req["rid"] = rid

        # check fo duplicated requests
        # we use 1st raw generation to get the hash code
        # (skipping rid as is unknown at this point)
        # raw = self._render_request(req, template, debug=False)
        # sign = hashlib.md5(raw).hexdigest()
        crid = self._cache.get(sign)
        if False and crid:  # TODO: is a 'alive-cache' indeed !
            print("REUSING an alive request with same parameters")
            # same request still exists in cache.
            # Don't duplicate request
            return self.waiting.get(crid)

        self._cache[sign] = rid  # TODO: drop done responses (timeout or direct drop)

        # send request to remote peer
        self.write(req)

        if wait:
            # need to create a new response holder and raw data
            res = self._create_response(req, meta, rid)

            # track request if needed
            # status = self._track_request(req, meta)
            # res[PROGRESS_CONTROL] = status

            # wait for response to be completed
            # or continue in case of stream subscription
            if wait > 0:
                res[TIMEOUT_AT] = time() + req.get(REQ_TIMEOUT, DEFAULT_TIMEOUT)
            return res

    def _expand_request(self, req):
        """Add extra values to request for providing extra keywords
        that are located outside request itself such results from
        previous responses or storage.

        i.e. contract internal ids from local_symbol

        """
        foo = 1

    def _new_rid(self, sign):
        """Generate a new rid based on signature.

        Depending on protocol, sign can be used as rid (e.g. HTTP)
        or more generally we need to create a new one (e.g. TWS)
        """
        self._next_rid += 1
        rid = self._next_rid

        return rid

    def _create_response(self, req, meta, rid=None, klass=None):
        """Create a reponse holder instance waiting for remote peer answer.

        A different response class can be passed for different response
        behavior.

        User can predefined the rid to be used if procotol needs it
        or generate a new one internally.
        """
        klass = klass or self.RESPONSE_KLASS
        self.waiting[rid] = res = klass(req=req, meta=meta, rid=rid)
        return res

    def _render_request(self, req, debug=False):
        """Render the request based on template protocol definition."""
        return req

    def write(self, req):
        """Append data in the outgoing queue.
        It also request kernel to wakeup writing ASAP.
        """
        assert isinstance(req, Message)

        data = self._render_request(req, debug=True)
        self._write(data)

    def _write(self, data):
        """Append data in the outgoing queue.
        It also request kernel to wakeup writing ASAP.
        """
        raise NotImplementedError()

    def _get_generic(self, **req):
        """Performs a generic GET request trying to minimize
        user code.

        REQ path is guessed by name of calling funcion.

        TODO: regexp extract sub-paths
        TODO: use this trick for 'cancel' or sub-specialize 'paths'
        """
        # path = req.setdefault("path", None)
        if req.get("path") is None:
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
            soft(req, cmd="request")

        sub_path = req.get("sub_path")
        if sub_path:
            path = req["path"].split("/")
            path.extend(sub_path.split("_"))
            req["path"] = "/".join(path)

        url = req["path"]
        # compute 'args' before guessing path, so 'path' will not
        # appears on parameters query.
        args = "&".join([f"{k}={v}" for k, v in req.get("query_", {}).items()])

        if args:
            url = f"{url}?{args}"

        # TODO: use command here: get, post, cancel, etc.
        func = getattr(self, req["cmd"])
        res = func(url, **req)
        return res

    def _find_request(self, url="", **req):
        url_ = parse_uri(url)
        soft(req, **url_)

        # get request meta-info
        meta = self.META_REQUEST.get(req["path"]) or self.META_REQUEST["default"]
        wait, body, template, extra, callbacks, tracking = meta
        soft(req, **extra)

        # check fo duplicated requests
        # we use 1st raw generation to get the hash code
        # (skipping rid as is unknown at this point)
        raw = self._render_request(req, template)
        sign = hashlib.md5(raw).hexdigest()
        crid = self._cache.get(sign)
        return crid

    # ---??---------------------------------------------------------

    # -----------------------------------------------
    # Tracking Responses
    # -----------------------------------------------
    def _track_request(self, req, meta):
        """
        check if tracking info is passed:
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

    # Events
    # -----------------------------------------------

    def on_timeout(self, event, data, wave=None, *args, **kw):
        pass


## ---------------------------------------------------
## handlers
## ---------------------------------------------------
# def _nop(self, msg):  # None
# "do nothing handler"
