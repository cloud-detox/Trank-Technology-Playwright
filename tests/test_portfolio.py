from pages.portfolio import portfolio
import pytest

@pytest.mark.smoke
def test_portfolio(page):
    po=portfolio(page)
    po.portfolio_clicking()
