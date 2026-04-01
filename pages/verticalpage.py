class VerticalPage:

    def __init__(self, page):
        self.page = page
        self.vertical_menu=page.locator('(//a[text()="Verticals"])[1]')
        self.trading_menu=page.locator('//strong[text()="Trading"]')
        self.Retail_eco_menu=page.locator('//strong[text()="Retail and Ecommerce"]')
        self.Helthcare_menu=page.locator('//strong[text()="Healthcare"]')
        self.Fintech_menu=page.locator('//strong[text()="Fintech"]')
        self.Customerapp_menu=page.locator('//strong[text()="Custom App"]')

    def hover_vertical(self):
        self.vertical_menu.hover()

    def hover_trading(self):
        self.trading_menu.hover()

    def hover_retail(self):
        self.Retail_eco_menu.hover()

    def hover_healthcare(self):
        self.Helthcare_menu.hover()

    def hover_fintech(self):
        self.Fintech_menu.hover()

    def hover_customerapp(self):
        self.Customerapp_menu.hover()

