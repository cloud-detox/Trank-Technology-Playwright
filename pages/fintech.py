from conftest import page
from pages.verticalpage import vertical


class FintechPage:
        
        def __init__(self, page):
                self.page = page
                self.vertical = page.locator("(//a[text()='Verticals'])[1]")
                self.fintech = page.locator ('//strong[text()="Fintech"]')  

                self.fin1 = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
                self.fin2 = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company-in-india"])[1]')

                self.fintech_locators=[self.fin1 ,self.fin2]

        def fintech_clicking(self):
                for i in self.fintech_locators:
                        self.vertical.hover()
                        self.fintech.hover()
                        i.click()
                        self.page.wait_for_timeout(2000)
                        self.page.go_back()