
from uswarm.tools import (
    parse_uri,
    soft,
)

from uswarm.tools.logs import logger
log = logger(__name__)

# ------------------------------------------------
# Base Protocol Node / States
# ------------------------------------------------
STATE_OFF = "off"
STATE_INIT = "init"
STATE_SYNC = "sync"
STATE_TRANSITION = "transition"
STATE_LIVE = "live"
STATE_TERM = "term"

NEXT_STATE = {
    STATE_OFF: STATE_INIT,
    STATE_INIT: STATE_SYNC,
    STATE_SYNC: STATE_TRANSITION,
    STATE_TRANSITION: STATE_LIVE,
    STATE_LIVE: STATE_TERM,
}



class Node:


    def __init__(self, uri, kernel, dom=None, *args, **kw):
        """
        - build initial state for start synchronization process.
        """
        self.uri = uri
        self._uri = parse_uri(uri)
        assert any(self._uri.values()), f"Bad URI '{uri}'"
        soft(self._uri, **kw)

        self.kernel = kernel
        self.state = STATE_OFF

        if kernel:
            dom = dom or kernel.dom
            kernel.register_queue(self)
            
        self.dom = dom
            
        self.next_state()

    def __repr__(self):
        return f"<{self.uri}>"

    def connection_made(self, *args):
        """Called when a connection is made."""

    def connection_lost(self, *args):
        """Called when the connection is lost or closed."""

    # STM states alike
    def next_state(self):
        self.change_state(NEXT_STATE[self.state])

    def change_state(self, state):
        func = getattr(self, f"_exit_{self.state}", None)
        func and func()

        self.state = state

        func = getattr(self, f"_enter_{self.state}", None)
        func and func()

    def _enter_init(self):
        self.next_state()

    def _enter_sync(self):
        self.next_state()

    def _enter_transition(self):
        self.next_state()

    def _enter_live(self):
        log.debug(f"On LIVE: {self} ")
        foo = 1

    def _enter_term(self):
        foo = 1


# ------------------------------------------------
# Pub / Sub
# ------------------------------------------------
ALL_GROUPS = "*"


class Publisher(Node):
    """REVIEW: ..."""

    def __init__(self, uri, kernel, *args, **kw):
        super().__init__(uri, kernel, *args, **kw)

    def data_received(self, provider, name, item, wave, *route):
        """a new data is received from provider.
        check if we can fire handle to make a step.

        Default implementation just forwards all data received.
        """
        deferred = super().data_received(provider, name, item, wave, *route)
        if not deferred:
            # check if all in-data has been received
            assert (
                name not in self.in_args
            ), f"overwriting incoming arg '{name}' before have been processed."

            self.in_args[name] = item
            if set(self.inputs.keys()).issubset(self.in_args):
                # all inputs are completed
                result = self.compute()
                # TODO: implement filter for FWD
                fqscheme = self._fwd_group(result)
                self.forward(fqscheme, wave, result, *route)
                self.clean_inputs()
        return deferred

    def compute(self):
        """Compute the condensation of received data.

        - modify internal state (wip outcome)
        - flush outcome result when is completed.

        FWD everithing
        """
        return self.in_args

    def _fwd_group(self, result):
        """Compute FWD groups.
        ALL by default.
        """
        return ALL_GROUPS

    def forward(self, fqscheme, wave, item, *route):
        """Push processed data into output provider.

        - send data to out provider.
        - start a fresh new inputs for compute the next outcome.
        """
        for regexp, holder in self.flows.items():
            if fqscheme == ALL_GROUPS or regexp.match(fqscheme):
                for actor, name in holder.values():
                    actor.data_received(self, name, item, wave, *route)

    def replay(self, target, wzero):
        """Resend all known waves from wzero to current wave."""
        # TODO: a 2nd connection is necessary?
        raise NotImplementedError()


class Subscripter(Node):
    def subscribe(self, uri, name=None):
        kernel = self.kernel
        source = kernel.allocate(uri)
        kernel.link(source, self, name)


