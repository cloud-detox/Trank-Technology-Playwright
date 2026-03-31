class CustomApp:

    def __init__(self, page):
        self.page = page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.customapp=page.locator('//strong[text()="Custom App"]')
        self.DSK=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.HRM=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.T=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company-in-india"])[1]')
        self.DATE=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.CRMUSA=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.CRM=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.ERP=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.EL=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company-in-india"])[1]')
        self.RE=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company-in-india"])[1]')



        self.Cust=[self.DSK,self.HRM,self.T,self.DATE,self.CRMUSA,self.CRM,self.ERP,self.EL,self.RE]

    def customapp_options(self):
        for i in self.Cust:
            self.vertical.hover()
            self.customapp.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()