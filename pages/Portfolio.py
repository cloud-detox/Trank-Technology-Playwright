class Portfolio:

    def __init__(self,page):
        self.page=page
        self.Portfolio=page.locator('//a[text()="Portfolio"]')

    def Portfolio_click(self):
        self.Portfolio.click()
        self.page.go_back()
        