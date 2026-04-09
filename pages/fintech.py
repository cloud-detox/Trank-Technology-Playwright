from pages.vertical import vertical


class FintechPage(vertical):

    def __init__(self, page):
        self.page=page
        super().__init__(page)

        self.fintech=page.locator('//strong[text()="Fintech"]')
        self.PSD=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.CP=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

        self.FN =[self.PSD, self.CP]

    def fintechoption_clicking(self):
          
        for i in self.FN:
            self.vertical_hover()
            self.fintech_hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()  