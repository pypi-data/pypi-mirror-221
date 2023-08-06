import re

import os
import random
import threading
import traceback
import yaml
import functools
import inspect
import gc
import sys
import hashlib
import pickle
import yaml

from time import time, sleep

from collections import deque
from datetime import datetime


# from .node import *  # TODO: review for deletion

from .request import *
from .kernel import Resource, SAVING_TIMER, SAVING_TIMER_EVENT, EVENT_IDLE, EVENT_SAVE
from .stats import Stats

from uswarm.tools.calls import scall

# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger

log = logger(__name__)

# ------------------------------------------------
# Definitions
# ------------------------------------------------


def try_convert(container, klasses=[int]):
    if not isinstance(klasses, list):
        klasses = [klasses]

    for k, v in list(container.items()):
        for f in klasses:
            try:
                container[k] = f(v)
                break
            except Exception as why:
                continue
    return container


INFINITE = float("inf")
TIMER_MARK = "timer:"
EACH_MARK = "each:"


def is_timer(event):
    return event.startswith(EACH_MARK) or event.startswith(TIMER_MARK)


# --------------------------------------------------
# State Definitions
# --------------------------------------------------
STATE_OFF = "off"
STATE_INIT = "init"
STATE_CONN = "conn"
STATE_SYNC = "sync"
STATE_TRAN = "tran"
STATE_LIVE = "live"
STATE_TERM = "term"
STATE_STOP = "stop"
STATE_ANY = ".*"  # TODO: implement regexp

NO_EVENT = None
EVENT_NEXT = "<next>"  # next step
EVENT_TERM = "<term>"  # term alike
EVENT_QUIT = "<quit>"  # kill alike, but a chance to do something before die
DELAYED_EXECUTION = "<delayed-exec>"

# Merge mode for states and transitions
MERGE_ADD = "add"
MERGE_REPLACE_EXISTING = "replace_existing"
MERGE_REPLACE_ALL = "replace_all"

# State Funcions groups
GROUP_ENTRY = 3
GROUP_DO = 4
GROUP_EXIT = 5


def bind(func_name, context, strict=True):
    func = context.get(func_name)
    if strict and func is None:
        raise RuntimeError(f"Method {func_name} is missing")
    # TODO: assert is calleable
    # func.__binded__ = True  # just a tag for now
    return func


def precompile(exp):
    code = compile(exp, "<input>", mode="eval")
    return code


# --------------------------------------------------
# Layer
# --------------------------------------------------

EVENT_STATE_CHANGE = "<state-change>"

DEFERRED_ORDERED = 0
DEFERRED_ANY = 1


