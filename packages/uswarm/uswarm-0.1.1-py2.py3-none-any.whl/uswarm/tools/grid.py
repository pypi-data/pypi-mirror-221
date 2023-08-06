from math import copysign

from ..tools import soft

class Grid(dict):
    """Class for values contained in a 'grid'.

    This class can auto-update some additional parameters:

    - accummulative parameters.
    - max/min parameters.

    Grid support some maths operation as vectors:

    - add, sub, mult, etc.

    Provide some helpers to compute overflows updating the grid:

    - I (unary vector aka identity vector)
    - A (unary accumulated vector)
    - single unitary vectors of 'k' axis.

    """

    ACC = {}  #: keys that holds accumulaitve values of other keys
    MAX = {}  #: keys that holds the max of others keys
    MIN = {}  #: keys that holds the min of others keys

    ROUND = {}  #: grid *size* for each key.
    DEFAULT_GRID = 0.01  #: value used when no ROUND[key] is defined.

    def __init_subclass__(cls, **kwargs):
        """Allows attibute class merging"""

        super().__init_subclass__(**kwargs)
        subclass = cls.mro()[1]
        for key in ("MAX", "MIN", "ROUND"):
            setattr(cls, key, soft(getattr(cls, key, {}), **getattr(subclass, key, {})))

        for key in ("ACC", ):
            value = getattr(cls, key) or set()
            value.update(getattr(subclass, key) or set())
            setattr(cls, key, value)


    def __init__(self, *iterable, **kwargs):
        super().__init__(*iterable, **kwargs)

    def __str__(self):
        s = []
        l = list(self.keys())
        l.sort()
        # point = self.__class__(self)
        # self.round(point)

        for k in l:
            v = self[k]
            if isinstance(v, float):
                s.append(f"{k}: {v:.2f}")  # {:.4f}
            else:
                s.append(f"{k}: {v}")

        s = ", ".join(s)
        return f"<[{s}]>"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        result = self.__class__()
        for k in set(other).intersection(self):
            result[k] = self[k] + other[k]
        return result

    def __sub__(self, other):
        result = self.__class__()
        for k in set(other).intersection(self):
            result[k] = self[k] - other[k]
        return result

    def sub(self, other):
        result = self.__class__(self)
        for k in set(other).intersection(self):
            result[k] = self[k] - other[k]
        return result

    def __mul__(self, other):
        result = self.__class__()
        if isinstance(other, (int, float, bool)):
            for k, v in self.items():
                # result[k] = v * other # avoid ROUND
                dict.__setitem__(result, k, v * other)

        elif isinstance(other, self.__class__):
            for k in set(other).intersection(self):
                # result[k] = self[k] * other[k]
                dict.__setitem__(result, k, self[k] * other[k])
        else:
            raise TypeError(
                f"we can not multiply {self.__class__} by {other.__class__}"
            )
        return result

    def __truediv__(self, other):
        result = self.__class__()
        if isinstance(other, (int, float, bool)):
            for k, v in self.items():
                # result[k] = v / other # avoid ROUND
                dict.__setitem__(result, k, v / other)
        elif isinstance(other, self.__class__):
            for k in set(other).intersection(self):
                # result[k] = self[k] / other # avoid ROUND
                dict.__setitem__(result, k, self[k] / other[k])
        else:
            raise TypeError(f"we can not divide {self.__class__} by {other.__class__}")
        return result

    def __div__(self, other):
        return self.__truediv__(other)

    def __floordiv__(self, other):
        result = self.__class__()
        if isinstance(other, (int, float, bool)):
            for k, v in self.items():
                # result[k] = v // other
                dict.__setitem__(result, k, v // other)
        elif isinstance(other, self.__class__):
            for k in set(other).intersection(self):
                # result[k] = self[k] // other[k]
                dict.__setitem__(result, k, self[k] // other[k])
        else:
            raise TypeError(f"we can not divide {self.__class__} by {other.__class__}")
        return result

    # reflection

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __rdiv__(self, other):
        return self.__div__(other)

    def __setitem__(self, k, v):
        g = self.ROUND.setdefault(k, self.DEFAULT_GRID)
        v = copysign(int(abs(v) / g + 0.0) * g, v)
        super().__setitem__(k, v)

    # unitary vectors
    @property
    def I(self):
        """Return a unary vector for all keys."""

        result = self.__class__({k: 1 for k in self})
        return result

    @property
    def A(self):
        """Return a unary vector just with 'ACC' keys."""
        result = self.__class__({k: 1 if k in self.ACC else 0 for k in self})
        return result

    def single(self, k):
        """Returns a single unitary vertor on 'k'-axis."""
        v = self[k]
        result = self.__class__({k: copysign(1, v)})
        return result

    def copy(self):
        result = self.__class__(self)
        return result

    # automatic properties
    def limits(self):
        """update MAX, MIN auto-keys."""
        for k, k2 in self.MAX.items():
            v = self.get(k)
            if v is not None:
                super().__setitem__(k2, max(self.get(k2, v), v))

        for k, k2 in self.MIN.items():
            v = self.get(k)
            if v is not None:
                super().__setitem__(k2, min(self.get(k2, v), v))

        return self

    def reset(self):
        """reset ACCUM values"""
        for k in self.ACC:
            self[k] = 0

        for k in self.MIN.values():
            self.pop(k, None)

        for k in self.MAX.values():
            self.pop(k, None)

        # self.limits()
        return self

    def move(self, kwargs):
        """Move the point to another location, but
        increassing the accummulative keys as well.
        """
        for k, v in kwargs.items():
            if k in self.ACC:
                v += self.get(k, 0)
            self[k] = v
        return self

    def round(self, shift=0.0):
        """Snap-to-grid the current point."""
        for k, v in list(self.items()):
            g = self.ROUND.setdefault(k, self.DEFAULT_GRID)
            v = copysign(int(abs(v) / g + shift) * g, v)
            super().__setitem__(k, v)
        return self

    def argmax(self):
        """Get the higher value for any key-axis."""
        b_key, b_value = None, None
        for k, v in self.items():
            if not b_key or v > b_value:
                b_key = k
                b_value = v
                return b_key, b_value

    def argmin(self):
        """Get the lower value for any key-axis."""
        b_key, b_value = None, None
        for k, v in self.items():
            if not b_key or v < b_value:
                b_key = k
                b_value = v
                return b_key, b_value

    def argabsmax(self):
        """Get the higher absolute value for any key-axis."""
        b_key, b_value = None, None
        for k, v in self.items():

            if not b_key or abs(v) > abs(b_value):
                b_key = k
                b_value = v
        return b_key, b_value

    def argabsmin(self):
        """Get the lower absolute value for any key-axis."""

        b_key, b_value = None, None
        for k, v in self.items():

            if not b_key or abs(v) < abs(b_value):
                b_key = k
                b_value = v
        return b_key, b_value
