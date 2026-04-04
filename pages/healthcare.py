from conftest import page
from pages.vertical import vertical

class healthcare:
    def __init__(self,page):
        self.page =page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.healthcare=page.locator('//strong[text()="Healthcare"]')
        self.page.wait_for_timeout(5000)

        self.diet=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.heath=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.heathcare_list=[self.diet,self.heath]

    def health_clicking(self):
        for i in self.heathcare_list:
            self.vertical.hover()
            self.healthcare.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()