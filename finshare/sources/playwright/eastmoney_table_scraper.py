"""配置驱动的东财通用表格抓取器。

东财的概念板块、行业资金流、财报日历页面使用同一套 table.table_wrapper 表格结构。
传入 URL + 列映射即可提取数据，避免为每个页面写一个 scraper。
"""

from __future__ import annotations

import logging
from typing import Any, Optional

from finshare.sources.playwright.base_scraper import BaseScraper

logger = logging.getLogger(__name__)


class EastMoneyTableScraper(BaseScraper):
    """配置驱动的东财表格抓取器。"""

    source_name = "playwright_eastmoney"

    def __init__(
        self,
        url: str,
        column_map: dict[int, str],
        wait_selector: str = "table.table_wrapper",
        row_selector: str = "table.table_wrapper tbody tr",
        cell_selector: str = "td",
        next_selector: Optional[str] = None,
        timeout: int = 30000,
    ):
        self.url = url
        self.column_map = column_map
        self.wait_selector = wait_selector
        self.row_selector = row_selector
        self.cell_selector = cell_selector
        self.next_selector = next_selector
        self.timeout = timeout

    def fetch(self, max_pages: int = 10) -> list[dict]:
        """抓取数据并返回结构化字典列表。"""
        if self.next_selector:
            return self._fetch_paginated(
                self.url,
                wait_selector=self.wait_selector,
                next_selector=self.next_selector,
                max_pages=max_pages,
            )
        return self._fetch_page(self.url, wait_selector=self.wait_selector)

    def _extract(self, page: Any) -> list[dict]:
        """从当前页面提取表格数据。"""
        rows = page.query_selector_all(self.row_selector)
        max_col_index = max(self.column_map.keys()) if self.column_map else 0
        results = []

        for row in rows:
            cells = row.query_selector_all(self.cell_selector)
            if len(cells) <= max_col_index:
                continue

            record = {}
            for col_index, field_name in self.column_map.items():
                text = cells[col_index].inner_text().strip()
                record[field_name] = text
            results.append(record)

        return results
