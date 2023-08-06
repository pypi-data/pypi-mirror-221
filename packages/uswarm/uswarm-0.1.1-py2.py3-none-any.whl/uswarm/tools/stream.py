# tick types taken from IB
LINK_STATUS = -1
BID_SIZE = 0
BID_PRICE = 1
ASK_PRICE = 2
ASK_SIZE = 3
VOLUME = 8
CLOSE = 9
TIME = 45

# see ibapi.ticktype.py
tick_types = {
    LINK_STATUS: "Link-Status",
    #  https://interactivebrokers.github.io/tws-api/tick_types.html
    BID_SIZE: "Bid-Size",
    BID_PRICE: "Bid-Price",
    ASK_PRICE: "Ask-Price",
    ASK_SIZE: "Ask-Size",
    4: "Last-Price",
    5: "Last-Size",
    6: "High",
    7: "Low",
    VOLUME: "Volume",
    CLOSE: "Close-Price",
    14: "Open-Tick",
    TIME: "Time-Tick",
}

# ----------------------------------------------

ST_DISCONNECTED = "disconnected"
ST_SYNC = "sync"
ST_READY = "ready"

CONNECTION = {LINK_STATUS: 1}
DISCONNECTION = {LINK_STATUS: 0}


class SourceStream:
    """The base of any stream source."""

    TRANSLATOR = {
        LINK_STATUS: "x",
        BID_PRICE: "p",
        ASK_PRICE: "p",
        BID_SIZE: "b",
        ASK_SIZE: "a",
        TIME: "t",
        VOLUME: "v",
    }  #: used for translating input data (keys) to neutral data

    POINT_KEYS = set(["p", "l", "h", "v"])
    ACCUM = set(["a", "b"])  #: ask, bid
    SPAN_TRANSLATION = {
        "h": "p",
        "l": "p",
    }

    def __init__(self):
        self.running = False

    def __iter__(self):
        self.running = True
        return self._stream()

    def _stream(self):
        raise NotImplementedError()

    def to_point(self, item):
        """Transform data keys from source
        (i.e broker, etc) to neutral data.
        """
        point = {self.TRANSLATOR.get(k, k): v for k, v in item.items()}
        return point
