"""for full list, see:- https://cdn.materialdesignicons.com/5.4.55/ ."""

import pandas as pd

from prettyqt import iconprovider

from cutepandas.constants import iconnames


def icon_for_dtype(dtype):
    if dtype == bool:
        icon = iconnames.BOOL
    elif str(dtype) == "category":
        icon = iconnames.BOOKMARK
    elif str(dtype) == "datetime64[ns]":
        icon = iconnames.TIME
    elif str(dtype) == "string":
        icon = iconnames.STRING
    elif str(dtype) == "object":
        icon = iconnames.OBJECT
    else:
        icon = iconnames.NUMERIC
    return iconprovider.get_icon(icon, as_qicon=True)


def icon_for_ds(ds):
    if isinstance(ds.index, pd.MultiIndex):
        icon = iconnames.MULTIINDEX
    else:
        icon = iconnames.SINGLEINDEX
    return iconprovider.get_icon(icon, as_qicon=True)


def icon_for_index(index):
    if isinstance(index, pd.RangeIndex):
        icon = iconnames.SORT
    elif isinstance(index, pd.DatetimeIndex):
        icon = iconnames.TIME
    elif isinstance(index, pd.CategoricalIndex):
        icon = iconnames.CATEGORY
    elif index.dtype == "int64":
        icon = iconnames.NUMERIC
    elif index.dtype == "float64":
        icon = iconnames.NUMERIC
    else:
        icon = iconnames.STRING
    return iconprovider.get_icon(icon, as_qicon=True)


def icon_for_history(item):
    if item.is_import_op():
        icon = iconnames.IMPORT
    elif item.operation == "export":
        icon = iconnames.EXPORT
    elif item.operation == "merge":
        icon = iconnames.MERGE
    else:
        icon = iconnames.CALCULATIONS
    return iconprovider.get_icon(icon, as_qicon=True)
