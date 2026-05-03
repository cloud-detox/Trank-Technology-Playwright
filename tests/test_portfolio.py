

import pytest

from config import BASE_URL
from pages.portfoliopage import portfolio

@pytest.mark.smoke
def test_portfolio(page):
    obj5 = portfolio(page)
    obj5.portfolio_method()