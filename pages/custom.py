from pages.vertical import vertical


class CustomAppPage(vertical):

    def __init__(self, page):
        self.page=page
        super().__init__(page)

        self.custom=page.locator('//strong[text()="Custom App"]')
        self.DAD=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.HRMD=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.T=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company-in-india"])[1]')
        self.DAAD=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.CRMD=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.ERPAD=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.EL=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company-in-india"])[1]')
        self.RE=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company-in-india"])[1]')

        self.CA = [self.DAD, self.HRMD, self.T, self.DAAD, self.CRMD, self.ERPAD, self.EL, self.RE]

    def customoption_clicking(self):
          
        for i in self.CA:
            self.vertical_hover()
            self.custom_hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()  
