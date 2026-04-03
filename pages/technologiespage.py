class technologies:

    def __init__(self,page):
        self.page = page
        self.technologies=page.locator('(//a[text()="Technologies"])[1]')
        self.E_comm=page.locator('//strong[text()="eCommerce Development"]')
        self.Mobile_app=page.locator('//strong[text()="Mobile App Development"]')
        self.AI=page.locator('//strong[text()="Artificial Intelligence"]')


    def technologies_hover(self):
        self.technologies.hover()

    def E_comm_hover(self):
        self.E_comm.hover()

    def Mobile_app_hover(self):
        self.Mobile_app.hover()

    def AI_hover(self):
        self.AI.hover()

    

    

    


    