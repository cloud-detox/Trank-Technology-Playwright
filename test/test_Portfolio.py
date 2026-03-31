import pytest

from pages.Portfolio import Portfolio

@pytest.mark.smoke
def test_portfolio(page):
      p = Portfolio(page)
      p.portfolio.click()
      page.wait_for_timeout(5000)
