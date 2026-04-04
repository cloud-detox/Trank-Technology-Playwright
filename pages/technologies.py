class technologies:
    def __init__(self,page):
        self.page=page
        self.technology=page.locator('(//a[text()="Technologies"])[1]')
        self.ecommD=page.locator('//strong[text()="eCommerce Development"]')
        self.MADev=page.locator('//strong[text()="Mobile App Development"]')
        self.AI=page.locator('//strong[text()="Artificial Intelligence"]')

    def technology_hover(self):
        self.technology.hover()
       

    def ecommD_hover(self):
        self.ecommD.hover()
       

    def MADev_hover(self):
        self.MADev.hover()
      

    def AI_hover(self):
        self.AI.hover()
      