"""ETF list scraper from 10jqka via Playwright."""
from __future__ import annotations
import logging
from typing import Any
from finshare.sources.playwright.base_scraper import BaseScraper

logger = logging.getLogger(__name__)

_TYPE_KEYWORDS = [
    ("qdii", ["QDII", "纳斯达克", "标普", "香港", "海外", "全球"]),
    ("money", ["货币", "现金", "流动性"]),
    ("bond", ["债券", "国债", "企债", "信用", "纯债"]),
    ("commodity", ["黄金", "原油", "商品", "大宗"]),
    ("stock", []),
]

class ETFListScraper(BaseScraper):
    source_name = "10jqka_playwright"
    timeout = 30000
    URL = "https://fund.10jqka.com.cn/etf_list.html"
    WAIT_SELECTOR = "table.tb-zp"
    NEXT_SELECTOR = "a.next"

    def fetch(self) -> list[dict]:
        etfs = self._fetch_paginated(self.URL, self.WAIT_SELECTOR, self.NEXT_SELECTOR, max_pages=30)
        for etf in etfs:
            etf["etf_type"] = self._classify(etf.get("name", ""), etf.get("typename", ""))
        logger.info(f"[ETFListScraper] fetched {len(etfs)} ETFs")
        return etfs

    def _extract(self, page: Any) -> list[dict]:
        results = []
        rows = page.query_selector_all("table.tb-zp table tbody tr")
        for row in rows:
            cells = row.query_selector_all("td")
            if len(cells) < 3:
                continue
            code = cells[0].inner_text().strip()
            name = cells[1].inner_text().strip()
            typename = cells[2].inner_text().strip()
            if code and name:
                results.append({"code": code, "name": name, "typename": typename})
        return results

    @staticmethod
    def _classify(name: str, typename: str) -> str:
        text = f"{name} {typename}".upper()
        for etf_type, keywords in _TYPE_KEYWORDS:
            if any(kw.upper() in text for kw in keywords):
                return etf_type
        return "stock"
