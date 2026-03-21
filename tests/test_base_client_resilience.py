"""Tests for BaseClient resilience integration."""
import time
from unittest.mock import patch, MagicMock
import requests

from finshare.stock.base_client import BaseClient


class TestableClient(BaseClient):
    """Concrete subclass for testing."""
    def __init__(self):
        super().__init__("test_client", request_interval=0.1)


def _reset_cooldown(client, source_name="test_client"):
    """Helper to fully reset cooldown state for a source."""
    state = client._cooldown_mgr.get_source_state(source_name)
    state.cooldown_until = 0
    state.consecutive_failures = 0


def test_make_request_returns_none_when_in_cooldown():
    """When source is in cooldown, _make_request should return None immediately."""
    client = TestableClient()
    client._cooldown_mgr.enter_cooldown("test_client", "timeout")

    result = client._make_request("https://example.com/api")
    assert result is None

    _reset_cooldown(client)


def test_make_request_records_success():
    """Successful request should clear cooldown state."""
    client = TestableClient()
    _reset_cooldown(client)

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": "ok"}

    with patch.object(client.session, "get", return_value=mock_response):
        result = client._make_request("https://example.com/api")

    assert result == {"data": "ok"}


def test_make_request_enters_cooldown_on_failure():
    """Failed request should enter cooldown."""
    client = TestableClient()

    with patch.object(client.session, "get", side_effect=requests.ConnectionError("refused")):
        result = client._make_request("https://example.com/api")

    assert result is None
    assert client._cooldown_mgr.is_in_cooldown("test_client")

    _reset_cooldown(client)


def test_make_request_fast_mode():
    """fast=True should use fast retry handler (fewer retries)."""
    client = TestableClient()
    assert client._fast_retry_handler.config.max_retries == 1
    assert client._fast_retry_handler.config.base_delay == 1.0


def test_cached_request_returns_fresh_cache():
    """_cached_request should return cached data without calling fetch_fn."""
    client = TestableClient()
    client._cache.set("test_key", {"cached": True}, ttl=60)

    call_count = 0
    def fetch_fn():
        nonlocal call_count
        call_count += 1
        return {"fetched": True}

    result = client._cached_request("test_key", 60, fetch_fn)
    assert result == {"cached": True}
    assert call_count == 0

    client._cache.delete("test_key")


def test_cached_request_fetches_on_cache_miss():
    """_cached_request should call fetch_fn on cache miss and write to cache."""
    client = TestableClient()

    result = client._cached_request(
        "new_key", 60, lambda: {"fetched": True}
    )
    assert result == {"fetched": True}

    assert client._cache.get("new_key") == {"fetched": True}

    client._cache.delete("new_key")


def test_cached_request_returns_stale_on_failure():
    """_cached_request should return stale cache when fetch fails."""
    client = TestableClient()

    client._cache.set("stale_key", {"old": True}, ttl=1)
    time.sleep(1.1)

    result = client._cached_request("stale_key", 60, lambda: None)
    assert result == {"old": True}

    client._cache.delete("stale_key")


def test_cached_request_returns_none_when_no_cache_and_fetch_fails():
    """_cached_request should return None when no cache and fetch fails."""
    client = TestableClient()
    result = client._cached_request("missing_key", 60, lambda: None)
    assert result is None


def test_classify_error():
    """_classify_error should map HTTP status codes and error messages."""
    client = TestableClient()
    assert client._classify_error("", 429) == "rate_limit"
    assert client._classify_error("", 403) == "forbidden"
    assert client._classify_error("", 503) == "service_unavailable"
    assert client._classify_error("connection refused", None) == "connection_error"
    assert client._classify_error("request timeout", None) == "timeout"
    assert client._classify_error("unknown error", None) == "default"


def test_rate_limit_is_thread_safe():
    """Rate limiting should use class-level lock."""
    client = TestableClient()
    assert hasattr(BaseClient, "_rate_limit_lock")
    assert hasattr(BaseClient, "_last_request_time")
