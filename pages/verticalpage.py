class vertical:

    def __init__(self, page):
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.trading=page.locator('//strong[text()="Trading"]')
        self.retail=page.locator('//strong[text()="Retail and Ecommerce"]')
        self.healthcare=page.locator('//strong[text()="Healthcare"]')
        self.fintech=page.locator('//strong[text()="Fintech"]')
        self.custom_app=page.locator('//strong[text()="Custom App"]')




