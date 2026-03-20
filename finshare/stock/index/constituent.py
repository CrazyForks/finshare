"""
指数成分股数据接口
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


def get_index_constituents(index_code: str) -> pd.DataFrame:
    """
    获取指数成分股列表。

    Args:
        index_code: 指数代码，如 "000300"（沪深300）、"000905"（中证500）

    Returns:
        DataFrame 包含列:
        - fs_code: 股票代码，格式 "000001.SZ"
        - name: 股票简称

    Example:
        >>> df = get_index_constituents("000300")
        >>> print(df.head())
    """
    client = _get_client()
    return client.get_index_constituents(index_code)
