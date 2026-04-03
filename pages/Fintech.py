from conftest import page
from pages.verticalpage import vertical

class Fintech:
    def __init__(self,page):
        self.page=page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.Fintech=page.locator('//strong[text()="Fintech"]')

        self.Pos=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.Crypto=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company-in-india"])[1]')
        self.Fintech_list=[self.Pos,self.Crypto]

    def Fintech_clicking(self):
        for i in self.Fintech_list:
            self.vertical.hover()
            self.Fintech.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()