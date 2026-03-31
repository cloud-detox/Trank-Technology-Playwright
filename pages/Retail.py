class Retail:

    def __init__(self, page):
        self.page = page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.retail=page.locator('//strong[text()="Retail and Ecommerce"]')
        self.ECWD=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company-in-india"])[2]')
        self.ECAD=page.locator('//a[text()="eCommerce App Development"]')
    
        self.Ret=[self.ECWD,self.ECAD] 
        

    def retail_options(self):
        for i in self.Ret:
          self.vertical.hover()
          self.retail.hover()
          i.click()
          self.page.wait_for_timeout(2000)
          self.page.go_back()

