from functools import wraps

import pandas as pd

from prettyqt import core


class Signals(core.Object):
    changed = core.Signal(object)


TO_DECORATE = [
    "dot",
    "transpose",
    "query",
    "eval",
    "select_dtypes",
    "insert",
    "assign",
    "align",
    "set_axis",
    "reindex",
    "drop",
    "rename",
    "fillna",
    "pop",
    "replace",
    "shift",
    "set_index",
    "reset_index",
    "dropna",
    "drop_duplicates",
    "duplicated",
    "sort_values",
    "sort_index",
    "value_counts",
    "nlargest",
    "nsmallest",
    "swaplevel",
    "reorder_levels",
    "compare",
    "combine",
    "combine_first",
    "update",
    "groupby",
    "pivot",
    "pivot_table",
    "stack",
    "explode",
    "unstack",
    "melt",
    "diff",
    "aggregate",
    "agg",
    "any",
    "transform",
    "apply",
    "applymap",
    "join",
    "merge",
    "round",
    "corr",
    "cov",
    "corrwith",
    "count",
    "nunique",
    "idxmin",
    "idxmax",
    "mode",
    "quantile",
    "asfreq",
    "resample",
    "isin",
    "hist",
    "boxplot",
    "ffill",
    "bfill",
    "clip",
    "interpolate",
    "where",
    "mask",
    "all",
    "sem",
    "var",
    "std",
    "cummin",
    "cummax",
    "cumsum",
    "cumprod",
    "sum",
    "prod",
    "product",
    "mean",
    "skew",
    "kurt",
    "kurtosis",
    "median",
    "max",
    "min",
    "add",
    "radd",
    "sub",
    "mul",
    "truediv",
    "floordiv",
    "mod",
    "pow",
    "rmul",
    "rsub",
    "rtruediv",
    "rfloordiv",
    "rpow",
    "rmod",
    "div",
    "rdiv",
    "eq",
    "ne",
    "lt",
    "gt",
    "le",
    "ge",
    "multiply",
    "subtract",
    "divide",
]


def wrapper(method):
    @wraps(method)
    def wrapped(*args, **kwargs):
        old_shape = args[0].shape
        # print(old_shape)
        result = method(*args, **kwargs)
        # print(result.shape)
        if str(result.shape) != str(old_shape):
            result.signals.changed.emit((old_shape, result.shape))
        return result

    return wrapped


class MetaClass(type):
    def __new__(cls, classname, bases, classDict):
        newClassDict = classDict
        for attributeName, attribute in bases[0].__dict__.items():
            if attributeName in TO_DECORATE:
                attribute = wrapper(attribute)
                newClassDict[attributeName] = attribute
        return type.__new__(cls, classname, bases, newClassDict)


class QtFrame(pd.DataFrame, metaclass=MetaClass):
    _metadata = ["_fn"]
    signals = Signals()

    @property
    def _constructor(self):
        return QtFrame

    def copy(self, deep=True):
        copied = super().copy(deep=deep)
        if type(copied) is pd.DataFrame:
            copied.__class__ = QtFrame
            copied._geometry_column_name = self._geometry_column_name
        return copied

    # def __finalize__(self, other, method=None, **kwargs):
    #     """Propagate metadata from other to self."""
    #     self = super().__finalize__(other, method=method, **kwargs)
    #     # merge operation: using metadata of the left object
    #     if method == "merge":
    #         for name in self._metadata:
    #             self.__setattr__(name, getattr(other.left, name, None))
    #     # concat operation: using metadata of the first object
    #     elif method == "concat":
    #         for name in self._metadata:
    #             self.__setattr__(name, getattr(other.objs[0], name, None))
    #     return self


app = core.app()
frame = QtFrame(dict(a=[1, 2]))
frame.signals.changed.connect(print)
frame = frame.T
frame = frame.T
frame = frame.T
