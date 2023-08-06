from .request import *
from .stm import *
from .kernel import (
    BASE_TIMER,
    BASE_TIMER_EVENT,
    DOMESTIC_TIMER,
    DOMESTIC_TIMER_EVENT,
    LONG_TIMER,
    LONG_TIMER_EVENT,
    SYS_GENERAL_BUS,
    EVENT_STATUS_CHANGED,
    EVENT_RESOURCE_ERROR,
    EVENT_RESOURCE_WARNING,
    EVENT_RESOURCE_INFO,
    EVENT_RESOURCE_PACING,
)

# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger

log = logger(__name__)

# ------------------------------------------------
# Definitions
# ------------------------------------------------
EVENT_CHILD_RESPONSE = "<child-response>"


class uServer(PSTM, iRequester):
    META_RESPONSE = {
        # Just for debugging
        "default": (True, "", {}),
    }

    def __init__(self, uri, kernel, *args, **kw):
        super().__init__(uri, kernel, *args, **kw)
        iRequester.__init__(self)

        # function handlers
        self.msg_handler = {}
        self._handler_error_code = {}
        self._resolve_callbacks()
        self._populate_msg_handlers()

        # Timers subscription
        self.subscribe(BASE_TIMER)
        self.subscribe(LONG_TIMER)
        self.subscribe(DOMESTIC_TIMER)
        self.subscribe(SYS_GENERAL_BUS)

        # TODO: review
        self.dom = self.kernel.dom
        
        

    # -----------------------------------------------
    # Layer definitions
    # -----------------------------------------------
    def _setup_012_sys_notification(self):
        """Set TERM and QUIT logic for the base layer."""
        states = {}

        transitions = {
            EVENT_STATUS_CHANGED: {
                STATE_LIVE: [
                    [STATE_LIVE, [], ["sys_status_changed"]],
                ],
            },
            EVENT_RESOURCE_ERROR: {
                STATE_LIVE: [
                    [STATE_LIVE, [], ["sys_resource_error"]],
                ],
            },
            EVENT_RESOURCE_WARNING: {
                STATE_LIVE: [
                    [STATE_LIVE, [], ["sys_resource_warning"]],
                ],
            },
            EVENT_RESOURCE_INFO: {
                STATE_LIVE: [
                    [STATE_LIVE, [], ["sys_resource_info"]],
                ],
            },
        }

        return states, transitions, MERGE_ADD

    # -----------------------------------------------
    # Layer definitions
    # -----------------------------------------------
    def _setup_012_sys_pacing(self):
        """Set TERM and QUIT logic for the base layer."""
        states = {}

        transitions = {
            EVENT_RESOURCE_PACING: {
                STATE_LIVE: [
                    [STATE_LIVE, [], ["sys_pacing"]],
                ],
            },
        }

        return states, transitions, MERGE_ADD

    def _setup_025_timers(self):
        """Set TERM and QUIT logic for the base layer."""
        states = {}

        transitions = {
            BASE_TIMER_EVENT: {
                STATE_LIVE: [
                    [STATE_LIVE, [], ["on_timer"]],
                ],
            },
            LONG_TIMER_EVENT: {
                STATE_LIVE: [
                    [STATE_LIVE, [], ["on_long_timer"]],
                ],
            },
        }

        return states, transitions, MERGE_ADD

    def _setup_035_domestic_timers(self):
        """Set TERM and QUIT logic for the base layer."""
        states = {}

        transitions = {
            BASE_TIMER_EVENT: {
                STATE_LIVE: [
                    [STATE_LIVE, [], ["on_domestic"]],
                ],
            },
        }

        return states, transitions, MERGE_ADD

    def _setup_050_request_response(self):
        """Set TERM and QUIT logic for the base layer."""
        states = {}

        transitions = {
            EVENT_REQUEST: {
                STATE_LIVE: [
                    [STATE_LIVE, [], ["on_request"]],
                ],
            },
            EVENT_RESPONSE: {
                STATE_LIVE: [
                    [STATE_LIVE, [], ["on_response"]],
                ],
            },
        }

        return states, transitions, MERGE_ADD

    def _setup_051_child_responses(self):
        """Set TERM and QUIT logic for the base layer."""
        states = {}

        transitions = {
            EVENT_CHILD_RESPONSE: {
                STATE_LIVE: [
                    [STATE_LIVE, [], ["on_child_response"]],
                ],
            },
        }

        return states, transitions, MERGE_ADD

    def _setup_027_term_nicely(self):
        """Control which events must be attended in STATE_TERM state."""
        states = {}

        transitions = {
            EVENT_CHILD_RESPONSE: {
                STATE_TERM: [
                    [STATE_TERM, [], ["on_child_response"]],
                ],
            },
            EVENT_REQUEST: {
                STATE_TERM: [
                    [STATE_TERM, [], ["on_request"]],
                ],
            },
            EVENT_RESPONSE: {
                STATE_TERM: [
                    [STATE_TERM, [], ["on_response"]],
                ],
            },
        }

        return states, transitions, MERGE_ADD

    # --------------------------------------------------
    # Events
    # --------------------------------------------------
    def term(self, event, data, wave, *args, **kw):
        """Execute in every received event while state = STATE_TERM.
        
        """
        log.debug(f"[{self.uri:20}][{self.state}] -- term 2 ...")
        if not self.pending_responses:
            super().term(event, data, wave, *args, **kw)
    

    def sys_status_changed(self, event, data, wave, *args, **kw):
        return

    def sys_resource_error(self, event, data, wave, *args, **kw):
        return

    def sys_resource_warning(self, event, data, wave, *args, **kw):
        return

    def sys_resource_info(self, event, data, wave, *args, **kw):
        return

    def __sys_pacing(self, event, data, wave, *args, **kw):
        if "algo" in self.uri:
            foo = 1
        return

    # --------------------------------------------------
    # Event Handlers
    # --------------------------------------------------

    def _resolve_callbacks(self):
        # TODO: review ....
        ## compile templates
        # template = {}
        # for key, (
        # rid,
        # body,
        # pattern,
        # extra,
        # callbacks,
        # tracking,
        # ) in self.META_REQUEST.items():
        # callbacks = tuple([getattr(self, cb) for cb in callbacks])
        # template[key] = (rid, body, pattern, extra, callbacks, tracking)
        # self.META_REQUEST = template

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
                handlers = self._handler_error_code.setdefault(code, dict())
                handlers[text] = getattr(self, name)

    def _populate_msg_handlers(self):
        """Populate incoming messages handlers.
        TODO: populte most by instrospection and regexp
        """
        # self.msg_handler[None] = self._nop
        foo = 1

    # --------------------------------------------------
    # High Level I/O
    # --------------------------------------------------

    def request_to(self, port, path, transport=None, **req):
        _port = port.uri if isinstance(port, Resource) else port
        _url0 = parse_uri(_port)
        _url1 = parse_uri(path)

        alias = self.kernel.rev_alias.get(_port)
        if alias:
            _url0["host"] = alias
        else:
            alias = port

        # _url0["query_"] = dict(req)
        _url0.pop("port", None)
        _url0.pop("path", None)
        soft(_url0, **_url1)

        new_url = build_uri(**_url0)

        # debug:
        #if "ticks" in self.uri:
            #if "query" in req:
                #if "tf=1" in req["query"]:
                    ## esta mal!
                    #foo = 1
            #else:
                #foo = 1

        req[REPLY_TO] = [self.uri]
        req[SERVER] = alias
        req[X_EVENT] = EVENT_REQUEST
        req[X_COMMAND] = "request"
        # req['reply-to-request'], req['local_symbol'], req['end']
        return self.request(new_url, **req)

        # print(f"-0-- request_to {self}--------------------------")
        # print(self.waiting.keys())

    def resend(self, port, path, transport=None, **data):
        """Resend the same query when it fails.
        - [ ] mark request as resend, so new attempts will do nothing.
        - [ ] prepare and use request_to()

        """
        res = self.waiting.get(data[REPLY_TO_REQUEST], {})
        if res.get(RESEND_AGAIN, False):
            log.warning(
                f"request is already resend: {res['req']['path']} : {res['req']['query_']}"
            )
        else:
            res[RESEND_AGAIN] = True
            self.request_to(port, path, transport=None, **data)
            log.warning(f"Resending the same request: {port}, {path},  {data['query_']}")

    def _write(self, data):
        """High I/O between Resources."""
        port = data[SERVER]
        event = data[X_EVENT]
        wave = data.get(X_WAVE)
        self.kernel.enqueue(port, event, data, wave)

    def answer(self, res):
        """
        Mark for deletion and not retire inmediately
        This allows to receive 'post-errors' related
        to the same reques before it is theoretical
        finished (e.g. cancel a subscription that is not
        really subscribe, etc).
        """
        # rid = res.get(RID_HEADER)  # we need to compute rid BEFORE calling handler
        # _res = self.waiting.pop(rid, None)

        req = res.get("req", {})
        req[REPLY_FROM] = self.uri
        for port in req.get(REPLY_TO, []):
            self.kernel.enqueue(port, EVENT_RESPONSE, res, req[REPLY_TO_WAVE])

    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def on_request(self, event, data, wave, *args, **kw):
        """Note: is data['reply-to-request'] is present
        that means is a re-send (maybe due PACING VIOLATION)

        """
        log.debug(f"on_request: {data}")
        data[REPLY_TO_REQUEST] = data[RID_HEADER]
        data[REPLY_TO_WAVE] = wave
        res = self._get_generic(**data)
        # print(f"-1-- on_request {self}--------------------------")
        # print(self.waiting.keys())
        foo = 1

    def on_response(self, event, data, wave, *args, **kw):
        log.debug(f"on_response: {data}")

        path = data["req"]["path"]
        req = data["req"]

        # parse message
        # path = self.in_mapping.get(mid, mid)
        retire, dom_patch, default = (
            self.META_RESPONSE.get(path) or self.META_RESPONSE["default"]
        )
        # data.decode()
        dom = data.get("dom")
        if "dom" in data:
            dom = data["dom"]
        else:
            dom = getattr(data, "dom", {})

        soft(dom, **default)
        debug = False
        if debug:
            if mid not in self.DEBUG_IGNORE_MID_IN:
                log.debug("-" * 30)
                log.debug(f"<<< {self.incoming_mid_name[mid]} : # {mid}")
                log.debug("-" * 30)
                for key, value in dom.items():
                    try:
                        value = str(value)
                        log.debug(f"< {key:14} := {value[:30]} ({len(value)}) bytes")

                    except Exception:
                        value = "(unable to convert value to string"
                        log.debug(f"< {key:14} := {value[:30]} ('??') bytes")
                        foo = 1

        rid = req.get(REPLY_TO_REQUEST)  # we need to compute rid BEFORE calling handler
        func = self.msg_handler.get(path)
        if func:
            rid = func(data) or rid

        # TODO: check if must remove the request or not
        res = self.waiting.get(rid)

        # try to complete and update DOM
        if dom_patch:  # TODO: relative path apply
            env = dict(self._uri)
            env.update(req)
            #if res:
                #env.update(res["req"])
            env.pop("path", None)
            soft(
                env,
                time=self.kernel.time,
                date=self.kernel.date,
            )
            # pickle is around 50 times faster than deepcopy
            aux = pickle.loads(pickle.dumps(dom))
            #for _, contract in self.broker.find_contracts(pattern="ESH2").items():
                #foo = 1
            self.dom.patch(path, dom_patch, aux, **env)
            #for _, contract in self.broker.find_contracts(pattern="ESH2").items():
                #foo = 1

        if res:
            # res.feed(data)  # try to complete # TODO: 'data' or 'data.dom'?
            if retire:
                res[DELETE_AT] = self.kernel.time + 100

    def on_child_response(self, event, data, wave, *args, **kw):
        log.debug(f"[{self.uri}] on_child_response: {data} ...")
        foo = 1

    def on_idle(self, event, data, wave=None, *args, **kw):
        super().on_idle(event, data, wave, *args, **kw)
        foo = 1

    def on_timeout(self, event, data, wave=None, *args, **kw):
        super().on_timeout(event, data, wave, *args, **kw)

        req = data.get("req", {})

        # FWD timeout to listeners
        req[REPLY_FROM] = self.uri
        for port in req.get(REPLY_TO, []):
            if port != self.uri:
                self.kernel.enqueue(port, EVENT_TIMEOUT, req, req[REPLY_TO_WAVE])

        # remove from waiting
        rid = req.get("rid")
        self.waiting.pop(rid, None)

    def on_timer(self, event, data, wave=None, *args, **kw):
        log.debug(f"[{self.uri}] on_timer ...")

        foo = 1

    def on_long_timer(self, event, data, wave=None, *args, **kw):
        log.debug(f"[{self.uri}] on_long_timer ...")

        foo = 1

    def on_domestic(self, event, data, wave=None, *args, **kw):
        log.debug(f"[{self.uri}] on_domestic ...")

        # 1. Check for responses mark as 'dead'
        t0 = self.kernel.time
        for rid, res in list(self.waiting.items()):
            delete = res.get(DELETE_AT)
            if delete:
                if delete < t0:
                    # TODO: drop signature cache as well
                    self.waiting.pop(rid)
            elif res.get(TIMEOUT_AT, t0) < t0:
                # check only timeout when res has not been answered
                # (marked with DELETE_AT)
                # self.waiting.pop(rid)
                self.asap(EVENT_TIMEOUT, data=res, wave=wave)

        # 2. Drop any signature that is not longer valid
        for sign, rid in list(self._cache.items()):
            if rid not in self.waiting:
                # print(f"-- remove {rid} signature: {sign} ...")
                self._cache.pop(sign)


