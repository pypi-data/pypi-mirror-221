import re
import operator

from collections import deque
from time import time

from uswarm.tools import hash_point, get_blueprint
from uswarm.tools.containers import find_best

from .kernel import EVENT_RESOURCE_PACING
from .userver import uServer, STATE_LIVE, MERGE_ADD, REPLY_TO_REQUEST, SYS_GENERAL_BUS
from .pacing import Pacing
from .request import DEFAULT_TIMEOUT, REQ_TIMEOUT

# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger, log_container

log = logger(__name__)
log_pacing = logger("uswarm.kernel.pacing")

# --------------------------------------------------
# Pools
# --------------------------------------------------
POLICY_ALL = "all"
POLICY_ROUND_ROBIN = "round-robin"
POLICY_ROUND_ROBIN_PACING = "round-robin-pacing"
POLICY_DEFAULT = POLICY_ALL

# TODO: move to uswarm global definitions and remove from atlas project
CONFIG_FSCHEME_DEFAULTS = "fscheme_defaults"
CONFIG_POOL_PREASIGNED_TARGETS = "preasigned_targets"
CONFIG_POOL_CLEAN_TARGETS_EVERY = "clean_targets_every"


class Pool(uServer):
    KERNEL_URI_REGISTERING = "(pool)://"
    MIN_PACING_DELAY = 1
    MIN_DELAY = 1

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.debug = False

        self.n = 10
        self.window = 500
        self.throttle = 2

        # recalc on subclass
        self.max_speed = self.n / self.window
        self.delta = 1.10 / self.max_speed  # +1: extra delay

        self.f0 = 0.20  # when start using last request time instead 'now'
        self.f2 = 0.45  # when start using 'now' + delta or last request time + delta
        self.f3 = 0.60  # when start to smooth request frequency to reach window period under max average speed.

        # pacing
        self.pacing = {}
        self.regexp = []

        # targets observed
        self.observed = {}

        # policy
        self.default_policy = "all"
        self.path_policies = {
            # "/contracts": (POLICY_ROUND_ROBIN, False),
            # "/fills": (POLICY_ALL, False),
            # "/historical/(bars|ticks)": (POLICY_ROUND_ROBIN_PACING, True),
        }
        self.policies = {
            # POLICY_ROUND_ROBIN_PACING: self._policy_round_robin,
            # POLICY_ROUND_ROBIN: self._policy_round_robin,
            # POLICY_ALL: self._policy_all,
        }

        self._round_robin_candidates = deque()

        # pacing regexps
        # self.regexp.append("tws://.*(10000|10001|10002|10004|10092)")

        # self.event_handler[EVENT_STATUS_CHANGED] = self.sys_status_changed

    # -----------------------------------------------
    # Layer definitions
    # -----------------------------------------------

    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def sys_status_changed(self, event, data, wave, *args, **kw):
        log.debug(f"sys_status_changed: {event} : data: {data}")
        uri = data["port"]
        status = data["status"]

        for reg in self.regexp:
            m = re.match(reg, uri)
            if m:
                if status in ("new",):
                    resource = self.kernel.find_resource(uri)
                    if resource:
                        self.observed[uri] = resource
                        # self.pacing[uri] = Pacing(self.n, self.window, uri=uri)
                        self.pacing[uri] = deque()
                        break
                elif status in ("delete",):
                    self.observed.pop(uri, None)
                    self.pacing.pop(uri, None)

    def sys_pacing(self, event, data, wave, *args, **kw):
        """
        'path': '/historical/bars'
        'query': 'local_symbol=ESH2&end=2022-02-06T07:26:18.683098+00:00',

        'reply-to-request': 102, (mine)
        'rid': 2004, (tws)
        'account': 'U7111446',

        'bar_size': '1 secs',
        'duration': '2000 S',
        'rth': '0',
        'what': 'TRADES',

        'reply-from': 'tws://gw-agp:10000?client_id=666'

        """
        log.debug(f"sys_pacing: {event} : data: {data}")

        uri = data["reply-from"]
        pacing = self.pacing.get(uri)
        if pacing:
            # pacing.slow()
            log.warning(f"Slowing down: {uri}: {data.get('local_symbol')}")
            self._slow(pacing)
        else:
            log.error(f"Pacing instance: {uri} not found!")

    def _slow(self, pacing):
        l = len(pacing)
        free = int(self.n / 2 - l)

        t0 = pacing[-1] if pacing else self.kernel.time
        t0 = max(t0, self.kernel.time)
        self.speed = 0.99 * self.n / self.window
        # self.delta = 1 / self.max_speed + 1
        self.throttle = 0.20

        # while len(pacing) <= self.f0 * self.n:
        # t0 += 0.1  # self.MIN_PACING_DELAY
        # pacing.append(t0)
        # t0 += 1 * self.MIN_PACING_DELAY
        # pacing.append(t0)

    def _when(self, pacing):
        # clean already sent time-marks
        t0 = self.kernel.time - self.window
        while pacing:
            if pacing[0] < t0:
                pacing.popleft()
            else:
                break

        # recalc delta
        samples = len(pacing)
        self.delta = 1.01 * self.window / self.n

        # Hack for fast debugging

        if samples <= self.f0 * self.n:
            t0 = self.kernel.time  # just now
        else:
            # compute smooth ?
            if samples >= self.f3 * self.n:
                elapsed = pacing[-1] - pacing[0]
                # speed = samples / elapsed
                # calculate a new delta that will brings the same average speed
                x = (samples + 1) * self.delta - elapsed
                x = max(self.MIN_DELAY, x)
                self.delta = min(x, 4 * self.delta / self.f3)
                self.throttle = 1.0

            # from now or from last request
            if samples > self.f2 * self.n:
                t0 = pacing[-1]
            else:
                t0 = self.kernel.time
            t0 += self.delta / self.throttle

        self.throttle += (1 - self.throttle) * 0.05

        pacing.append(t0)

        delays = [pacing[i] - pacing[i - 1] for i in range(1, samples)]
        delays = [f"{x:0.2f}" for x in delays]
        log_pacing.debug(f"[{self.uri}] {delays}")
        log_pacing.debug(f"[{self.uri}] lapse: {self.delta}, window: {self.window}")
        now = self.kernel.time

        log_container(log_pacing, [x - now for x in pacing])

        return t0

    def on_request(self, event, data, wave, *args, **kw):
        """Select single or multiples targets to attend the requests."""
        # log.debug(f"on_request: {data}")
        policy, pacing = self._guess_policy(data)
        for uri in self.policies[policy](data):
            resource = self.observed.get(uri)
            if resource:
                if pacing:
                    pacing = self.pacing[uri]
                    when = self._when(pacing)
                    resource.at(when, event, data, wave)
                    # set timeout
                    data[REQ_TIMEOUT] = data.setdefault(
                        REQ_TIMEOUT, DEFAULT_TIMEOUT
                    ) + max(0, when - self.kernel.time)

                else:
                    resource.asap(event, data, wave)

            else:
                log.warning(f"{self} There is not resources to forward: {data}")
                # TODO: add to deferred?

        else:
            foo = 1

        foo = 1

    def _guess_policy(self, data):
        for regexp, policy in self.path_policies.items():
            if re.match(regexp, data["path"]):
                return policy
        return POLICY_DEFAULT, False

    def _policy_all(self, data):
        return list(self.observed)

    def _policy_round_robin(self, data):
        if not self._round_robin_candidates:
            # TODO: suffle ?
            self._round_robin_candidates.extend(self.observed)

        # random.sample(list(self.observed), 1)
        while self._round_robin_candidates:
            uri = self._round_robin_candidates.popleft()
            yield uri
            break

    def on_response(self, event, data, wave, *args, **kw):
        # super().on_response(event, data, wave, *args, **kw)
        return

        log.debug(f"on_response: {data}")

        path = data["req"]["path"]
        req = data["req"]
        # meta = data['meta']

        # if mid not in self.DEBUG_IGNORE_MID_IN:
        # foo = 1

        # if mid in (14,):
        ## print (f">> received mid: {mid}")
        # foo = 1  # news bulleting

        # parse message
        # path = self.in_mapping.get(mid, mid)
        retire, dom_patch, dec = (
            self.META_RESPONSE.get(path) or self.META_RESPONSE["default"]
        )
        dom = data.dom
        # data.decode()
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

        # try to find any waiting response
        # related to the just incoming message

        # getting the last rid sent as fallback value
        # rid = data.get_rid() # or self._next_rid

        # and feed the waiting response (if any)
        # TODO: check if must remove the request or not
        res = self.waiting.get(rid)

        # try to complete and update DOM
        if dom_patch is not None:  # TODO: relative path apply
            env = dict(self._uri)
            if res:
                env.update(res["req"])
            env.pop("path", None)
            soft(
                env,
                time=self.kernel.time,
                date=self.kernel.date,
            )
            # pickle is around 50 times faster than deepcopy
            aux = pickle.loads(pickle.dumps(data.dom))
            self.dom.patch(path, dom_patch, aux, **env)
            # self.dom.save()

        if res:
            # res.feed(data)  # try to complete # TODO: 'data' or 'data.dom'?

            if retire:
                # Mark for deletion and not retire inmediately
                # This allows to receive 'post-errors' related
                # to the same reques before it is theoretical
                # finished (e.g. cancel a subscription that is not
                # really subscribe, etc)
                self.waiting.pop(rid)

    def on_idle(self, event, data, wave=None, *args, **kw):
        super().on_idle(event, data, wave, *args, **kw)
        # clean *stall* queues from time to time.
        t0 = self.kernel.time - self.window
        for uri, pacing in self.pacing.items():
            while pacing:
                if pacing[0] < t0:
                    pacing.popleft()
                else:
                    break
        foo = 1

    def on_timer(self, event, data, wave=None, *args, **kw):
        super().on_timer(event, data, wave, *args, **kw)

        foo = 1

    def on_long_timer(self, event, data, wave=None, *args, **kw):
        super().on_long_timer(event, data, wave, *args, **kw)

        foo = 1

    def on_domestic(self, event, data, wave=None, *args, **kw):
        super().on_domestic(event, data, wave, *args, **kw)


