import pytest
from pages.portfolio_page import portfolio

@pytest.mark.portfolio
def test_porfolio(page):
    obj_portfolio = portfolio(page)
    obj_portfolio.portfolio_Click()

    