"""
指数估值历史数据接口（PE / PB）
"""

import pandas as pd
from finshare.stock.index.client import IndexClient


_client = None


def _get_client() -> IndexClient:
    """获取客户端单例"""
    global _client
    if _client is None:
        _client = IndexClient()
    return _client


def get_index_pe(symbol: str) -> pd.DataFrame:
    """
    获取指数 PE 历史。

    Args:
        symbol: 指数中文名（如 "沪深300"）或代码（如 "000300"）

    Returns:
        DataFrame 包含列:
        - date: 日期 (datetime)
        - index_val: 指数点位
        - pe: 静态PE
        - pe_ttm: 滚动PE

    Example:
        >>> df = get_index_pe("沪深300")
        >>> print(df.tail())
    """
    client = _get_client()
    return client.get_index_pe(symbol)


def get_index_pb(symbol: str) -> pd.DataFrame:
    """
    获取指数 PB 历史。

    Args:
        symbol: 指数中文名（如 "沪深300"）或代码（如 "000300"）

    Returns:
        DataFrame 包含列:
        - date: 日期 (datetime)
        - index_val: 指数点位
        - pb: 市净率

    Example:
        >>> df = get_index_pb("沪深300")
        >>> print(df.tail())
    """
    client = _get_client()
    return client.get_index_pb(symbol)
