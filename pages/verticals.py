class vertical:
    def __init__(self,page):
        self.page=page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.trade=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/trade-mob.png"]')
        self.reatail=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.health=page.locator('(//a[@href="https://www.tranktechnologies.com/healthcare-mobile-app-development-company"])[1]')
        self.fintech=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/fintech-mob.png"]')
        self.customapp=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/custom-mob.png"]')

        # trading Options
        self.t1=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.t2=page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.t3=page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.t4=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.t5=page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.t6=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.t7=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')

        self.tradinglist=[self.t1,self.t2,self.t3,self.t4,self.t5,self.t6,self.t7]
       

       
        # Retail and E-commerce
        self.r1=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.r2=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

        self.reatilandecommlist=[self.r1,self.r2]
    
    # Health care
        self.h1=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.h2=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.healthcarelist=[self.h1,self.h2]

    # Fintech 

        self.f1=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.f2=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

        self.fintechlist=[self.f1,self.f2]
    # Custom App
        self.c1=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.c2=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.c3=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.c4=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.c5=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.c6=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.c7=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.c8=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.c9=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')

        self.customapplist=[self.c1,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8,self.c9]

    
    def mousehoververtical(self):
        self.vertical.hover()
        

    def mousehovertrading(self):
        self.trade.hover()
      

    def mousehoverretail(self):
        self.reatail.hover()
        

    def mousehoverhealth(self):
        self.health.hover()
        
    
    def mousehoverfintech(self):
        self.fintech.hover()


    def mousehovercustomapp(self):
        self.customapp.hover()
       


    def trading_list_click(self):
        for i in self.tradinglist:
            self.mousehoververtical()
            self.mousehovertrading()
            i.click()
            self.page.go_back()
            self.page.wait_for_timeout(1000)
            
    def reatil_ecomm_click(self):
        for i in self.reatilandecommlist:
            self.mousehoververtical()
            self.mousehoverretail()
            i.click()
            self.page.go_back()
            self.page.wait_for_timeout(1000)

    def healthcare_click(self):
        for i in self.healthcarelist:
            self.mousehoververtical()
            self.mousehoverhealth()
            i.click()
            self.page.go_back()
            self.page.wait_for_timeout(1000)

    def fintech_click(self):
        for i in self.fintechlist:
            self.mousehoververtical()
            self.mousehoverfintech()
            i.click()
            self.page.go_back()
            self.page.wait_for_timeout(1000)
    
    def customapp_click(self):
        for i in self.customapplist:
            self.mousehoververtical()
            self.mousehovercustomapp()
            i.click()
            self.page.go_back()
            self.page.wait_for_timeout(1000)
