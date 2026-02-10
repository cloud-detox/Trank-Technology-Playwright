import pytest
from pages.portfolio_page import portfolio_page_class
from utils.csv_data_loader import CSVDataLoader

@pytest.mark.smoke
def test_portfolio(page):
    expected_titles = CSVDataLoader.load_expected_titles("testdata/portfolio.csv")

    abpout_menu=portfolio_page_class(page)
    abpout_menu.click_portfolio(expected_titles) 