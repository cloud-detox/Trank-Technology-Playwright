class Graphic_Design:

    def __init__(self,page):
        self.page=page
        self.Graphic_Design=page.locator('//a[text()="Graphic Design"]')
        self.Logo=page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company-in-india"]')
        self.Banner=page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company-in-india"]')
        self.Packaging=page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company-in-india"]')
        self.Business_card=page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company-in-india"]')
        self.Graphic_Design_list=[self.Logo,self.Banner,self.Packaging,self.Business_card]

    def Graphic_Design_click(self):
        for i in self.Graphic_Design_list:
            i.click()
            self.page.go_back()