class Algo(uServer):
    """An Algorithm."""

    def __init__(self, uri, kernel, *args, **kw):
        super().__init__(uri, kernel, *args, **kw)
        self.result = None
        
        # Idle or Background Tasks
        self._task_pending = {}
        

    # --------------------------------------------------
    # State Change
    # --------------------------------------------------

    def conn_2_sync(self, event, data, wave, *args, **kw):
        super().conn_2_sync(event, data, wave, *args, **kw)

    def sync_2_tran(self, event, data, wave, *args, **kw):
        super().sync_2_tran(event, data, wave, *args, **kw)

    def tran_2_live(self, event, data, wave, *args, **kw):
        super().tran_2_live(event, data, wave, *args, **kw)

    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def on_request(self, event, data, wave, *args, **kw):
        super().on_request(event, data, wave, *args, **kw)
        foo = 1

    def on_response(self, event, data, wave, *args, **kw):
        super().on_response(event, data, wave, *args, **kw)
        foo = 1

    def on_idle(self, event, data, wave=None, *args, **kw):
        super().on_idle(event, data, wave, *args, **kw)
        foo = 1

    def on_timeout(self, event, data, wave=None, *args, **kw):
        super().on_timeout(event, data, wave, *args, **kw)
        foo = 1

    def on_timer(self, event, data, wave=None, *args, **kw):
        super().on_timer(event, data, wave, *args, **kw)
        foo = 1

    def on_long_timer(self, event, data, wave=None, *args, **kw):
        log.debug(f"[{self.uri}] on_long_timer ...")
        super().on_long_timer(event, data, wave, *args, **kw)
        foo = 1

    def on_domestic(self, event, data, wave=None, *args, **kw):
        super().on_domestic(event, data, wave, *args, **kw)
        foo = 1
