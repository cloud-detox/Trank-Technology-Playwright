class vertical:
    def __init__(self,page):
        self.page =page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.trading=page.locator('//strong[text()="Trading"]')
        self.retail_ecommerce=page.locator('//strong[text()="Retail and Ecommerce"]')
        self.healthcare=page.locator('//strong[text()="Healthcare"')
        self.fintech=page.locator('//strong[text()="Fintech"]')
        self.customapp=page.locator('//strong[text()="Custom App"]')


    def vertical_hover(self):
        self.vertical.hover()
        

    def trading_hover(self):
        self.trading.hover()
        
    def retail_ecomerce_hover(self):
        self.retail_ecommerce.hover()

    def healthcare_hover(self):
        self.healthcare.hover()

    def fintech_hover(self):
        self.fintech.hover()

    def customapp_hover(self):
        self.customapp.hover()

    

    