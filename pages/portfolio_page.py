import pytest
class PortfolioPage:
    def __init__(self,page):
        self.page = page
        self.portfolio = page.locator('(//a[text()="Portfolio"])[1]')

    def portfolio_hover(self):
        self.portfolio.hover()
        self.page.wait_for_timeout(2000)

    def open_portfolio_page(self):
        self.portfolio.click()
        self.page.wait_for_timeout(4000)
    