"""HTTP API for Swarm Module"""
import time
import re

# from struct import pack, unpack
# from datetime import datetime
# from dateutil.parser import parse
# from asyncio import gather, sleep

# from .parsers import dict_decode
from .reactor import Response, RESPONSE_SINGLE

from .network import NetWorker, StreamedApi, StreamMessage

# ----------------------------------------------------
# HTTP Protocol
# ----------------------------------------------------

reg_status_line = re.compile(
    r"(?P<protocol_version>[^\s]*)\s+(?P<code>[^\s]*)\s+(?P<status>.*)$"
)
reg_header = re.compile(r"(?P<key>[^:]*):\s+(?P<value>.*)$")

BEGING_BODY_MARK = b"\r\n"
LENGTH_BODY_MARK = len(BEGING_BODY_MARK)
CONTENT_LENGTH = "Content-Length"


class HTTPMessage(StreamMessage):
    def __init__(self, api, **kw):
        super().__init__(api, **kw)
        self.header_completed = False
        self.status = ""

    # def parse(self, dec):
    # """Decode Message:
    # Example:
    # self.dom = dict_decode(list(dec), list(self.body))
    # return self.dom

    # """
    # self.dom = dict_decode(list(dec), list(self.body))
    # return self.dom

    def feed(self, raw):
        self.raw += raw

        if not self.header_completed:
            lines = self.raw.split(BEGING_BODY_MARK)
            if len(lines) > 1:
                header = self.header
                if not self.status:
                    self.status = self.decode(lines.pop(0))
                    m = reg_status_line.match(self.status)
                    if m:
                        for key, value in m.groupdict().items():
                            header[key] = value
                    else:
                        raise RuntimeError("Bad status line!!")
                    # TODO: process error codes
                while lines:
                    m = reg_header.match(self.decode(lines[0]))
                    if m:
                        key, value = m.groups()
                        header[key] = value
                        lines.pop(0)
                    else:
                        break
                raw = BEGING_BODY_MARK.join(lines)
                if raw.startswith(BEGING_BODY_MARK):
                    self.header_completed = True
                    self.length = int(self.header[CONTENT_LENGTH])
                    tail = raw[self.length + LENGTH_BODY_MARK :]
                    self.raw = raw[LENGTH_BODY_MARK : self.length]
                else:
                    tail = b""
                    self.raw = raw

        if self.header_completed:
            if len(self.raw) >= self.length:
                tail = self.raw[self.length :]
                self.raw = self.raw[: self.length]
                self.body = [self.raw]
            else:
                # print(f"{len(self.raw)} --> {self.length}")
                tail = b""

        return tail


class HTTPResponse(Response):
    def feed(self, message):
        # TODO: review 206 cases (partials)
        # TODO: check if response is completed now
        completed = True
        if completed:
            self.set_result(message)  # TODO: check what to do with body

        return completed


class HTTPClient(StreamedApi):

    RESPONSE_KLASS = HTTPResponse
    INCOMING_KLASS = HTTPMessage

    template = {
        "default": (
            RESPONSE_SINGLE,
            dict,
            """GET {path} HTTP/1.1
{headers}

""",
            {},
            (),
            {},
        ),
    }

    # Human MSG_ID mapping
    in_mapping = {
        None: "GET",  # special case
        "200": "/ok",
        "404": "/forbidden",
    }

    incoming_mid_name = {
        "200": "Response OK",
        "404": "Forbidden",
    }

    extract = {
        "default": (True, "", (("payload", str),)),
    }

    def _populate_handlers(self):
        """Populate incoming messages handlers"""

        for mid in None, "200", "404":
            self.handler[mid] = self._get

    def _render_request(self, req, template, debug=False):
        """Render the request based on template protocol definition."""
        # HTTP need to rebuild the readers
        headers = [f"{k}: {v}" for k, v in req.items() if k[0].isupper()]
        headers = "\r\n".join(headers)
        raw = self.encoder(template.format(headers=headers, **req))
        return raw

    def _create_request(self, url, **req):
        req = super()._create_request(url, **req)

        # extend some HTTP headers
        req["Host"] = req["host"]
        req["Accept"] = "text/html"

        return req

    def _set_handshaking_requirements(self):
        """Set the futures needed *flags* for a completed handshaking."""
        # set needed handshaking flags
        #self._handshaking_add_flags(None)
        super()._set_handshaking_requirements()

    async def _do_handshaking(self):
        await super()._do_handshaking()

    # ---------------------------------------------------
    # handlers
    # ---------------------------------------------------
    def _get(self, msg):

        rid = msg.get_rid()
        if rid is None:
            rid = list(self.waiting.keys())
            if rid:
                rid = rid[0]
        return rid


class HTTPSClient(HTTPClient):
    pass


NetWorker.register("http", dict(klass=HTTPClient, port=80))
NetWorker.register("https", dict(klass=HTTPClient, port=443))
