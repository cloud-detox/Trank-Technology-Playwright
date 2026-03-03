from conftest import page
from utils.screenshot import takeScrnsht

class portfolio:
    def __init__(self, page):
        self.page = page

        #Portfolio
        self.portfolio = page.locator('(//a[text()="Portfolio"])[1]')
        
    def portfolio_Click(self):
        self.portfolio.click()
        self.page.wait_for_load_state()
        takeScrnsht(self.page, "Portfolio")    