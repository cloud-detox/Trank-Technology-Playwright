class vertical:

    def __init__(self,page):
        self.page = page
        self.vertical = page.locator('(//a[text()="Verticals"])[1]')
        self.Trading=page.locator('(//strong[text()="Trading"]')
        self.Retail_Ecommerce=page.locator('//strong[text()="Retail and Ecommerce"]')
        self.Healthcare=page.locator('//strong[text()="Healthcare"]')
        self.Fintech=page.locator('//strong[text()="Fintech"]')
        self.Custom_app=page.locator('(//a[@href="#"])[4]')

       

    def vertical_hover(self):
        self.vertical.hover()

    def Trading_hover(self):
        self.Trading.hover()

    def Retail_Ecommerce_hover(self):
        self.Retail_Ecommerce.hover()

    def Healthcare_hover(self):
        self.Healthcare.hover()

    def Fintech_hover(self):
        self.Fintech.hover()

    def Custom_app_hover(self):
        self.Custom_app.hover()

    

        
        

