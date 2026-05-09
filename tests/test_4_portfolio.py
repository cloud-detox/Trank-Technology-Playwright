import pytest

from pages.potfolio_page import Portfolio

@pytest.mark.smoke
def test_portfolip(page):
    obj = Portfolio(page)
    obj.portfoliomethod()