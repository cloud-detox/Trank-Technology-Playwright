from conftest import page
from pages.verticalpage import vertical


class Healthcare:

    def __init__(self,page):
        self.page=page

        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.Healthcare=page.locator('//strong[text()="Healthcare"]')

        self.Diet_Nutrition=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.Health_tracking_app=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.Healthcare_list=[self.Diet_Nutrition,self.Health_tracking_app]

    def Healthcare_clicking(self):
        for i in self.Healthcare_list:
            self.vertical.hover()
            self.Healthcare.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()