class Layer(Resource):
    def __init__(
        self,
        uri,
        kernel,
        states=None,
        transitions=None,
        context=None,
        protocols=None,
        strict=False,
        *args,
        **kw,
    ):
        """
        - build initial state for start synchronization process.
        """
        super().__init__(uri, kernel, *args, **kw)

        # states and transitions
        self.states = states if states is not None else dict()
        self.transitions = transitions if transitions is not None else dict()

        self.state = STATE_OFF

        self.strict = strict
        # self.protocols = build_xset(
        # protocols, register=True
        # )  # test_set_vs_wset_speed > 5

        self._properties = set()  # for updating properties in context
        self.context = context if context is not None else self._build_context()

        # Setup layer logic
        for name, states, transitions, mode, _ in self._get_layer_setups():
            self._merge(states, transitions, mode)

        self.states, self.transitions = self.compile(
            self.states, self.transitions, self.strict
        )

        ## flying requests
        # self._requests = dict()  # domestic task will clean up timeouts

        # deferred events
        self._deferred_events = deque()
        self.deferred_policy = DEFERRED_ORDERED
        self.allowed_deferred = dict()  # faster than set !
        self.allowed_deferred[EVENT_NEXT] = True
        self.allowed_deferred[EVENT_QUIT] = True
        self.allowed_deferred[EVENT_TERM] = True

        ## 2nd builds parent structure (uri, fingerprint, etc)
        # super().__init__(*args, **kw)

        # try to load state from disk (if applies)
        # self.update_state()
        kernel and kernel._attach(self)

    def __str__(self):
        # uri = parse_uri(self.uri)
        # if uri["path"]:
        ## return f"{uri['fscheme']}::{uri['path'].split('/')[-1]}"
        # return f"{uri['path'].split('/')[-1]}"
        # if uri["host"]:
        # return f"{uri['fscheme']}_{uri['host']}"

        return self.uri

    def __repr__(self):
        return self.__str__()

    def add(self, states=None, transitions=None, mode=MERGE_ADD, strict=None):
        """Add/Modify some logic to the Layer.

        - [x] compile when necessary the preconditions and make the late-binding.
        - [x] merges with current states and transitions.
        - [x] reconfigure event table with loop if is defined.
        """
        strict = strict if strict is not None else self.strict
        states, transitions = self.compile(states, transitions, strict)

        self._merge(states, transitions, mode)

        # if self.loop:
        # self.loop.attach(self)

    def compile(self, states=None, transitions=None, strict=None):
        """Precompile preconditions expressions and function calls as possible.

        - strict = True, forces that all methods must exist
        - strict = False, just ignore missing methods

        - [x] build the execution context for preconditions and methods
        - [x] extend transition info with compile expressions
        - [x] extend transition info with late-binding methods
        - [x] extend with late-binding for state functions

        """
        strict = strict if strict is not None else self.strict

        states = states or dict()
        transitions = transitions or dict()
        # build the execution context for preconditions and methods
        # context = self._build_context()
        # context = self.context

        # add binded transitions functions
        for event, info in transitions.items():
            for source, trans in info.items():
                if len(trans) > 3:
                    continue  # it's already compiled
                for trx in trans:
                    trx.extend([list(), list()])
                    target, precond, func_names, comp_precond, functions = trx

                    # extend transition info with compile expressions
                    for func in precond:
                        comp_precond.append(precompile(func))

                    # extend transition info with late-binding methods
                    for func in func_names:
                        func = self._bind(func, strict)
                        if func:
                            functions.append(func)

        # extend with late-binding for state functions
        for state_functions in states.values():
            if len(state_functions) > 3:
                continue  # it's already compiled
            for func_names in list(state_functions):
                functions = list()
                for func in func_names:
                    func = self._bind(func, strict)
                    if func:
                        functions.append(func)
                state_functions.append(functions)

        return states, transitions

    def _bind(self, func_name, strict=True):
        func = getattr(self, func_name, self.context.get(func_name))
        if strict:
            if func is None:
                raise RuntimeError(
                    f"Method {func_name} is missing and 'strict' mode is {strict}"
                )
            assert inspect.ismethod(func)
        # func.__binded__ = True  # just a tag for now
        return func

    def _merge(self, states, transitions, mode=MERGE_ADD):
        """Merge states and transitions to create hierarchies of layers"""
        # _merge([self.states, states], [self.transitions, transitions], mode=mode)
        states, transitions = [self.states, states], [self.transitions, transitions]

        _states = states.pop(0) if states else dict()
        _transitions = transitions.pop(0) if transitions else dict()

        if mode in (MERGE_ADD,):
            pass
        elif mode in (MERGE_REPLACE_EXISTING,):
            for st in states:
                for state, new_functions in st.items():
                    _states.pop(state, None)

            for tr in transitions:
                for source, new_info in tr.items():
                    info = _transitions.setdefault(source, dict())
                    for event, new_trx in new_info.items():
                        trx = info.setdefault(event, list())
                        for new_t in new_trx:
                            for i, t in reversed(list(enumerate(trx))):
                                if t[:1] == new_t[:1]:
                                    trx.pop(i)

        elif mode in (MERGE_REPLACE_ALL,):
            states.clear()
            for tr in transitions:
                for source, new_info in tr.items():
                    _transitions.pop(source, None)
        else:
            raise RuntimeError(f"Unknown '{mode}' MERGE MODE")

        # merge states
        for st in states:
            for state, new_functions in st.items():
                functions = _states.setdefault(state, list([[], [], []]))
                for i, func in enumerate(new_functions):
                    for f in func:
                        if f not in functions[i]:
                            functions[i].append(f)

        # merge transitions
        def _expand(expression):
            try:
                exp = f"f'{expression}'"
                return eval(exp, self.context)
            except Exception as why:
                return expression

        def _merge_trx_old(source, new_info):
            info = _transitions.setdefault(source, dict())
            for event, new_trx in new_info.items():
                trx = info.setdefault(event, list())
                for new_t in new_trx:
                    for t in trx:
                        if t[:2] == new_t[:2]:
                            t[-1].extend(new_t[-1])
                            break
                    else:
                        trx.append(new_t)

        def _merge_trx(event, new_info):
            info = _transitions.setdefault(event, dict())
            for state, new_trx in new_info.items():
                trx = info.setdefault(state, list())
                for new_t in new_trx:
                    for t in trx:
                        if t[:2] == new_t[:2]:
                            t[-1].extend(new_t[-1])
                            break
                    else:
                        trx.append(new_t)

        def match_states(regexp):
            try:
                regexp = re.compile(source, re.DOTALL)
            except Exception:
                return regexp

            for state in _states:
                try:
                    m = regexp.match(state)
                    if not m:
                        continue
                    d = try_convert(m.groupdict())
                    self.context.update(d)
                    yield state
                except Exception:
                    pass

        for tr in transitions:
            for event, new_info in tr.items():
                event = _expand(event)
                info = pickle.loads(pickle.dumps(new_info))  # fast deep copy
                for source, trxs in info.items():
                    for source in match_states(source):
                        for trx in trxs:
                            # expand target state
                            trx[0] = _expand(trx[0])
                            # expand just conditions and functions, preseving original container
                            for i in range(1, 3):
                                for j, item in list(enumerate(trx[i])):
                                    trx[i][j] = _expand(trx[i][j])
                _merge_trx(event, info)

        # org -------------------------
        # for tr in transitions:
        # for source, new_info in tr.items():
        ## regular expression case -----------------------
        # try:
        # regexp = re.compile(source, re.DOTALL)
        # if regexp.groups > 0:  # is an regular expression?
        # for state in _states:
        # try:
        # m = regexp.match(state)
        # if not m:
        # continue
        # d = try_convert(m.groupdict())
        # self.context.update(d)
        ## just try to expand transision
        # info = copy.deepcopy(new_info)
        # for event, trxs in info.items():
        ## expand event
        # event = _expand(event)
        # for trx in trxs:
        ## expand target state
        # trx[0] = _expand(trx[0])
        ## expand just conditions and functions, preseving original container
        # for i in range(1, 3):
        # for j, item in list(enumerate(trx[i])):
        # trx[i][j] = _expand(trx[i][j])
        # _merge_trx(state, info)
        # except Exception as why:
        # _merge_trx(state, info)
        # continue
        # else:
        ## regular case, string is not a regular exp
        # _merge_trx(source, new_info)

        # except Exception as why:
        ## source is not a string, could be?
        # _merge_trx(source, new_info)

        return _states, _transitions

    def _get_layer_setups(self, include=None, skip=None):
        """Get Layer states and transitions by self instrospection from:

        - [x] _setup_xxxxx() methods (applied by sorted function names)
        - [x] @expose() decorator

        """
        include = include or []
        skip = skip or []

        match = re.compile("_setup_(?P<name>.*)").match
        names = [name for name in dir(self) if match(name)]
        names.sort()
        for name in names:
            logic = match(name).groupdict()["name"]

            if logic in skip:
                continue
            if include and logic not in include:
                continue

            func = getattr(self, name)
            states, transitions, mode = scall(func, **self.context)
            yield logic, states, transitions, mode, func.__doc__

        # provide @expose functions as self-transision
        states, transitions = self._build_self_transitions()
        yield "autogenerated_self_transitions", states, transitions, MERGE_ADD, ""

    def _build_context(self):
        """Create a default context when no other is provided"""
        result = dict()
        for k in dir(self):
            if k[0] == "_":
                continue

            item = getattr(type(self), k, None)
            if isinstance(item, property):
                self._properties.add(k)

            try:
                item = getattr(self, k)
                if inspect.ismethod(item):
                    continue
                result[k] = item
            except Exception as why:
                foo = 1
        return result

    def _build_self_transitions(
        self, source=STATE_LIVE, target=STATE_LIVE, precond=None, pattern=r".*"
    ):
        """Create (states, transitions) info based on decorator
        @expose(**context)

        context can contains:

        - source:    transition source
        - target:    transition target
        - precond:   transition preconditions

        You don't need to change the following values (are set by default):

        - key:       the event key to be published with
        - func_name: the function name that will be try to late-binding

        You can also use regexp pattern if method names follows a name pattern

        form where to extracto context info, instead declaring
        as decoraor parameters
        """
        regexp = re.compile(pattern, re.DOTALL)
        self_states = dict()
        self_transitions = dict()
        precond = precond or list()
        for func_name in dir(self):
            m = regexp.match(func_name)
            if not m:
                continue
            func = getattr(self, func_name)
            ctx = getattr(func, "__context__", dict())
            if ctx:
                d = m.groupdict()
                src = d.get("source", ctx.get("source")) or source
                tar = d.get("target", ctx.get("target")) or target

                self_states.setdefault(src, [[], [], []])
                trx = self_transitions.setdefault(src, dict())

                func_name = d.get("func_name", ctx["func_name"])  # must exist
                pre = ctx.get("precond") or precond

                keys = build_set(d.get("keys", ctx["keys"]))
                keys.add(func_name)
                for key in keys:
                    trx[key] = [[tar, pre, [func_name]]]

        return self_states, self_transitions

    # -----------------------------------------------
    # Layer definitions
    # -----------------------------------------------
    def _setup_010_term(self):
        """Set TERM and QUIT logic for the base layer."""
        states = {
            STATE_OFF: [[], [], []],
            STATE_INIT: [[], [], []],
            STATE_CONN: [[], [], []],
            STATE_SYNC: [[], [], []],
            STATE_TRAN: [[], [], []],
            STATE_LIVE: [[], [], []],
            STATE_TERM: [["term"], [], []],
            STATE_STOP: [["bye"], [], []],
        }

        transitions = {
            EVENT_NEXT: {
                STATE_OFF: [
                    [STATE_INIT, [], ["off_2_init"]],
                ],
                STATE_INIT: [
                    [STATE_CONN, [], ["init_2_conn"]],
                ],
                STATE_CONN: [
                    [STATE_SYNC, [], ["conn_2_sync"]],
                ],
                STATE_SYNC: [
                    [STATE_TRAN, [], ["sync_2_tran"]],
                ],
                STATE_TRAN: [
                    [STATE_LIVE, [], ["tran_2_live"]],
                ],
            },
            # signals TERM and QUIT
            EVENT_TERM: {
                STATE_LIVE: [
                    [STATE_TERM, [], ["on_term"]],
                ],
            },
            EVENT_QUIT: {
                STATE_LIVE: [
                    [STATE_STOP, [], ["on_term", "on_quit"]],
                ],
                STATE_TERM: [
                    [STATE_STOP, [], ["on_quit"]],
                ],
            },
        }

        return states, transitions, MERGE_ADD

    # -----------------------------------------------
    # Layer methods
    # -----------------------------------------------

    def off_2_init(self, event, data, wave, *args, **kw):
        log.debug(f"[{self.uri:20}][{self.state}] -- off_2_init ...")
        self.asap(EVENT_NEXT)

    def init_2_conn(self, event, data, wave, *args, **kw):
        log.debug(f"[{self.uri:20}][{self.state}] -- init_2_conn ...")
        self.asap(EVENT_NEXT)

    @property
    def resources_loaded(self):
        return True

    def conn_2_sync(self, event, data, wave, *args, **kw):
        log.debug(f"[{self.uri:20}][{self.state}] -- conn_2_sync ...")
        self.asap(EVENT_NEXT)

    def sync_2_tran(self, event, data, wave, *args, **kw):
        log.debug(f"[{self.uri:20}][{self.state}] -- sync_2_tran ...")
        self.asap(EVENT_NEXT)

    def tran_2_live(self, event, data, wave, *args, **kw):
        log.debug(f"[{self.uri:20}][{self.state}] -- tran_2_live ...")
        # self.asap(EVENT_NEXT)

    # -----------------------------------------------
    # Exiting methods
    # -----------------------------------------------
    def term(self, event, data, wave, *args, **kw):
        """Prepare shutdown process

        Should fire any tear-down tasks and auto-send an EVENT_QUIT
        event when everything is ready to quit.
        """
        log.debug(f"[{self.uri:20}][{self.state}] -- term 1 ...")
        self.asap(EVENT_QUIT)

    def on_term(self, event, data, wave, *args, **kw):
        """Execute on the transition from LIVE to TERM due EVENT_TERM request.

        Should fire any tear-down tasks because a EVENT_QUIT event may happens
        really soon to kill Layer.
        """
        log.debug(f"[{self.uri:20}][{self.state}] -- on_term 1 ...")

    def on_quit(self, event, data, wave, *args, **kw):
        """Execute on the transition from TERM to QUIT due EVENT_QUIT request.
        Discard any chance to shutdown nicely and performs any action needed
        to free any resources.
        """
        log.debug(f"[{self.uri:20}][{self.state}] -- quit 1 ...")

    def bye(self, event, data, wave, *args, **kw):
        """Executed when state == STOP as the last task to do
        before dying and retire from kernel.
        """
        log.debug(f"[{self.uri:20}][{self.state}] -- bye 1 ...")
        if self.kernel:
            self.kernel.delete(self.uri)

    # -----------------------------------------------
    # Event Dispatch methods
    # -----------------------------------------------
    def enqueue(self, port, event, data=None, wave=None):
        """Override for complex parappel implementation"""
        log.debug(
            f"[{self.uri:20}][{self.state}] ##>>>> enqueue: {port}, {event}, {data} ..."
        )
        self.kernel.enqueue(port, event, data, wave)

    def oob(self, event, data=None, wave=None):
        """Insert an event to be proceses Out-of-Bound
        (just inmediately) before any other."""
        log.warning(
            f"[{self.uri:20}][{self.state}] ##>>>> oob: {self.uri}, {event}, {data} ..."
        )
        self.kernel.oob(self.uri, event, data, wave)

    def asap(self, event, data=None, wave=None):
        """Override for complex parappel implementation"""
        if event in (EVENT_NEXT,):
            if self.state in (STATE_LIVE,):
                assert False

        log.debug(
            f"[{self.uri:20}][{self.state}] ##>>>> asap: {self.uri}, {event}, {data} ..."
        )
        self.kernel.enqueue(self.uri, event, data, wave)

    def at(self, when, event, data, wave=None):
        self.kernel.at(when, self.uri, event, data, wave)


