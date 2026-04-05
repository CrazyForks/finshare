"""Tests for concept board routing: EastMoneyDataSource methods and Manager routing."""
import pytest
import pandas as pd
from unittest.mock import patch


class TestEastMoneyConceptMethods:
    def test_has_get_concept_list(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        assert hasattr(EastMoneyDataSource(), "get_concept_list")

    def test_get_concept_list_returns_dataframe(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        mock_json = {"data": {"diff": [{"f12": "BK0493", "f14": "新能源", "f3": 2.35, "f62": 1000000, "f184": 5.2}]}}
        with patch.object(source, "_make_request", return_value=mock_json):
            df = source.get_concept_list()
        assert len(df) == 1
        assert df.iloc[0]["board_name"] == "新能源"

    def test_get_concept_list_empty_response(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        with patch.object(source, "_make_request", return_value=None):
            df = source.get_concept_list()
        assert len(df) == 0

    def test_get_concept_list_columns(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        mock_json = {"data": {"diff": [{"f12": "BK0001", "f14": "AI", "f3": 1.5, "f62": 500000, "f184": 2.1}]}}
        with patch.object(source, "_make_request", return_value=mock_json):
            df = source.get_concept_list()
        assert set(["board_code", "board_name", "change_pct", "net_inflow", "net_inflow_ratio"]).issubset(df.columns)

    def test_get_concept_constituents_returns_dataframe(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        mock_json = {"data": {"diff": [{"f12": "000001", "f14": "平安银行"}, {"f12": "600519", "f14": "贵州茅台"}]}}
        with patch.object(source, "_make_request", return_value=mock_json):
            df = source.get_concept_constituents("BK0493")
        assert len(df) == 2
        assert "fs_code" in df.columns
        assert "000001.SZ" in df["fs_code"].values
        assert "600519.SH" in df["fs_code"].values

    def test_get_concept_constituents_empty(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        with patch.object(source, "_make_request", return_value=None):
            df = source.get_concept_constituents("BK0001")
        assert len(df) == 0

    def test_get_concept_money_flow_returns_dataframe(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        mock_json = {"data": {"diff": [{"f14": "新能源", "f62": 1000000, "f184": 5.2, "f3": 2.35}]}}
        with patch.object(source, "_make_request", return_value=mock_json):
            df = source.get_concept_money_flow()
        assert len(df) == 1
        assert df.iloc[0]["concept"] == "新能源"
        assert "net_inflow" in df.columns

    def test_get_concept_money_flow_empty(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        with patch.object(source, "_make_request", return_value={"data": None}):
            df = source.get_concept_money_flow()
        assert len(df) == 0


class TestManagerRouting:
    def setup_method(self):
        from finshare.sources.manager import DataSourceManager
        self.manager = DataSourceManager.__new__(DataSourceManager)
        self.manager.sources = {}
        self.manager.source_status = {}
        self.manager._playwright_sources = {}

    def test_get_concept_list(self):
        with patch.object(self.manager, "_tiered_request", return_value=pd.DataFrame({"board_name": ["AI"]})):
            df = self.manager.get_concept_list()
        assert len(df) == 1

    def test_get_concept_list_none_fallback(self):
        with patch.object(self.manager, "_tiered_request", return_value=None):
            df = self.manager.get_concept_list()
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 0

    def test_get_concept_constituents(self):
        with patch.object(self.manager, "_tiered_request", return_value=pd.DataFrame({"fs_code": ["000001.SZ"]})):
            df = self.manager.get_concept_constituents("BK0493")
        assert len(df) == 1

    def test_get_concept_money_flow(self):
        with patch.object(self.manager, "_tiered_request", return_value=pd.DataFrame({"concept": ["新能源"]})):
            df = self.manager.get_concept_money_flow()
        assert len(df) == 1

    def test_get_money_flow_stock(self):
        with patch.object(self.manager, "_tiered_request", return_value=pd.DataFrame({"main_net": [100]})):
            df = self.manager.get_money_flow_stock("000001")
        assert len(df) == 1

    def test_get_earnings_calendar(self):
        with patch.object(self.manager, "_tiered_request", return_value=pd.DataFrame({"code": ["000001"]})):
            df = self.manager.get_earnings_calendar("2026-04-15")
        assert len(df) == 1

    def test_get_earnings_preannouncement(self):
        with patch.object(self.manager, "_tiered_request", return_value=pd.DataFrame({"pre_type": ["预增"]})):
            df = self.manager.get_earnings_preannouncement("000001")
        assert len(df) == 1

    def test_get_market_overview(self):
        with patch.object(self.manager, "_tiered_request", return_value=pd.DataFrame({"up_count": [3200]})):
            df = self.manager.get_market_overview()
        assert len(df) == 1

    def test_get_margin_trading_summary(self):
        with patch.object(self.manager, "_tiered_request", return_value=pd.DataFrame({"margin_buy": [50e9]})):
            df = self.manager.get_margin_trading_summary()
        assert len(df) == 1
