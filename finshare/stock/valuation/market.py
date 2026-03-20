"""
市场估值数据接口 - thin wrappers around ValuationClient
"""

import pandas as pd
from finshare.stock.valuation.client import ValuationClient


_client = None


def _get_client() -> ValuationClient:
    """获取客户端单例"""
    global _client
    if _client is None:
        _client = ValuationClient()
    return _client


def get_market_pb() -> pd.DataFrame:
    """
    获取A股全市场PB中位数历史。

    Returns:
        DataFrame 包含列: date, middlePB, quantileInRecent10YearsMiddlePB, close

    Example:
        >>> from finshare.stock.valuation import get_market_pb
        >>> df = get_market_pb()
    """
    return _get_client().get_market_pb()


def get_global_index_daily(symbol: str) -> pd.DataFrame:
    """
    获取全球指数日线数据。

    Args:
        symbol: 指数代号，支持 HSI, HSTECH, HSCEI, DJI, IXIC, SPX,
                以及带点前缀格式 .DJI, .IXIC, .INX

    Returns:
        DataFrame 包含列: date, open, close, high, low, volume

    Example:
        >>> from finshare.stock.valuation import get_global_index_daily
        >>> df = get_global_index_daily("HSI")
    """
    return _get_client().get_global_index_daily(symbol)


def get_stock_spot() -> pd.DataFrame:
    """
    获取A股全量实时行情（含PE/PB/市值/换手率）。

    Returns:
        DataFrame 包含列: code, name, price, change_pct, pe_ttm, pb,
                          turnover_rate, total_mv, circ_mv,
                          change_pct_60d, change_pct_ytd

    Example:
        >>> from finshare.stock.valuation import get_stock_spot
        >>> df = get_stock_spot()
    """
    return _get_client().get_stock_spot()


def get_etf_classification() -> pd.DataFrame:
    """
    获取ETF基金分类数据。

    Returns:
        DataFrame 包含列: fs_code, fund_type (debt/qdii/money/equity), name

    Example:
        >>> from finshare.stock.valuation import get_etf_classification
        >>> df = get_etf_classification()
    """
    return _get_client().get_etf_classification()