class PreassignedPool(Pool):
    BLUEPRINT_KEYS = set(
        [
            "_url_",
            "reply-to",
        ]
    )
    MIN_REASIGN_LAPSE = 60

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self._preassigned = dict()
        self._last_reasignation = 0

    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def sys_status_changed(self, event, data, wave, *args, **kw):
        super().sys_status_changed(event, data, wave, *args, **kw)

        uri = data["port"]
        status = data["status"]

        if status in ("delete",):
            for sign, uri2 in list(self._preassigned.items()):
                if uri2 == uri:
                    self._preassigned.pop(sign)

    def _policy_round_robin(self, data):
        """Try to send the same query type to the same server, so TWS can not trace
        a swarm collaborating to retrieve data."""
        # BLUEPRINT_SKIP_KEYS = set(["rid", "end", "date"])
        # blue = {k: data[k] for k in set(data).difference(BLUEPRINT_SKIP_KEYS)}

        # blue = {k: data[k] for k in self.BLUEPRINT_KEYS.intersection(data)}
        # sign = hash_point(blue)
        defaults = self.kernel.config.get(CONFIG_FSCHEME_DEFAULTS, {}).get(
            self._uri["fscheme"], {}
        )

        clean_preasigned = defaults.get(CONFIG_POOL_CLEAN_TARGETS_EVERY, 0)
        if clean_preasigned > 0:
            if self.kernel.time - self._last_reasignation > clean_preasigned:
                self._preassigned.clear()
                self._last_reasignation = self.kernel.time

        if defaults.get(CONFIG_POOL_PREASIGNED_TARGETS):
            sign = get_blueprint(data, self.BLUEPRINT_KEYS)
            uri = self._preassigned.get(sign)
        else:
            uri = sign = None

        if uri not in self.observed:
            for uri in super()._policy_round_robin(data):
                self._preassigned[sign] = uri
                #log.warning(f"Assignate: {uri} for {data}")
                break

        self._preassigned[sign] = uri
        if "end" in data:
            log.debug(f"Fwd: {data['end']}: {uri} : {data.get('query_')}")
        else:
            log.debug(f"FWD: {uri} : {data.get('_url_')}")

        yield uri

    def on_idle(self, event, data, wave=None, *args, **kw):
        """
        Try to reassign queues when a worker has much less load than average.

        """
        super().on_idle(event, data, wave, *args, **kw)

        if self.kernel.time - self._last_reasignation < self.MIN_REASIGN_LAPSE:
            return

        if True:
            return

        family = self.get_family()
        loads = {uri: len(x) for uri, x in self.pacing.items()}
        if loads:
            avg_load = sum(loads.values()) / len(loads)
            min_uri, min_load = find_best(loads, operator.lt)
            max_uri, max_load = find_best(loads, operator.gt)

            delta_h = max_load - avg_load
            delta_l = avg_load - min_load
            if delta_h > 0 and delta_l / delta_h > 1.5:
                # try to reassign one queue at time
                for sign, uri in list(self._preassigned.items()):
                    if uri == max_uri:
                        self._preassigned[sign] = min_uri
                        self._last_reasignation = self.kernel.time
                        break

        foo = 1
