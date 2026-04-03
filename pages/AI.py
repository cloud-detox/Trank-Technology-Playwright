from conftest import page
from pages.technologiespage import technologies

class AI:

    def __init__(self,page):
        self.page=page
        self.technologies=page.locator('(//a[text()="Technologies"])[1]')
        self.AI=page.locator('//strong[text()="Artificial Intelligence"]')

    def  AI_click(self): 
            self.technologies.hover()
            self.AI.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()