from conftest import page
from pages.verticalpage import vertical


class HealthcarePage:
        
        def __init__(self, page):
                self.page = page
                self.vertical = page.locator("(//a[text()='Verticals'])[1]")
                self.healthcare = page.locator ('//strong[text()="Healthcare"]')

                self.dnn = page.locator ('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
                self.healthtrack = page.locator ('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

                self.healthcare_locators=[self.dnn ,self.healthtrack]

        def healthcare_clicking(self):
                for i in self.healthcare_locators:
                        self.vertical.hover()
                        self.healthcare.hover()
                        i.click()
                        self.page.wait_for_timeout(2000)
                        self.page.go_back()