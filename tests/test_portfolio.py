import pytest
from pages.Portfolio_page import portfolio

@pytest.mark.portfolio
def test_portfolio(page):
    obj_portfolio = portfolio(page)
    obj_portfolio.portfolio_Click()