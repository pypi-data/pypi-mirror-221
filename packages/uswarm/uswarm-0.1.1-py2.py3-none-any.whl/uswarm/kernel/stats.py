# ------------------------------------------------
# Stats
# ------------------------------------------------
class Stats(dict):
    def __init__(self, *iterable, **kwargs):
        super().__init__(*iterable, **kwargs)
        self.means = {}

    def push(self, t0, data):
        self.setdefault(t0, {}).update(data)

    def compute(self, historical=10):
        keys = list(self.keys())
        keys.sort()
        while len(self) > historical:
            self.pop(keys.pop(0))

        self.means = {}
        for wave, data in self.items():
            for k, v in data.items():
                self.means.setdefault(k, []).append(v)

        for key, values in list(self.means.items()):
            self.means[key] = sum(values) / len(values)
