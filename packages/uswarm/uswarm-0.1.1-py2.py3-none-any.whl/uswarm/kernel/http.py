import re

import lzma as xz
import gzip as gz
import zlib

from .stm import *
from .channel import (
    CONTENT_LENGTH,
    CONTENT_TYPE,
    CONTENT_ENCODING,
    EVENT_RX,
    Message,
    RESPONSE_SINGLE,
    TCPChannel,
)

from uswarm.tools import soft
# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger
log = logger(__name__)

HTTP_HEADER_CUT = b"\r\n\r\n"

# https://www.geeksforgeeks.org/http-headers-content-encoding/?ref=lbp
HTTP_ENCODING = {
    "gzip": gz.decompress,  # It uses Lempel-Ziv coding (LZ77), with a 32-bit CRC format. It is the original format of UNIX gzip program.
    "compress": xz.decompress,  # It uses Lempel-Ziv-Welch (LZW) algorithm. Due to patent issue, many modern browsers don’t support this type of content-encoding.
    "deflate": zlib.decompress,  # This format uses zlib structure with deflate compression algorithm.
    #'br': 4, # It is a compression format using the Brotli algorithm.
    "identity": lambda x: x,  # no compression
    None: lambda x: x,  # no compression
}

# https://www.geeksforgeeks.org/http-headers-content-type/
HTTP_TYPE_REG = {
    r"chartset": r"charset=(?P<charset>[\w\-]+)",
}

HTTP_TYPE_FUNC = {
    r"chartset": lambda body, charset, **kw: body.decode(charset),
}


class HTTPMessage(Message):
    """HTTP response messages"""

    def decode(self):
        body = self["body"]

        # decompress
        encoding = self.get(CONTENT_ENCODING)
        body = HTTP_ENCODING.get(encoding, HTTP_ENCODING["identity"])(body)

        # decode
        content_type = self.get(CONTENT_TYPE, "")
        for encoding, pattern in HTTP_TYPE_REG.items():
            m = re.search(pattern, content_type)
            if m:
                d = m.groupdict()
                func = HTTP_TYPE_FUNC.get(encoding)
                if func:
                    body = func(body, **d)

        self["body"] = body
        self["status"] = self["status"].decode("utf-8")


class HTTPChannel(TCPChannel):
    HTTP_REQ = """GET {path} HTTP/1.1
Host: {host}
User-Agent: curl/7.54.0
Accept-Encoding: gzip, deflate


"""
    #: render tenplates for outgoing messages
    META_REQUEST = {  # TODO: change to "render"
        "default": (
            RESPONSE_SINGLE,
            dict,
            """GET {path} HTTP/1.1
Host: {host}
User-Agent: curl/7.54.0
Accept-Encoding: gzip, deflate


""",
            {"path": "/"},
            (),
            {},
        ),
    }

    def __init__(self, *args, **kw):
        kw.setdefault("factory", HTTPMessage)
        super().__init__(*args, **kw)

    # ----------------------------------------------------------------
    # STM callbacks methods
    # ----------------------------------------------------------------
    def conn_2_sync(self, event, data, wave, *args, **kw):
        """By default, Sync State just:

        - request the / page.
        - check 200 status
        - move to live
        """
        # log.debug(f"1. sock: {self.sock}")
        # log.info(f"GET {self.uri}")

        soft(self._uri, path="/")
        request = self.request(self.uri)
        # log.debug(f"3. sock: {self.sock}")

    def dispatch_sync(self, event, data, wave, *args, **kw):
        self.dispatch_live(event, data, wave, *args, **kw)
        if data["status"][0] not in ("4", "5"):
            # page is ok retrieved
            self.asap(EVENT_NEXT)

    def dispatch_live(self, event, data, wave, *args, **kw):
        data.decode()
        log.debug(f"dispatching: {data}")

    # ----------------------------------------------------------------
    # High I/O
    # ----------------------------------------------------------------
    def _encoder(self, *message):
        """Encode data to be sent to server"""
        raw = super()._encoder(*message)
        raw = raw.replace("\n", "\r\n")
        raw = bytes(raw, "utf-8")
        return raw

    def get_old(self, uri, **kw):
        soft(kw, **self._uri)
        request = self.HTTP_REQ.format_map(kw)

        request = request.replace("\n", "\r\n")
        raw = bytes(request, "utf-8")
        self._write(raw)
        return request

    # ----------------------------------------------------------------
    # rx/tx mechanism
    # ----------------------------------------------------------------

    def rx(self):
        """HTTP protocol uses always same RX strategy,
        so we don't need to change the way that incoming
        messages are handled.

        - [ ] Transfer-Encoding: chunked (i.e google)

        """
        super().rx()  # don't make a

        msg = self.message

        body_len = msg.get(CONTENT_LENGTH, False)
        if body_len:
            if len(self._raw) >= body_len:
                msg["body"] = self._raw[:body_len]
                self._raw = self._raw[body_len:]
                self.asap(EVENT_RX, msg)
        else:
            header = self._raw.split(HTTP_HEADER_CUT, 1)
            if len(header) < 2:
                # header is too big that is still not completed
                # to the best way is wait for it and then
                # process normally
                return

            self._raw = header[-1]
            lines = header[0].splitlines()

            if not msg.get("status", False):
                line = lines.pop(0).split(b" ")
                msg["protocol"], msg["status"] = line[:2]

            # redirects = []
            # while True:
            # if self._raw[:4] == b"HTTP":
            ## TODO: what to do with redirects
            # redirects.append(header)
            # continue
            # break

            for line in lines:
                if line:
                    key, value = [
                        x.decode("ISO-8859-1").strip() for x in line.split(b":", 1)
                    ]
                    msg[key.lower()] = value
                else:
                    foo = 1

            if CONTENT_LENGTH in msg:
                msg[CONTENT_LENGTH] = int(msg[CONTENT_LENGTH])

            foo = 1


