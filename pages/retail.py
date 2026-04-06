from conftest import page
from pages.verticalpage import vertical


class RetailPage:
        
        def __init__(self, page):
                self.page = page
                self.vertical = page.locator("(//a[text()='Verticals'])[1]")
                self.retail = page.locator("//strong[text()='Retail and Ecommerce']")

                self.ecomweb=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company-in-india"])[2]')
                self.ecomapp=page.locator('//a[text()="eCommerce App Development"]')

                self.retail_locators=[self.ecomweb,self.ecomapp]

        def retail_clicking(self):
                for i in self.retail_locators:
                        self.vertical.hover()
                        self.retail.hover()
                        i.click()
                        self.page.wait_for_timeout(2000)
                        self.page.go_back()


                     


