import logging
import numpy as np
from crawlutils.text_utils import make_num

logger = logging.getLogger(__name__)


일억 = 100_000_000
일조 = 1_000_000_000_000


def format_number_100m(num, default="-"):
    if num is None:
        return default

    if num != num:  # isnan
        return default

    try:
        if num > 일조:
            return f"{int(num/일조):,}조 {int((num % 일조)/일억):,}억"
        elif num > 일억:
            return f"{int(num/일억):,}억"
        else:
            return f"{int(num):,}"
    except Exception as ex:
        logging.exception(ex)
        raise ValueError

def check_unit(check_text):
    if '조원' in check_text:
        unit = 1_000_000_000_000
    elif '억원' in check_text:
        unit = 100_000_000
    elif '백만원' in check_text:
        unit = 1_000_000
    elif '천원' in check_text:
        unit = 1_000
    elif '원' in check_text:
        unit = 1
    else:
        logging.error(f"check_text not contains unit string {check_text}")
        raise ValueError
    return unit


def defaultIfNumber(text, unit_multiplier, default="-"):
    op_num = make_num(text)
    op = default if op_num == '-' or op_num == '' else round(float(op_num) * unit_multiplier)
    return op


def limit_cap(num: float, min: int, max: int) -> float:
    if num != num:  # isnan
        return num
    elif num < min:
        return min
    elif num > max:
        return max
    else:
        return num

def to_int(text: str) -> int:
    """
    type of np.nan == float
    :param text:
    :return:
    """
    if text is None:
        return np.nan
    elif isinstance(text, float):
        if text != text:  # isnan
            return np.nan
        else:
            return int(text)
    elif isinstance(text, int):
        return text
    try:
        t = text.replace(",", "").replace(" ", "")
        if t == "-":
            return np.nan
        return np.nan if t == '' else int(float(t))
    except Exception as ex:
        logging.exception(f"{text} => {ex}")
        return np.nan


def to_float(text: str) -> float:
    if text is None:
        return np.nan
    elif isinstance(text, float):
        return text

    try:
        t = text.replace(",", "").replace(" ", "")
        if t == "-":
            return np.nan
        return np.nan if t == '' else float(t)
    except Exception as ex:
        logging.exception(f"{text} => {ex}")
        return np.nan


def aof_ratio(actual: int, forecast: int) -> float:
    """
    Actual over Forecast ratio
    :param actual:
    :param forecast:
    :return:
    """
    if actual != actual or forecast != forecast:    # isnan
        return np.nan

    return (actual - forecast) / forecast * 100 if forecast != 0 else np.nan
