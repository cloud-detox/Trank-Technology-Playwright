

import pytest

from pages.portfolio_page import PortfolioPage

@pytest.mark.smoke
def test_portfolio_menu(page):
    portfolio=PortfolioPage(page)
    portfolio.open_portfolio()

