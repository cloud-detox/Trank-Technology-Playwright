import pytest
class TechnologiesPage: 
    def __init__(self,page):
        self.page = page
        self.technologies = page.locator('(//a[text()="Technologies"])[1]')
        
       

    def technologies_hover(self):
        self.technologies.hover()
        self.page.wait_for_timeout(2000)

    def open_technologies_page(self):
        self.technologies.click()
        self.page.wait_for_timeout(2000)

    