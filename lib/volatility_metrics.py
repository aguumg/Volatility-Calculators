# volatility_metrics.py

import numpy as np
import pandas as pd

# ------------------------- #
# Basic Return Calculations
# ------------------------- #

def compute_log_returns(price_series: pd.Series) -> pd.Series:
    """
    Compute log returns of a price series.
    """
    return np.log(price_series / price_series.shift(1))


def compute_rolling_mean(series: pd.Series, window: int) -> pd.Series:
    """
    Compute rolling mean of a series.
    """
    return series.rolling(window).mean()


def compute_rolling_std(series: pd.Series, window: int) -> pd.Series:
    """
    Compute rolling standard deviation of a series.
    """
    return series.rolling(window).std()


def compute_z_score(series: pd.Series, window: int) -> pd.Series:
    """
    Compute Z-score over a rolling window.
    """
    rolling_mean = compute_rolling_mean(series, window)
    rolling_std = compute_rolling_std(series, window)
    return (series - rolling_mean) / rolling_std

# ------------------------- #
# Candle-Based Volatility
# ------------------------- #

def normalized_candle_height(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """
    Normalized candle height: (High - Low) / Close.
    """
    return (high - low) / close


def range_over_price(high: pd.Series, low: pd.Series, close: pd.Series, window: int) -> pd.Series:
    """
    Rolling version of normalized candle height.
    """
    range_ = (high.rolling(window).max() - low.rolling(window).min())
    return range_ / close

# ------------------------- #
# Trend + Volatility Combo
# ------------------------- #

def rate_of_change(price: pd.Series, window: int) -> pd.Series:
    """
    Rate of change: (Close_t - Close_t-window) / Close_t-window
    """
    return (price - price.shift(window)) / price.shift(window)


def average_true_range(high: pd.Series, low: pd.Series, close: pd.Series, window: int) -> pd.Series:
    """
    Average True Range (ATR) using the Wilder smoothing method.
    """
    high_low = high - low
    high_close = (high - close.shift(1)).abs()
    low_close = (low - close.shift(1)).abs()
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    return tr.rolling(window).mean()


def efficiency_ratio(roc: pd.Series, atr: pd.Series) -> pd.Series:
    """
    Efficiency ratio: ROC / ATR. High when trends are strong and smooth.
    """
    return roc / atr

if __name__ == '__main__':
    import pandas as pd

    df = pd.read_csv("data/BTCBUSD-1h-data.csv", parse_dates=["timestamp"])
