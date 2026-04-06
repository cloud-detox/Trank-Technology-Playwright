from conftest import page
from pages.verticalpage import vertical


class CustomAppPage:
        
        def __init__(self, page):
                self.page = page
                self.vertical = page.locator("(//a[text()='Verticals'])[1]")
                self.customapp = page.locator ('//strong[text()="Custom App"]') 

                self.op1 = page.locator ('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
                self.op2 = page.locator ('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
                self.op3 = page.locator ('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
                self.op4 = page.locator ('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
                self.op5 = page.locator ('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company-in-india"])[1]')
                self.op6 = page.locator ('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company-in-india"])[1]')
                self.op7 = page.locator ('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
                self.op8 = page.locator ('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company-in-india"])[1]')
                self.op9 = page.locator ('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')

                self.customapp_locators=[self.op1,self.op2,self.op3,self.op4,self.op5,self.op6,self.op7,self.op8,self.op9]  

        def customapp_clicking(self):
                for i in self.customapp_locators:
                        self.vertical.hover()
                        self.customapp.hover()
                        i.click()
                        self.page.wait_for_timeout(2000)
                        self.page.go_back()
