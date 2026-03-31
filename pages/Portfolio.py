class Portfolio:

    def __init__(self, page):
        self.page = page
        self.portfolio = page.locator('//a[@href="https://www.tranktechnologies.com/portfolio"]')
