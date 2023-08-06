"""Some tools for creating simple plots for debuging.
"""


class Chronogram(dict):
    """A Smart dict that can plot itself."""

    def __init__(self, params=None, *args, **kw):
        super().__init__(*args, **kw)
        self._last_key = None
        self.params = params or dict()
        self.labels = dict()
        self.key_name = "x"
        self.name = "A simle plot"
        self.formats = ("png", "svg")

    def push(self, key, *args, **kw):
        for i, v in enumerate(args):
            kw[f"y{i}"] = v

        if kw != self.get(self._last_key, None):
            self[key] = kw
            self._last_key = key
            for i, k in enumerate(kw.keys()):
                self.params.setdefault(k, {"chart": "plot"})
            return True
        return False

    def sorted_keys(self):
        keys = list(self.keys())
        keys.sort()
        return keys

    def extract(self, *names, **coverters):
        def ident(v):
            return v

        names = names or self.params
        for name in names:
            yield name, [
                coverters.get(name, ident)(self[k][name]) for k in self.sorted_keys()
            ], self.params[name]

    def compute(self):
        """
        - [x] compute df, and outside values

        """
        import pandas as pd

        self.df = df = pd.DataFrame(self).transpose()

        std = df.std()
        mean = df.mean()

        # BBU
        bbu = mean + 1.0 * std
        bbl = mean - 1.0 * std

        # outside values
        xbbu = (df - bbu) > 0
        self.outside_u = xbbu.sum() / xbbu.size

        xbbl = (df - bbl) < 0
        self.outside_l = xbbl.sum() / xbbu.size

        assert (self.outside_l < 0.10).all()  # less than 10% of value are outside
        assert (self.outside_u < 0.10).all()  # less than 10% of value are outside

    def plot(self, **context):
        """Create a simple plot from data."""
        assert isinstance(self, Chronogram)
        import matplotlib.pyplot as plt

        plt.rcdefaults()
        import matplotlib.pyplot as plt

        x = self.sorted_keys()
        params = list(self.params)

        fig, axes = plt.subplots(
            nrows=len(params), constrained_layout=True, figsize=(20, 15)
        )
        axes = dict([(params[i], ax) for (i, ax) in enumerate(axes)])

        for param, y, ctx in self.extract():
            ax = axes[param]
            chart = ctx.get("chart", context.get(param, {}).get("chart", "plot"))
            # ax.plot(x, y)
            eval(f"ax.{chart}(x, y)")
            ax.grid()
            ax.set(
                xlabel=self.key_name,
                ylabel=self.params.get(param).get("name"),
                title=self.labels.get(param, param),
            )

        for fmt in self.formats:
            # plt.savefig(f"{self.name}.{time.time()}.{fmt}", dpi=600)
            plt.savefig(f"{self.name}.{fmt}", dpi=600)
        # plt.show()  # TODO: skip if is runing whitout desktop shell


class BoxedChronogram(Chronogram):
    """Chronogram that average values within a timeframe (acting as *bins*)."""

    def __init__(self, timeframe=None, *args, **kw):
        super().__init__(*args, **kw)
        self.timeframe = timeframe
        self._current_sampes = 0

    def push(self, key, *args, **kw):
        """push a value inside a *timeframe*."""
        if self.timeframe:
            key = key // self.timeframe

        for i, v in enumerate(args):
            kw[f"y{i}"] = v

        if self._last_key != key:
            self._current_sampes = 1
            self[key] = kw
            self.params.update(kw.keys())
        else:
            # get average
            self._current_sampes += 1
            for k, v in kw.items():
                self[key][k] += (v - self[key][k]) / self._current_sampes
