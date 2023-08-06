from .kernel_old import WKernel, WQueue
from .http import iHTTPKernel

from uswarm.tools.logs import logger

log = logger(__name__)


class PyTestKernel(WKernel, iHTTPKernel):
    def __init__(self, uri="kernel://demo", kernel=None, *args, **kw):
        super().__init__(uri, kernel, *args, **kw)

    def _bootstrap_demo(self):
        log.debug(">> _bootstrap_demo")

        def func1(a, b):
            c = a + b
            return c

        def func2(a):
            return 2 * a

        def func3(x):
            log.info(x)
            # sleep(random.random() / 10)

        kernel = self
        q1 = WQueue("demo://demo/1", kernel, func2)
        q2 = WQueue("demo://demo/2", kernel, func2)
        q3 = WQueue("console://demo/1", kernel, func3)

        # build workflow
        q1.subscribe("timer://localhost/secs/5", "a")
        kernel.link(q1, q2)
        kernel.link(q2, q3)

        log.debug("<< _bootstrap_demo")

    def _bootstrap_tcp_client(self):
        log.debug(">> _bootstrap_tcp_client")
        cfg = {"port": 52000}
        uri = "tcp://localhost:{port}".format_map(cfg)
        channel = self.allocate(uri)

        log.debug("<< _bootstrap_tcp_client")

    def _bootstrap_udp_time_server(self):
        log.debug(">> _bootstrap_udp_time_server")
        cfg = {"port": 52000}

        def func1(t):
            channel = self.allocate("broadcast")
            log.info(f"time-server: {channel.uri}: {t}")
            channel.send(t)

        kernel = self
        q1 = WQueue("beacon://localhost/time-server", kernel, func1)
        q1.subscribe("timer://localhost/secs/2", "t")

        log.debug("<< _bootstrap_udp_time_server")

    def _bootstrap_http_pages(self):
        log.debug(">> _bootstrap_http_pages")

        for uri in [
            # "http://mnt:4080",
            "https://www.python.org:443",  #
            "https://www.debian.org:443",  # 20 secs inactivity closing
        ]:
            channel = self.allocate(uri)
            foo = 1

        log.debug("<< _bootstrap_http_pages")
