"""
Integration tests for finshare.stock.index module.
"""

import pytest
import pandas as pd


class TestIndexConstituent:
    @pytest.mark.integration
    def test_get_hs300(self):
        from finshare.stock.index import get_index_constituents
        df = get_index_constituents("000300")
        assert isinstance(df, pd.DataFrame)
        if not df.empty:
            assert "fs_code" in df.columns
            assert len(df) > 100

    @pytest.mark.integration
    def test_get_csi500(self):
        from finshare.stock.index import get_index_constituents
        df = get_index_constituents("000905")
        assert isinstance(df, pd.DataFrame)
        if not df.empty:
            assert "fs_code" in df.columns
            assert "name" in df.columns

    @pytest.mark.integration
    def test_invalid_code_returns_empty(self):
        from finshare.stock.index import get_index_constituents
        df = get_index_constituents("999999")
        assert isinstance(df, pd.DataFrame)
        assert "fs_code" in df.columns
        assert "name" in df.columns


class TestIndexValuation:
    @pytest.mark.integration
    def test_get_pe(self):
        from finshare.stock.index import get_index_pe
        df = get_index_pe("沪深300")
        assert isinstance(df, pd.DataFrame)
        if not df.empty:
            assert "pe" in df.columns
            assert len(df) > 100

    @pytest.mark.integration
    def test_get_pb(self):
        from finshare.stock.index import get_index_pb
        df = get_index_pb("沪深300")
        assert isinstance(df, pd.DataFrame)
        if not df.empty:
            assert "pb" in df.columns

    @pytest.mark.integration
    def test_get_pe_by_code(self):
        from finshare.stock.index import get_index_pe
        df = get_index_pe("000300")
        assert isinstance(df, pd.DataFrame)

    @pytest.mark.integration
    def test_get_pe_columns(self):
        from finshare.stock.index import get_index_pe
        df = get_index_pe("上证指数")
        assert isinstance(df, pd.DataFrame)
        if not df.empty:
            assert "date" in df.columns
            assert "pe" in df.columns

    @pytest.mark.integration
    def test_unknown_symbol_returns_empty(self):
        from finshare.stock.index import get_index_pe
        df = get_index_pe("不存在的指数")
        assert isinstance(df, pd.DataFrame)
        assert "pe" in df.columns
