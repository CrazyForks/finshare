"""
Integration tests for finshare.stock.valuation module.
"""

import pytest
import pandas as pd


class TestMarketPB:
    @pytest.mark.integration
    def test_get_market_pb(self):
        from finshare.stock.valuation import get_market_pb
        df = get_market_pb()
        assert isinstance(df, pd.DataFrame)
        # May be empty if legulegu requires token
        if not df.empty:
            assert "date" in df.columns
            assert "middlePB" in df.columns
            assert "quantileInRecent10YearsMiddlePB" in df.columns
            assert "close" in df.columns

    @pytest.mark.integration
    def test_market_pb_returns_dataframe_on_error(self):
        from finshare.stock.valuation import get_market_pb
        df = get_market_pb()
        # Should never raise, always return DataFrame
        assert isinstance(df, pd.DataFrame)


class TestGlobalIndex:
    @pytest.mark.integration
    def test_hsi(self):
        from finshare.stock.valuation import get_global_index_daily
        df = get_global_index_daily("HSI")
        assert isinstance(df, pd.DataFrame)
        if not df.empty:
            assert "close" in df.columns
            assert "date" in df.columns
            assert len(df) > 100

    @pytest.mark.integration
    def test_djia(self):
        from finshare.stock.valuation import get_global_index_daily
        df = get_global_index_daily("DJI")
        assert isinstance(df, pd.DataFrame)
        if not df.empty:
            assert "close" in df.columns

    @pytest.mark.integration
    def test_dot_prefix_symbol(self):
        from finshare.stock.valuation import get_global_index_daily
        df = get_global_index_daily(".DJI")
        assert isinstance(df, pd.DataFrame)

    @pytest.mark.integration
    def test_unknown_symbol_returns_empty(self):
        from finshare.stock.valuation import get_global_index_daily
        df = get_global_index_daily("UNKNOWN_XYZ")
        assert isinstance(df, pd.DataFrame)
        assert "close" in df.columns
        assert df.empty

    @pytest.mark.integration
    def test_columns_present(self):
        from finshare.stock.valuation import get_global_index_daily
        df = get_global_index_daily("HSI")
        assert isinstance(df, pd.DataFrame)
        if not df.empty:
            for col in ["date", "open", "close", "high", "low", "volume"]:
                assert col in df.columns


class TestStockSpot:
    @pytest.mark.integration
    def test_get_spot(self):
        from finshare.stock.valuation import get_stock_spot
        df = get_stock_spot()
        assert isinstance(df, pd.DataFrame)
        if not df.empty:
            assert "pe_ttm" in df.columns
            assert "pb" in df.columns
            assert len(df) > 3000

    @pytest.mark.integration
    def test_spot_columns(self):
        from finshare.stock.valuation import get_stock_spot
        df = get_stock_spot()
        assert isinstance(df, pd.DataFrame)
        if not df.empty:
            for col in ["code", "name", "price", "change_pct", "pe_ttm", "pb",
                        "turnover_rate", "total_mv", "circ_mv"]:
                assert col in df.columns


class TestEtfClassification:
    @pytest.mark.integration
    def test_classification(self):
        from finshare.stock.valuation import get_etf_classification
        df = get_etf_classification()
        assert isinstance(df, pd.DataFrame)
        if not df.empty:
            assert "fund_type" in df.columns
            assert "fs_code" in df.columns
            assert "name" in df.columns

    @pytest.mark.integration
    def test_fund_types_valid(self):
        from finshare.stock.valuation import get_etf_classification
        df = get_etf_classification()
        assert isinstance(df, pd.DataFrame)
        if not df.empty:
            valid_types = {"debt", "qdii", "money", "equity"}
            assert set(df["fund_type"].unique()).issubset(valid_types)

    @pytest.mark.integration
    def test_has_equity_etfs(self):
        from finshare.stock.valuation import get_etf_classification
        df = get_etf_classification()
        assert isinstance(df, pd.DataFrame)
        if not df.empty:
            assert "equity" in df["fund_type"].values
