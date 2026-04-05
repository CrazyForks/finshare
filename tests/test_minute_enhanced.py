import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from finshare.sources.resilience.smart_router import DataType


class TestMinuteDataEnhanced:
    def setup_method(self):
        from finshare.sources.manager import DataSourceManager
        self.manager = DataSourceManager.__new__(DataSourceManager)
        self.manager.sources = {}
        self.manager.source_status = {}
        self.manager._playwright_sources = {}

    def test_uses_tiered_request(self):
        mock_df = pd.DataFrame({"close": [12.5, 12.6]})
        with patch.object(self.manager, "_tiered_request", return_value=mock_df) as mock_tr:
            df = self.manager.get_minutely_data_tiered("000001", freq=5)
            mock_tr.assert_called_once()
            call_kwargs = mock_tr.call_args
            assert call_kwargs[1]["data_type"] == DataType.MINUTE or call_kwargs[0][0] == DataType.MINUTE
        assert len(df) == 2

    def test_passes_freq_parameter(self):
        with patch.object(self.manager, "_tiered_request", return_value=pd.DataFrame()) as mock_tr:
            self.manager.get_minutely_data_tiered("600036", freq=15, start="2026-04-01")
            call_args = mock_tr.call_args
            # Check kwargs contains freq
            if "kwargs" in call_args[1]:
                assert call_args[1]["kwargs"]["freq"] == 15
            else:
                assert call_args[0][3]["freq"] == 15

    def test_returns_empty_on_failure(self):
        with patch.object(self.manager, "_tiered_request", return_value=None):
            df = self.manager.get_minutely_data_tiered("000001")
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 0
