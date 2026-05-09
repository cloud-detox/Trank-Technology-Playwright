import pytest

from pages.portfolio_page import portfolio_page

@pytest.mark.smoke
def test_portfolio_page(page):
    portfolio = portfolio_page(page)
    portfolio.portfolio_menu_clicking()

def test_portfolio_links(page):
    portfolio = portfolio_page(page)
    portfolio.portfolio_links_clicking()

