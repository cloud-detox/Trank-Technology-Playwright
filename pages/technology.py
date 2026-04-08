class technology:

    def __init__(self, page):
        self.page=page
        self.technology=page.locator('(//a[text()="Technologies"])[1]')
        self.commerce=page.locator('//strong[text()="eCommerce Development"]')
        self.mobileapp=page.locator('//strong[text()="Mobile App Development"]')
        
        



    def technology_hover(self):
        self.technology.hover()

    def commerce_hover(self):
        self.commerce.hover()

    def mobileapp_hover(self):
        self.mobileapp.hover()

    def ai_hover(self):
        self.ai.hover()