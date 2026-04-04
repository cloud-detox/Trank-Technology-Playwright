from conftest import page
from pages.technologies import technologies

class AI:
    def __init__(self,page):
        self.page=page
        self.technology=page.locator('(//a[text()="Technologies"])[1]')
        self.AI=page.locator('//strong[text()="Artificial Intelligence"]')

    def AI_clicking(self):
        self.technology.hover()
        self.AI.click()
        self.page.go_back()
        self.page.wait_for_timeout(2000)