class STM(
    Layer,
):
    # TODO: save and STM ?
    # TODO: checkself.event_handler[EVENT_SAVE]
    def __init__(self, *args, **kw):
        Layer.__init__(self, *args, **kw)
        # iRequester.__init__(self)

        self.allowed_deferred[EVENT_STATE_CHANGE] = True

        self.asap(EVENT_NEXT)  # needed to start evolution

    def dispatch(self, event, data, wave=None):
        log.debug(
            f"[{self.uri:20}][{self.state}] >> event: {event}, data: {data}, wave: {wave}"
        )

        # if len(self._deferred_events) > 6:
        # foo = 1

        transitions = self.transitions.get(event)
        if not transitions:
            # STM does not handle this event
            log.debug(f"[{self.uri:20}] does not handle event: {event}")
            return

        transitions = transitions.get(self.state)
        if not transitions:
            if event in self.allowed_deferred:
                log.debug(
                    f"[{self.uri:20}][{self.state}] -1- event: {event} send to defered"
                )
                self._deferred_events.append((event, data, wave))
            return

        # ctx = self.context

        for (
            new_state,
            preconds,
            func_names,
            comp_preconds,
            func_methods,
        ) in transitions:
            new_state = new_state or self.state  # None means state will no change
            # TODO: build a single python eval code for all preconditions
            valid = True
            if preconds:
                # Check preconditions
                # layer._update_context_properties()
                for k in self._properties:
                    self.context[k] = getattr(self, k)

                for pre in comp_preconds:
                    # use globals = {} to avoid python
                    # push '__builtins__' into context
                    if not eval(pre, {}, ctx):
                        valid = False
                        break

            if valid:
                # 2. Execute Transition ---------------
                # execute EXIT state functions (old state)
                for func in self.states[self.state][GROUP_EXIT]:
                    log.debug(f"[{self.uri:20}][{self.state}] -- (exit) -- {func}")
                    func(event, data, wave)

                # execute transition functions
                for func in func_methods:
                    log.debug(f"[{self.uri:20}][{self.state}] -- (link) -- {func}")
                    func(event, data, wave, new_state=new_state)

                # new_state == None means no state change
                if self.state != new_state:
                    self._pub_state_changed(new_state)
                self.state = new_state

                # execute ENTRY state functions (new state)
                for func in self.states[new_state][GROUP_ENTRY]:
                    log.debug(f"[{self.uri:20}][{self.state}] -- (enter) -- {func}")
                    func(event, data, wave)

                # 3. Execute Transition ---------------
                # include DO state functions (new state) as domestic tasks
                # to be processed if Layer stays for time enough
                # self.watchdog.watch(layer)

                ## 4. Try to dispatch just one deferred Event for this layer ---------------
                # Note: preserve order vs dispatch any available event
                if self._deferred_events:
                    if self.deferred_policy == DEFERRED_ORDERED:
                        event = self._deferred_events[0][0]
                        if self.transitions.get(event, {}).get(new_state):
                            self.oob(*self._deferred_events.popleft())
                    else:
                        for i, deferred in enumerate(list(self._deferred_events)):
                            event = deferred[0]
                            if self.transitions.get(event, {}).get(new_state):
                                self.oob(*deferred)
                                self._deferred_events.pop(i)
                                break

                # possible_events = layer._deferred_events \
                # .intersection(
                # layer.transitions[new_state])

                # if possible_events:
                # d_event = possible_events.pop()  # take just one
                # d_data_queue = layer._deferred_data[d_event]
                # d_data = d_data_queue.pop(0)
                # if not d_data_queue:
                # layer._deferred_events.remove(d_event)

                ## recursively dispatch all events so far
                # self.dispatch(key=d_event, data=d_data, scope=set([layer]))

                ## assume there's only 1 transition possible each time
                ## TODO: use a debugger (slower) Loop class
                ## TODO: that check this issues in real time
                break

        else:
            # no event has matched now
            if event in self.allowed_deferred:
                log.warning(
                    f"[{self.uri:20}][{self.state}] -2- event: {event} send to defered"
                )
                self._deferred_events.append((event, data, wave))

    def _pub_state_changed(self, new_state):
        if new_state in (STATE_LIVE,):
            foo = 1
        log.debug(
            f"[{self.uri:20}][{self.state}] --->> {new_state} :  _pub_state_changed -- .."
        )
        for parent in self.parents:
            if isinstance(parent, STM):
                parent.asap(EVENT_STATE_CHANGE, (self, self.state, new_state))

    # -----------------------------------------------
    # Layer definitions
    # -----------------------------------------------
    def _setup_012_status_notification(self):
        """Set TERM and QUIT logic for the base layer."""
        states = {}

        transitions = {
            EVENT_STATE_CHANGE: {
                STATE_LIVE: [
                    [STATE_LIVE, [], ["on_state_change"]],
                ],
            }
        }

        return states, transitions, MERGE_ADD

    def _setup_013_special_events(self):
        """Set TERM and QUIT logic for the base layer."""
        states = {}

        transitions = {
            EVENT_IDLE: {
                STATE_LIVE: [
                    [STATE_LIVE, [], ["on_idle"]],
                ],
            },
            EVENT_TIMEOUT: {
                STATE_LIVE: [
                    [STATE_LIVE, [], ["on_timeout"]],
                ],
            },
        }

        return states, transitions, MERGE_ADD

    def _setup_026_term_nicely(self):
        """Control which events must be attended in STATE_TERM state."""
        states = {}

        transitions = {
            EVENT_STATE_CHANGE: {
                STATE_TERM: [
                    [STATE_TERM, [], ["on_state_change"]],
                ],
            },
            EVENT_TIMEOUT: {
                STATE_TERM: [
                    [STATE_TERM, [], ["on_timeout"]],
                ],
            },
        }

        return states, transitions, MERGE_ADD

    # -----------------------------------------------
    # Layer methods
    # -----------------------------------------------
    def on_state_change(self, event, data, wave, *args, **kw):
        child, old_state, new_state = data
        log.debug(
            f"[{self.uri:20}][{self.state}] : [{child.uri}] : {old_state} --->  {new_state} :  on_state_change ..."
        )


