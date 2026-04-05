"""Playwright-based web scraping — last-resort fallback when all API sources fail."""

from finshare.sources.playwright.browser_pool import get_page, is_available

__all__ = ["get_page", "is_available"]
