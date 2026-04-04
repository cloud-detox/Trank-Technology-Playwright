from conftest import page
from pages.vertical import vertical

class customapp:
    def __init__(self,page):
        self.page =page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.customapp=page.locator('//strong[text()="Custom App"]')
        self.page.wait_for_timeout(5000)

        self.desktop=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.hrm=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.travel=page.locator('(//a[text()="Travel"])[1]')
        self.dating=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.crmUSA=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.crmdev=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.erp=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.elearn=page.locator('(//a[text()="E-Learning"])[1]')
        self.restate=page.locator('(//a[text()="Real Estate"])[1]')
        self.custom_list=[self.desktop,self.hrm,self.travel,self.dating,self.crmUSA,self.crmdev,self.erp,self.elearn,self.restate]

    def customapp_clicking(self):
        for i in self.custom_list:
            self.vertical.hover()
            self.customapp.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()