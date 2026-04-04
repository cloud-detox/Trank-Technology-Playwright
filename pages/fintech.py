from conftest import page
from pages.vertical import vertical

class fintech:
    def __init__(self,page):
        self.page =page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.fintech=page.locator('//strong[text()="Fintech"]')
        self.page.wait_for_timeout(5000)

        self.pos=page.locator('(//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company-in-india"])[1]')
        self.cryp=page.locator('(//a[text()="Crypto"])[1]')
        self.fint_list=[self.pos,self.cryp]
    
    def fintech_clicking(self):
        for i in self.fint_list:
            self.vertical.hover()
            self.fintech.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()