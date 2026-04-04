class UIUX:
    def __init__(self,page):
        self.page=page
        self.mob=page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company-in-india"]')
        self.resp=page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company-in-india"]')
        self.brand=page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company-in-india"]')

    def UIUX_clicking(self):
        self.mob.click()
        self.page.go_back()
        self.resp.click()
        self.page.go_back()
        self.brand.click()
        self.page.go_back()