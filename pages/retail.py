from pages.vertical import vertical


class RetailPage(vertical):

    def __init__(self, page):
        self.page=page
        super().__init__(page)
        self.retail=page.locator('//strong[text()="Retail and Ecommerce"]')
        self.ECWD=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.EAWD=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

        self.RP = [self.ECWD,self.EAWD]

    def retailoption_clicking(self):
          
        for i in self.RP:
            self.vertical_hover()
            self.retail_hover()
            i.click()
            self.page.wait_for_timeout(2500)
            self.page.go_back()  
        