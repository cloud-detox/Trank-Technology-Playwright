from config import URL

class RetailAndEcommerce:

    def __init__(self,page):
        self.page =page 
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.retailandecommerce = page.locator("//strong[text()='Retail and Ecommerce']")
        self.ecomweb = page.locator("(//a[contains(@href,'ecommerce-web-development-company-in-india') and contains(text(),'eCommerce')])[1]")
        self.ecomapp = page.locator("//a[text()='eCommerce App Development']")

        self.list = [self.ecomweb,self.ecomapp]

    def retail_commerce(self):
        for i in self.list:
            self.vertical.hover()
            self.page.wait_for_timeout(2000)
            self.retailandecommerce.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.goto(URL)

