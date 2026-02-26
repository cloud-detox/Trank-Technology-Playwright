import pytest
from pages.portfolio_page import portfolio

@pytest.mark.order(6)
def test_porfolio(page):
    obj_portfolio = portfolio(page)
    obj_portfolio.portfolio_Click()