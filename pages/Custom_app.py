from conftest import page
from pages.verticalpage import vertical

class Custom_app:
    def __init__(self,page):
        self.page=page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.Custom_app=page.locator('(//a[@href="#"])[4]')

        self.Desk_app=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.CRM=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.HRM=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.ERP_App=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.Travel=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company-in-india"])[1]')
        self.E_Learning=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company-in-india"])[1]')
        self.Dating_app=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.Real_Estate=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company-in-india"])[1]')
        self.CRM_USA=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.Custom_app_list=[self.Desk_app,self.CRM,self.HRM,self.ERP_App,self.Travel,self.E_Learning,self.Dating_app,self.Real_Estate,self.CRM_USA]

    def Custom_app_clicking(self):
        for i in self.Custom_app_list:
            self.vertical.hover()
            self.Custom_app.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()
        
        