"""Tests for MemoryCache stale fallback behavior."""
import time
from finshare.cache.cache import MemoryCache


def test_get_returns_none_for_expired_without_deleting():
    """get() should return None for expired entries but NOT delete them."""
    cache = MemoryCache()
    cache.set("key1", "value1", ttl=1)
    time.sleep(1.1)
    assert cache.get("key1") is None
    assert cache._cache.get("key1") is not None


def test_get_stale_returns_expired_data():
    """get_stale() should return data even if expired."""
    cache = MemoryCache()
    cache.set("key1", "value1", ttl=1)
    time.sleep(1.1)
    result = cache.get_stale("key1")
    assert result == "value1"


def test_get_stale_returns_none_for_missing_key():
    """get_stale() should return None for keys that never existed."""
    cache = MemoryCache()
    assert cache.get_stale("nonexistent") is None


def test_get_stale_returns_fresh_data():
    """get_stale() should also work for non-expired data."""
    cache = MemoryCache()
    cache.set("key1", "value1", ttl=60)
    assert cache.get_stale("key1") == "value1"


def test_get_still_works_for_fresh_data():
    """get() should still return fresh data normally."""
    cache = MemoryCache()
    cache.set("key1", "value1", ttl=60)
    assert cache.get("key1") == "value1"


def test_eviction_cleans_stale_entries():
    """When cache is full, _evict_oldest should remove stale entries."""
    cache = MemoryCache(max_size=2)
    cache.set("old", "old_val", ttl=1)
    time.sleep(1.1)
    cache.set("new1", "val1", ttl=60)
    cache.set("new2", "val2", ttl=60)
    assert cache.get_stale("old") is None
