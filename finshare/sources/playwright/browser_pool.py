"""Playwright browser pool — thread-safe singleton, auto-cleanup."""

from __future__ import annotations

import atexit
import threading
import logging
from contextlib import contextmanager
from typing import Generator

logger = logging.getLogger(__name__)

_lock = threading.Lock()
_playwright_instance = None
_browser = None
_ref_count = 0


def _ensure_browser():
    global _playwright_instance, _browser
    if _playwright_instance is None:
        from playwright.sync_api import sync_playwright
        _playwright_instance = sync_playwright().start()
        _browser = _playwright_instance.chromium.launch(headless=True)
        atexit.register(_cleanup)
        logger.info("[PlaywrightPool] browser launched")


def _cleanup():
    global _playwright_instance, _browser
    if _browser is not None:
        try:
            _browser.close()
        except Exception:
            pass
        _browser = None
    if _playwright_instance is not None:
        try:
            _playwright_instance.stop()
        except Exception:
            pass
        _playwright_instance = None


@contextmanager
def get_page(timeout: int = 30000) -> Generator:
    """Get a new page from shared browser. Auto-closes on exit.

    Usage:
        with get_page() as page:
            page.goto("https://example.com")
    """
    global _ref_count
    with _lock:
        _ensure_browser()
        _ref_count += 1

    page = _browser.new_page()
    page.set_default_timeout(timeout)
    try:
        yield page
    finally:
        try:
            page.close()
        except Exception:
            pass
        with _lock:
            _ref_count -= 1
            if _ref_count == 0:
                _cleanup()


def is_available() -> bool:
    """Check if Playwright is installed (not imported until needed)."""
    try:
        import playwright  # noqa: F401
        return True
    except ImportError:
        return False
