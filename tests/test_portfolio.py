import pytest
from pages.Portfolio import Portfolio


@pytest.mark.smoke
def test_portfolio(page):
    p=Portfolio(page)
    p.Portfolio_click()