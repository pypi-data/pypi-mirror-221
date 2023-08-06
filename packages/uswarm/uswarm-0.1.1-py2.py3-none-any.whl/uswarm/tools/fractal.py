import time
from random import shuffle, choice
from collections import deque

import pandas as pd

# ----------------------------------------------------------
# Fractal Graph
# ----------------------------------------------------------


class Fractal:
    MARKET_TYPES = {
        # abrupto
        "wild": [
            (1 / 9, 0.67),
            (5 / 9, 0.33),
        ],
        # tendencia
        "tendency": [
            (1 / 9, 0.30),
            (3 / 9, 0.60),
            (5 / 9, 0.35),
            (6 / 9, 0.50),
            (7 / 9, 0.85),
            (8 / 9, 0.70),
        ],
        "normal": [
            (1 / 9, 0.60),
            (5 / 9, 0.30),
            (8 / 9, 0.70),
        ],
    }

    def __init__(self, depth=0, grid="min", max_points=None, *args, **kw):
        self.depth = depth
        self.grid = grid
        self.max_points = max_points
        self._stack = deque()

    def generate(
        self, start, end, mtype="wild", depth=None, grid=None, quantum=None, max_points=None
    ):
        """Greate a Fractal graph.
        """
        def make_graph(depth, graph, start, end, turns):
            # add points to graph
            graph.add(start)
            graph.add(end)

            if depth > 0:
                # unpack input values
                fromtime, fromvalue = start
                totime, tovalue = end

                # calcualte differences between points
                diffs = []
                last_time, last_val = fromtime, fromvalue
                for t, v in turns:
                    new_time = fromtime + (totime - fromtime) * t
                    new_val = fromvalue + (tovalue - fromvalue) * v
                    diffs.append((new_time - last_time, new_val - last_val))
                    last_time, last_val = new_time, new_val

                # add 'brownian motion' by reordering the segments
                # shuffle(diffs)

                # calculate actual intermediate points and recurse
                last = start
                for segment in diffs:
                    p = last[0] + segment[0], last[1] + segment[1]
                    make_graph(depth - 1, graph, last, p, turns)
                    last = p
                make_graph(depth - 1, graph, last, end, turns)

        depth = depth or self.depth
        grid = grid or self.grid
        graph = set()
        # mtype, turns = choice(list(self.MARKET_TYPES.items()))


        turns = self.MARKET_TYPES[mtype]

        # create a [0,1]x[0,1] Fractal
        _start, _end = (0, 0), (1, 1)
        make_graph(depth, graph, _start, _end, turns)

        # check graph length
        assert len(graph) == (len(turns) + 1) ** depth + 1

        # create a pandas dataframe from Fractal graph
        df = pd.DataFrame(graph)
        df.sort_values(0, inplace=True)
        df.reset_index(drop=True, inplace=True)

        # translate to real coordenates
        X = pd.DataFrame(
            data=[(start[0].timestamp(), start[1]), (end[0].timestamp(), end[1])]
        ).T
        delta = X[1] - X[0]
        Y = df.mul(delta) + X[0]
        Y[0] = [*map(lambda x: pd.to_datetime(x, unit="s"), Y[0])]

        # now resample and interpolate data according to *grid* size
        Z = Y.set_index(0)
        A = Z.resample(self.grid).mean().interpolate()

        return A

    def generate2(
        self, start, end, mtype="normal", depth=None, grid=None, max_points=None
    ):
        graphs = {}
        ncalls = 0

        def make_graph(depth, graph, x0, y0, x1, y1, turns):
            nonlocal ncalls
            ncalls += 1
            # add points to graph
            graph.add((x0, y0))
            graph.add((x1, y1))

            if depth > 0:
                # calcualte differences between points
                diffs = []
                last_time, last_val = x0, y0
                for t, v in turns:
                    new_time = x0 + (x1 - x0) * t
                    new_val = y0 + (y1 - y0) * v
                    diffs.append((new_time - last_time, new_val - last_val))
                    last_time, last_val = new_time, new_val

                # add 'brownian motion' by reordering the segments
                # shuffle(diffs)

                # calculate actual intermediate points and recurse
                for sx, sy in diffs:
                    x = x0 + sx
                    y = y0 + sy
                    make_graph(depth - 1, graph, x0, y0, x, y, turns)
                    x0 = x
                    y0 = y
                make_graph(depth - 1, graph, x0, y0, x1, y1, turns)

        depth = depth or self.depth
        graph = set()
        # mtype, turns = choice(list(self.MARKET_TYPES.items()))
        turns = self.MARKET_TYPES[mtype]
        make_graph(depth, graph, *start, *end, turns)
        return graph, ncalls

    def new_generate(
        self, start, end, mtype="wild", depth=None, grid=None, max_points=None
    ):
        # mtype, turns = choice(list(self.MARKET_TYPES.items()))
        turns = self.MARKET_TYPES[mtype]

        depth = 3 if depth is None else depth
        graph = set()
        ncalls = 0

        def add(*args):
            nonlocal ncalls
            self._stack.append(args)
            ncalls += 1

        add(
            start,
            end,
            depth or self.depth,
            grid or self.grid,
            max_points or self.max_points,
        )

        while self._stack:
            # print(f"len: {len(self._stack)}")
            start, end, depth, grid, max_points = self._stack.popleft()

            if max_points is not None and len(graph) > max_points:
                continue
            # add points to graph
            graph.add(start)
            graph.add(end)

            if depth == 0:
                continue

            # unpack input values
            fromtime, fromvalue = start
            totime, tovalue = end

            if grid is not None:
                if totime - fromtime <= grid:
                    continue

            # calcualte differences between points
            diffs = []
            last_time, last_val = fromtime, fromvalue
            for t, v in turns:
                new_time = fromtime + (totime - fromtime) * t
                new_val = fromvalue + (tovalue - fromvalue) * v
                diffs.append((new_time - last_time, new_val - last_val))
                last_time, last_val = new_time, new_val

            # add 'brownian motion' by reordering the segments
            shuffle(diffs)

            # calculate actual intermediate points and recurse
            last = start
            for segment in diffs:
                p = last[0] + segment[0], last[1] + segment[1]
                add(last, p, depth - 1, grid, max_points)
                last = p
            add(last, end, depth - 1, grid, max_points)

        return graph, ncalls


