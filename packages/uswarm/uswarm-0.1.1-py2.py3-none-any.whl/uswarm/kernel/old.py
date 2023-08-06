
# ------------------------------------------------
# Antiguo kernel
# ------------------------------------------------
class NOQUEUE:
    pass


class DemoKernel_old(WKernel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.fibers = {}  # the running fibers (if any)

    def _start_fiber(self, name, func):
        th = threading.Thread(name=name, target=func)
        self.debug(f"Starting fiber: '{name}'")
        th.start()
        self.fibers[name] = th

    def stop(self):
        self.running = False
        # wait all fibers stop
        remain = True
        while remain:
            time.sleep(0.1)
            remain = [th.is_alive() for th in self.fibers.values()]
            remain = any(remain)

    def put(self, url, event):  # TODO: review
        queue = self.queues.get(url)
        if queue is None:
            pass
        else:
            queue.put(event)
            self.scheduler.add(queue)

    def get(self, url):  # TODO: review
        queue = self.queues.get(url)
        if queue is None:
            event = NOQUEUE
        else:
            event = queue.get()
        return event

    def _pool_workers_3(self, name):
        log.debug(f">> {name}")
        n = 0
        while self.scheduler or self.running:
            # try to get a queue to dispatch an event
            try:
                # TODO: use queues instead deque
                queue = self.scheduler.pop()
                while True:
                    event = queue.get()
                    # print(f"{name}: got {event}")
                    if not n % 500:
                        log.debug(f"- {name}: {n} done.")
                    # do the 'task'
                    time.sleep(event * 0.005)
                    n += 1
            except IndexError as why:
                time.sleep(random.random() * 0.2)
                foo = 1

        log.debug(f"<< {name}: {n} works done!")

    def _loop_bootstrap(self):
        log.debug(">> loop_bootstrap")

        queue = TQueue(url="A")
        self.register_queue(queue)

        queue = TQueue(url="B")
        self.register_queue(queue)

        self._start_fiber("demo", self._demo)

        while self.running:
            # log.debug("---")
            time.sleep(1)
        log.debug("<< loop_bootstrap")

    def _demo(self):
        self.put("A", 3.1415)
        self.put("A", 1.4142)

        log.debug(self.get("A"))
        log.debug(self.get("A"))

        while self.running:
            time.sleep(random.random() * 0.002)
            self.put("B", random.random())
        foo = 1
