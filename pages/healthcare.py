from pages.vertical import vertical


class HealthCarePage(vertical):

    def __init__(self, page):
        self.page=page
        super().__init__(page)
        self.healthcare=page.locator('//strong[text()="Healthcare"]')
        self.DN=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.HTA=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

        self.HC=[self.DN, self.HTA]

    def healthcareoption_clicking(self):
          
        for i in self.HC:
            self.vertical_hover()
            self.healthcare_hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()  