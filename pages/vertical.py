class vertical:

    def __init__(self, page):
        self.page=page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
       
        



    def vertical_hover(self):
        self.vertical.hover()

    def trade_hover(self):
        self.trade.hover()
    
    def retail_hover(self):
        self.retail.hover()

    def healthcare_hover(self):
        self.healthcare.hover()

    def fintech_hover(self):
        self.fintech.hover()

    def custom_hover(self):
        self.custom.hover()