from conftest import page
from pages.verticalpage import vertical


class Retail_Ecommerce:

    def __init__(self,page):
        self.page=page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.Retail_Ecommerce=page.locator('//strong[text()="Retail and Ecommerce"]')

        self.Ecommerce_web=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company-in-india"])[2]')
        self.Ecommerce_App=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.Retail_Ecommerce_list=[self.Ecommerce_web,self.Ecommerce_App]

    def Retail_Ecommerce_clicking(self):
        for i in self.Retail_Ecommerce_list:
            self.vertical.hover()
            self.Retail_Ecommerce.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()