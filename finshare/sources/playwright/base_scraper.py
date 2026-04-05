"""Base scraper with navigate/wait/paginate patterns."""

from __future__ import annotations

import logging
from typing import Any

from finshare.sources.playwright.browser_pool import get_page

logger = logging.getLogger(__name__)


class BaseScraper:
    """Base class for Playwright page scrapers."""

    source_name: str = "playwright"
    timeout: int = 30000

    def _fetch_page(self, url: str, wait_selector: str | None = None) -> list[dict]:
        """Navigate to URL, wait for selector, call _extract."""
        try:
            with get_page(timeout=self.timeout) as page:
                page.goto(url, wait_until="networkidle", timeout=self.timeout)
                if wait_selector:
                    page.wait_for_selector(wait_selector, timeout=self.timeout)
                return self._extract(page)
        except Exception as e:
            logger.warning(f"[{self.source_name}] scrape {url} failed: {e}")
            return []

    def _fetch_paginated(
        self, url: str, wait_selector: str, next_selector: str, max_pages: int = 50
    ) -> list[dict]:
        """Navigate + paginate, collecting data from each page."""
        all_data = []
        try:
            with get_page(timeout=self.timeout) as page:
                page.goto(url, wait_until="networkidle", timeout=self.timeout)
                if wait_selector:
                    page.wait_for_selector(wait_selector, timeout=self.timeout)

                for _ in range(max_pages):
                    page_data = self._extract(page)
                    if not page_data:
                        break
                    all_data.extend(page_data)

                    next_btn = page.query_selector(next_selector)
                    if next_btn and next_btn.is_enabled():
                        next_btn.click()
                        page.wait_for_load_state("networkidle", timeout=10000)
                        page.wait_for_timeout(500)
                    else:
                        break
        except Exception as e:
            logger.warning(f"[{self.source_name}] paginated scrape failed after {len(all_data)} items: {e}")
        return all_data

    def _extract(self, page: Any) -> list[dict]:
        """Override in subclass: extract data from current page."""
        raise NotImplementedError
