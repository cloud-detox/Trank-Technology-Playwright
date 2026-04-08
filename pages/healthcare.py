from config import URL

class HealthCare:
    def __init__(self,page):
        self.page = page 
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.health = page.locator("//strong[text()='Healthcare']")
        self.diet = page.locator("(//a[normalize-space()='Diet & Nutritions'])[1]")
        self.track = page.locator("(//a[text()='Health tracking App'])[1]")

        self.list = [self.diet,self.track]

    def health_care(self):
        for i in self.list:
            self.vertical.hover()
            self.page.wait_for_timeout(2000)
            self.health.hover()
            i.click(force=True)
            self.page.wait_for_timeout(2000)
            self.page.goto(URL)
    