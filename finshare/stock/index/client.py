"""
IndexClient - 指数成分股 + PE/PB 估值历史客户端

提供指数成分股查询（东方财富）和估值历史数据（乐估乐股）。
"""

import pandas as pd
from typing import Optional

from finshare.stock.base_client import BaseClient
from finshare.logger import logger


LG_SYMBOL_MAP = {
    "上证指数": "000001.XSHG",
    "沪深300": "000300.XSHG",
    "中证500": "000905.XSHG",
    "中证1000": "000852.XSHG",
    "创业板指": "399006.XSHE",
    "上证50": "000016.XSHG",
    "深证成指": "399001.XSHE",
    "科创50": "000688.XSHG",
    "中证全指": "000985.XSHG",
    "中证800": "000906.XSHG",
}

# Also support lookup by code (without exchange suffix)
_CODE_TO_LG = {v.split(".")[0]: v for v in LG_SYMBOL_MAP.values()}


class IndexClient(BaseClient):
    """指数成分股 + PE/PB 估值历史客户端"""

    CLIST_URL = "https://push2.eastmoney.com/api/qt/clist/get"
    LG_PE_URL = "https://legulegu.com/api/stockdata/index-pe"
    LG_PB_URL = "https://legulegu.com/api/stockdata/index-pb"

    def __init__(self):
        super().__init__("eastmoney_index")

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _to_secid(self, index_code: str) -> str:
        """
        将指数代码转换为 EastMoney secid 格式。

        首位 0/3/9 → 0.{code}，其余 → 1.{code}
        """
        code = index_code.strip()
        first = code[0] if code else ""
        if first in ("0", "3", "9"):
            return f"0.{code}"
        return f"1.{code}"

    def _resolve_lg_symbol(self, symbol: str) -> Optional[str]:
        """
        将中文名称或代码映射到乐估乐股 symbol。

        支持：
        - 中文名称，如 "沪深300"
        - 纯数字代码，如 "000300"
        - 已包含交易所后缀，如 "000300.XSHG"
        """
        # Direct map by Chinese name
        if symbol in LG_SYMBOL_MAP:
            return LG_SYMBOL_MAP[symbol]

        # Already in legulegu format
        if ".XSHG" in symbol or ".XSHE" in symbol:
            return symbol

        # Lookup by numeric code
        code = symbol.strip()
        if code in _CODE_TO_LG:
            return _CODE_TO_LG[code]

        logger.warning(f"[eastmoney_index] 无法映射指数代码到乐估乐股 symbol: {symbol}")
        return None

    # ------------------------------------------------------------------
    # Public methods
    # ------------------------------------------------------------------

    def get_index_constituents(self, index_code: str) -> pd.DataFrame:
        """
        获取指数成分股列表（东方财富 API）。

        Args:
            index_code: 指数代码，如 "000300"

        Returns:
            DataFrame 包含列:
            - fs_code: 股票代码，格式 "000001.SZ"
            - name: 股票简称
        """
        empty = pd.DataFrame(columns=["fs_code", "name"])
        secid = self._to_secid(index_code)

        logger.debug(f"获取指数成分股: {index_code} (secid={secid})")

        params = {
            "fs": f"b:{secid}",
            "fields": "f12,f14",
            "pz": 10000,
        }
        headers = {"Referer": "https://quote.eastmoney.com/"}

        data = self._make_request(self.CLIST_URL, params=params, headers=headers)

        if not data:
            return empty

        try:
            data_obj = data.get("data") or {}
            diff = data_obj.get("diff", []) if isinstance(data_obj, dict) else []

            if not diff:
                logger.warning(f"[eastmoney_index] 成分股列表为空: {index_code}")
                return empty

            records = []
            for item in diff:
                raw_code = str(item.get("f12", ""))
                name = item.get("f14", "")
                # Convert to fs_code format (000001.SZ)
                fs_code = self._ensure_full_code(raw_code)
                records.append({"fs_code": fs_code, "name": name})

            df = pd.DataFrame(records)
            logger.info(f"获取指数成分股成功: {index_code}, {len(df)}只")
            return df

        except Exception as e:
            logger.error(f"解析指数成分股失败: {e}")
            return empty

    def get_index_pe(self, symbol: str) -> pd.DataFrame:
        """
        获取指数 PE 历史（乐估乐股 API）。

        Args:
            symbol: 指数中文名（如 "沪深300"）或代码（如 "000300"）

        Returns:
            DataFrame 包含列:
            - date: 日期 (datetime)
            - index_val: 指数点位
            - pe: 静态PE
            - pe_ttm: 滚动PE
        """
        empty = pd.DataFrame(columns=["date", "index_val", "pe", "pe_ttm"])
        lg_symbol = self._resolve_lg_symbol(symbol)
        if not lg_symbol:
            return empty

        logger.debug(f"获取指数PE: {symbol} -> {lg_symbol}")

        params = {"token": "", "indexCode": lg_symbol}
        headers = {"Referer": "https://legulegu.com/stockdata/index-pe"}

        data = self._make_request(self.LG_PE_URL, params=params, headers=headers)

        if not data:
            return empty

        try:
            items = data if isinstance(data, list) else data.get("data", [])

            if not items:
                logger.warning(f"[eastmoney_index] PE 数据为空: {symbol}")
                return empty

            records = []
            for item in items:
                records.append({
                    "date": pd.to_datetime(item["date"], unit="ms"),
                    "index_val": item.get("close") or item.get("indexValue") or item.get("index_val"),
                    "pe": item.get("pe"),
                    "pe_ttm": item.get("peTTM") or item.get("pe_ttm"),
                })

            df = pd.DataFrame(records)
            logger.info(f"获取指数PE成功: {symbol}, {len(df)}条")
            return df

        except Exception as e:
            logger.error(f"解析指数PE失败: {e}")
            return empty

    def get_index_pb(self, symbol: str) -> pd.DataFrame:
        """
        获取指数 PB 历史（乐估乐股 API）。

        Args:
            symbol: 指数中文名（如 "沪深300"）或代码（如 "000300"）

        Returns:
            DataFrame 包含列:
            - date: 日期 (datetime)
            - index_val: 指数点位
            - pb: 市净率
        """
        empty = pd.DataFrame(columns=["date", "index_val", "pb"])
        lg_symbol = self._resolve_lg_symbol(symbol)
        if not lg_symbol:
            return empty

        logger.debug(f"获取指数PB: {symbol} -> {lg_symbol}")

        params = {"token": "", "indexCode": lg_symbol}
        headers = {"Referer": "https://legulegu.com/stockdata/index-pb"}

        data = self._make_request(self.LG_PB_URL, params=params, headers=headers)

        if not data:
            return empty

        try:
            items = data if isinstance(data, list) else data.get("data", [])

            if not items:
                logger.warning(f"[eastmoney_index] PB 数据为空: {symbol}")
                return empty

            records = []
            for item in items:
                records.append({
                    "date": pd.to_datetime(item["date"], unit="ms"),
                    "index_val": item.get("close") or item.get("indexValue") or item.get("index_val"),
                    "pb": item.get("pb"),
                })

            df = pd.DataFrame(records)
            logger.info(f"获取指数PB成功: {symbol}, {len(df)}条")
            return df

        except Exception as e:
            logger.error(f"解析指数PB失败: {e}")
            return empty
