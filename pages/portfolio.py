class portfolio:
    def __init__(self,page):
        self.page=page
        self.portfolio=page.locator('//a[text()="Portfolio"]')

    def portfolio_clicking(self):
        self.portfolio.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()
       
