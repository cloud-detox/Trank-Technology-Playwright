class Healthcare:

    def __init__(self, page):
        self.page = page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.healthcare=page.locator('//strong[text()="Healthcare"]')
        self.DN=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.HA=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

        self.Health=[self.DN,self.HA] 

    def healthcare_options(self):
        for i in self.Health:
            self.vertical.hover()
            self.healthcare.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()