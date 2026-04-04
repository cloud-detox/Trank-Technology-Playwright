class Graphicdesign:
    def __init__(self,page):
        self.page=page
        self.logo=page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company-in-india"]')
        self.baner=page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company-in-india"]')
        self.pack=page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company-in-india"]')
        self.buss=page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company-in-india"]')

    def graphicdesign_clicking(self):
        self.logo.click()
        self.page.go_back()
        self.baner.click()
        self.page.go_back()
        self.pack.click()
        self.page.go_back()
        self.buss.click()
        self.page.go_back()
    