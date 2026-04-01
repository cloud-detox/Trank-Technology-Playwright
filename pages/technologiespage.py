class TechnologiesPage:
    
    def __init__(self,page):
        self.page=page
        self.technologies_menu=page.locator('(//a[text()="Technologies"])[1]')
        self.eCOM_Dev=page.locator('//strong[text()="eCommerce Development"]')
        self.Mobile_appdev=page.locator('//strong[text()="Mobile App Development"]')
        self.Artificial_int=page.locator('//li[@data-id="aipage"]')
          
    def hover_technologies(self):
        self.technologies_menu.hover()

    def hover_eComdev(self):
        self.eCOM_Dev.hover()

    def hover_mobileapp(self):
        self.Mobile_appdev.hover()


    