def plot_graph(graph):
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))
    # plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=15))

    plt.plot(*zip(*sorted(graph)))
    # pyplot.plot(*zip(turns), c="red", marker="x")
    plt.show()


def make_graph(depth, graph, start, end, turns):
    # add points to graph
    graph.add(start)
    graph.add(end)

    if depth > 0:
        # unpack input values
        fromtime, fromvalue = start
        totime, tovalue = end

        # calcualte differences between points
        diffs = []
        last_time, last_val = fromtime, fromvalue
        for t, v in turns:
            new_time = fromtime + (totime - fromtime) * t
            new_val = fromvalue + (tovalue - fromvalue) * v
            diffs.append((new_time - last_time, new_val - last_val))
            last_time, last_val = new_time, new_val

        # add 'brownian motion' by reordering the segments
        # shuffle(diffs)

        # calculate actual intermediate points and recurse
        last = start
        for segment in diffs:
            p = last[0] + segment[0], last[1] + segment[1]
            make_graph(depth - 1, graph, last, p, turns)
            last = p
        make_graph(depth - 1, graph, last, end, turns)

    return graph



def test_fractal_stackoverflow():
    import arrow
    import pandas as pd
    import time

    depth = 5
    # the "geometry" of fractal
    turns = [
            (1 / 9, 0.60),
            (5 / 9, 0.30),
            (8 / 9, 0.70),
        ]

    # select start / end time
    t0 = arrow.now().floor("hours")
    t1 = t0.shift(days=5)
    start = (pd.to_datetime(t0._datetime), 1000)
    end = (pd.to_datetime(t1._datetime), 2000)

    # create a non-dimensionalized [0,1]x[0,1] Fractal
    _start, _end = (0, 0), (1, 1)
    graph = set()
    make_graph(depth, graph, _start, _end, turns)
    # just check graph length
    assert len(graph) == (len(turns) + 1) ** depth + 1

    # create a pandas dataframe from the normalized Fractal
    df = pd.DataFrame(graph)
    df.sort_values(0, inplace=True)
    df.reset_index(drop=True, inplace=True)

    # translate to real coordinates
    X = pd.DataFrame(
            data=[(start[0].timestamp(), start[1]), (end[0].timestamp(), end[1])]
            ).T
    delta = X[1] - X[0]
    Y = df.mul(delta) + X[0]
    Y[0] = [*map(lambda x: pd.to_datetime(x, unit="s"), Y[0])]

    # now resample and interpolate data according to *grid* size
    grid ="min"
    Z = Y.set_index(0)
    A = Z.resample(grid).mean().interpolate()

    # plot both graph to check errors
    import matplotlib.pyplot as plt
    ax = Z.plot()
    A.plot(ax=ax)
    plt.show()

    return A







def test_fractal():
    import arrow
    import pandas as pd
    import time

    fr = Fractal(depth=5)
    # select start / end time
    t0 = arrow.now().floor("hours")
    t1 = t0.shift(days=5)
    start = (pd.to_datetime(t0._datetime), 1000)
    end = (pd.to_datetime(t1._datetime), 2000)

    A = fr.generate(start, end, depth=6, mtype="wild")
    import matplotlib.pyplot as plt
    A.plot()
    plt.show()
    foo = 1


if __name__ == "__main__":
    test_fractal()
