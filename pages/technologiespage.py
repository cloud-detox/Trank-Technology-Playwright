class TechnologiesPage:

    def __init__(self, page):
        self.technologies=page.locator('(//a[text()="Technologies"])[1]')
        self.ecommerce=page.locator('//strong[text()="eCommerce Development"]')
        self.Mobile=page.locator('//strong[text()="Mobile App Development"]')
        self.AI=page.locator('//strong[text()="Artificial Intelligence"]')
