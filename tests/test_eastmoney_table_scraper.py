import pytest
from unittest.mock import MagicMock, patch


class TestEastMoneyTableScraper:
    def test_init_stores_config(self):
        from finshare.sources.playwright.eastmoney_table_scraper import EastMoneyTableScraper

        scraper = EastMoneyTableScraper(
            url="https://quote.eastmoney.com/center/boardlist.html#concept_board",
            column_map={0: "code", 1: "name", 2: "change_pct"},
            wait_selector="table.table_wrapper",
        )
        assert scraper.url == "https://quote.eastmoney.com/center/boardlist.html#concept_board"
        assert scraper.column_map == {0: "code", 1: "name", 2: "change_pct"}
        assert scraper.wait_selector == "table.table_wrapper"

    def test_extract_parses_table_rows(self):
        from finshare.sources.playwright.eastmoney_table_scraper import EastMoneyTableScraper

        scraper = EastMoneyTableScraper(
            url="https://example.com",
            column_map={0: "code", 1: "name", 2: "change_pct"},
        )

        mock_page = MagicMock()

        mock_cell_0_0 = MagicMock()
        mock_cell_0_0.inner_text.return_value = "BK0493"
        mock_cell_0_1 = MagicMock()
        mock_cell_0_1.inner_text.return_value = "新能源"
        mock_cell_0_2 = MagicMock()
        mock_cell_0_2.inner_text.return_value = "2.35%"

        mock_cell_1_0 = MagicMock()
        mock_cell_1_0.inner_text.return_value = "BK0655"
        mock_cell_1_1 = MagicMock()
        mock_cell_1_1.inner_text.return_value = "芯片"
        mock_cell_1_2 = MagicMock()
        mock_cell_1_2.inner_text.return_value = "-1.20%"

        mock_row_0 = MagicMock()
        mock_row_0.query_selector_all.return_value = [mock_cell_0_0, mock_cell_0_1, mock_cell_0_2]
        mock_row_1 = MagicMock()
        mock_row_1.query_selector_all.return_value = [mock_cell_1_0, mock_cell_1_1, mock_cell_1_2]

        mock_page.query_selector_all.return_value = [mock_row_0, mock_row_1]

        result = scraper._extract(mock_page)
        assert len(result) == 2
        assert result[0] == {"code": "BK0493", "name": "新能源", "change_pct": "2.35%"}
        assert result[1] == {"code": "BK0655", "name": "芯片", "change_pct": "-1.20%"}

    def test_extract_skips_rows_with_insufficient_cells(self):
        from finshare.sources.playwright.eastmoney_table_scraper import EastMoneyTableScraper

        scraper = EastMoneyTableScraper(
            url="https://example.com",
            column_map={0: "code", 1: "name", 2: "change_pct"},
        )

        mock_page = MagicMock()
        mock_cell = MagicMock()
        mock_cell.inner_text.return_value = "BK0493"
        mock_row = MagicMock()
        mock_row.query_selector_all.return_value = [mock_cell]

        mock_page.query_selector_all.return_value = [mock_row]

        result = scraper._extract(mock_page)
        assert len(result) == 0

    def test_fetch_delegates_to_fetch_paginated(self):
        from finshare.sources.playwright.eastmoney_table_scraper import EastMoneyTableScraper

        scraper = EastMoneyTableScraper(
            url="https://example.com",
            column_map={0: "code"},
            next_selector="a.next",
        )

        with patch.object(scraper, "_fetch_paginated", return_value=[{"code": "BK0001"}]) as mock_fp:
            result = scraper.fetch(max_pages=5)
            mock_fp.assert_called_once_with(
                "https://example.com",
                wait_selector="table.table_wrapper",
                next_selector="a.next",
                max_pages=5,
            )
            assert result == [{"code": "BK0001"}]

    def test_fetch_uses_fetch_page_when_no_next_selector(self):
        from finshare.sources.playwright.eastmoney_table_scraper import EastMoneyTableScraper

        scraper = EastMoneyTableScraper(
            url="https://example.com",
            column_map={0: "code"},
        )

        with patch.object(scraper, "_fetch_page", return_value=[{"code": "BK0001"}]) as mock_fp:
            result = scraper.fetch()
            mock_fp.assert_called_once_with("https://example.com", wait_selector="table.table_wrapper")
            assert result == [{"code": "BK0001"}]
