"""Tests for individual stock money flow (get_money_flow_stock)."""
import pytest
import pandas as pd
from unittest.mock import patch


class TestEastMoneyMoneyFlowStock:
    def test_returns_dataframe(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        mock_json = {"data": {"klines": [
            "2026-04-04,1000000,800000,200000,500000,400000,100000",
            "2026-04-05,1200000,900000,300000,600000,500000,100000",
        ]}}
        with patch.object(source, "_make_request", return_value=mock_json):
            df = source.get_money_flow_stock("000001")
        assert len(df) == 2
        assert "trade_time" in df.columns
        assert "main_net" in df.columns
        assert "retail_net" in df.columns

    def test_empty_response(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        with patch.object(source, "_make_request", return_value=None):
            df = source.get_money_flow_stock("000001")
        assert len(df) == 0

    def test_no_data_key(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        with patch.object(source, "_make_request", return_value={"data": None}):
            df = source.get_money_flow_stock("000001")
        assert len(df) == 0

    def test_empty_klines(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        with patch.object(source, "_make_request", return_value={"data": {"klines": []}}):
            df = source.get_money_flow_stock("000001")
        assert len(df) == 0

    def test_columns_present(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        mock_json = {"data": {"klines": ["2026-04-05,1200000,900000,300000,600000,500000,100000"]}}
        with patch.object(source, "_make_request", return_value=mock_json):
            df = source.get_money_flow_stock("600519")
        expected_cols = {"trade_time", "main_inflow", "main_outflow", "main_net",
                         "retail_inflow", "retail_outflow", "retail_net"}
        assert expected_cols.issubset(df.columns)

    def test_numeric_values(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        mock_json = {"data": {"klines": ["2026-04-05,1200000.0,900000.0,300000.0,600000.0,500000.0,100000.0"]}}
        with patch.object(source, "_make_request", return_value=mock_json):
            df = source.get_money_flow_stock("000001")
        assert df.iloc[0]["main_net"] == 300000.0
        assert df.iloc[0]["retail_net"] == 100000.0

    def test_skips_short_lines(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        mock_json = {"data": {"klines": [
            "2026-04-04,1000000,800000",  # too short — should be skipped
            "2026-04-05,1200000,900000,300000,600000,500000,100000",
        ]}}
        with patch.object(source, "_make_request", return_value=mock_json):
            df = source.get_money_flow_stock("000001")
        assert len(df) == 1

    def test_sh_code_conversion(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        mock_json = {"data": {"klines": ["2026-04-05,500000,400000,100000,200000,150000,50000"]}}
        with patch.object(source, "_make_request", return_value=mock_json) as mock_req:
            df = source.get_money_flow_stock("600519.SH")
        # Verify the request was made (secid format for SH should start with "1.")
        call_kwargs = mock_req.call_args
        params = call_kwargs[1].get("params", call_kwargs[0][1] if len(call_kwargs[0]) > 1 else {})
        assert params.get("secid", "").startswith("1.")


class TestEarningsCalendarAndPreannouncement:
    def test_get_earnings_calendar_returns_dataframe(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        mock_json = {"result": {"data": [
            {"SECURITY_CODE": "000001", "SECURITY_NAME_ABBR": "平安银行",
             "REPORT_DATE": "2026-03-31", "REPORT_TYPE": "年报"}
        ]}}
        with patch.object(source, "_make_request", return_value=mock_json):
            df = source.get_earnings_calendar("2026-04-15")
        assert len(df) == 1
        assert df.iloc[0]["code"] == "000001"

    def test_get_earnings_calendar_empty(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        with patch.object(source, "_make_request", return_value=None):
            df = source.get_earnings_calendar("2026-04-15")
        assert len(df) == 0

    def test_get_earnings_preannouncement_returns_dataframe(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        mock_json = {"result": {"data": [
            {"REPORT_DATE": "2026-03-31", "PREDICT_TYPE": "预增",
             "PREDICT_CONTENT": "净利润增长50%-80%", "NOTICE_DATE": "2026-01-15"}
        ]}}
        with patch.object(source, "_make_request", return_value=mock_json):
            df = source.get_earnings_preannouncement("000001")
        assert len(df) == 1
        assert df.iloc[0]["pre_type"] == "预增"

    def test_get_earnings_preannouncement_empty(self):
        from finshare.sources.eastmoney_source import EastMoneyDataSource
        source = EastMoneyDataSource()
        with patch.object(source, "_make_request", return_value={"result": None}):
            df = source.get_earnings_preannouncement("000001")
        assert len(df) == 0
