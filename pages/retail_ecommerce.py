from conftest import page
from pages.vertical import vertical

class retail_ecommerce:
    def __init__(self,page):
        self.page =page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.retail_ecommerce=page.locator('//strong[text()="Retail and Ecommerce"]')
        self.page.wait_for_timeout(5000)
        self.ecom=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company-in-india"])[2]')
        self.ecommDev=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.retail_list=[self.ecom,self.ecommDev]
        
    def retail_clicking(self):
        for i in self.retail_list:
            self.vertical.hover()
            self.retail_ecommerce.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()