class PSTM(STM):
    "Persistent STM"

    def __init__(self, uri, kernel, *args, **kw):
        super().__init__(uri, kernel, *args, **kw)

        self.allowed_deferred[SAVING_TIMER_EVENT] = True
        # self.subscribe(SAVING_TIMER)

    def _setup_205_saving(self):
        """Set TERM and QUIT logic for the base layer."""
        states = {}

        transitions = {
            EVENT_SAVE: {
                # STATE_OFF: [
                # [STATE_INIT, [], []],
                # ],
                # STATE_INIT: [
                # [STATE_CONN, [], []],
                # ],
                # STATE_CONN: [
                # [STATE_SYNC, [], []],
                # ],
                STATE_LIVE: [
                    [STATE_LIVE, [], ["save_state"]],
                ],
                # STATE_TRAN: [
                # [STATE_LIVE, [], []],
                # ],
            },
        }

        return states, transitions, MERGE_ADD

    # -----------------------------------------------
    # Layer methods
    # -----------------------------------------------
    def off_2_init(self, event, data, wave, *args, **kw):
        log.debug(
            f"[{self.uri:20}][{self.state}] -- off_2_init: trying to load from {self.storage_path}"
        )
        self.load()
        super().off_2_init(event, data, wave, *args, **kw)


if __name__ == "__main__":
    # no merece la pena usar decoradores para intentar pasarle
    # un contexto a la funcion de ejecucion.
    # mejor hacerlo en cada llamada. no nos vamos a ahorrar tiempo.
    ctx = dict(b=1)

    def handler(func):
        def wrapper(*args, **kw):
            # code = func.__code__
            # for missing in code.co_varnames[len(args):code.co_argcount]:
            # kw[missing] = ctx[missing]
            return func(*args, **kw)

        return wrapper

    @handler
    def func00(a, b):
        c = a + b
        return c

    z = func00(1, 2)

    foo = 1
# End
