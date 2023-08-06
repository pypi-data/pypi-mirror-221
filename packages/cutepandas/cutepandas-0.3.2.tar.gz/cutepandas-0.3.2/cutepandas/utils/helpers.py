from __future__ import annotations

import logging
import logging.config

import numpy as np


logger = logging.getLogger(__name__)


def infer_type(text: str):
    try:
        if float(text).is_integer():
            return int(text)
        return float(text)
    except (TypeError, ValueError):
        return text


def format_name(name) -> str:
    if isinstance(name, tuple | list):
        return " | ".join(str(i) for i in name)
    return str(name)


def is_nan(obj) -> bool:
    try:
        return np.isnan(obj) if isinstance(obj, float) else False
    except TypeError:
        return False
