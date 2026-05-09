class verticalsPage:
    def __init__(self, page):
        self.page = page
        #vertical main menu
        self.vertical = page.locator('(//a[text()="Verticals"])[1]')
        #sub menus vertical
        self.trading=page.locator('//li[@data-id="trading"]')
        self.retail=page.locator('//li[@data-id="retailEcommerce"]')
        self.healthcare=page.locator('//li[@data-id="healthcare"]')
        self.fintech=page.locator('//li[@data-id="fintech"]')
        self.customapp=page.locator('//li[@data-id="customApp"]')
     # Trading submenus 
        self.stock_trading = page.locator('(//a[text()="Stock Trading"])[1]')
        self.paper_trading = page.locator('(//a[text()="Paper Trading"])[1]')
        self.cfd_trading = page.locator('(//a[text()="CFD Trading"])[1]')
        self.trading_mass = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.algo_trading = page.locator('(//a[text()="Algo Trading"])[1]')
        self.custom_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.web_portal = page.locator('(//a[text()="Web Portal Trading"])[1]')
    # retail &Ecom sub menu
        self.ecomWebDev=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.ecomAppDev=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
    #healthcare sub menu  
        self.dietandNeutri=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.healthTrackingapp=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
    #finetech sub menu
        self.posSoftDev=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
    #customApp submenu
        self.desktopAppDev=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.hrmDev=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.travel=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.datingAppDev=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.crmDevUsa=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.crmdev=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.erpAppDev=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.elearing=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.realestate=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        

    def open_verticals(self):
        self.vertical.hover()
        #self.page.wait_for_timeout(2000)


    def trading_hover(self):
        self.open_verticals()
        self.trading.hover()
        #self.page.wait_for_timeout(1000)
        
    def retails_hover(self):
        self.open_verticals()
        self.retail.hover()
        #self.page.wait_for_timeout(1000)



    def healthcare_hover(self):
        self.open_verticals()
        self.healthcare.hover()
        #self.page.wait_for_timeout(1000)
        


    def fintech_hover(self):
        self.open_verticals()
        self.fintech.hover()
        #self.page.wait_for_timeout(2000)
        



    def customapp_hover(self):
        self.open_verticals()
        self.customapp.hover()
        #self.page.wait_for_timeout(2000)
        

    def verticals_trading_clicking(self):
        self.trading_hover()
        self.trade_list=[self.stock_trading,self.paper_trading,self.cfd_trading,self.trading_mass,self.algo_trading,self.custom_trading,self.web_portal]
        
        for i in self.trade_list:
            self.open_verticals()
            i.click()

            #self.page.wait_for_timeout(1000)
            self.page.go_back()
            
    def vertical_retail_clicking(self):
        
        self.retail_list=[self.ecomAppDev]
        for r in self.retail_list:
            self.retails_hover()
            r.click()
            #self.page.wait_for_timeout(1000)
            self.page.go_back()
    def vertical_healthcare_clickig(self):
        
        self.healthcare_list=[self.dietandNeutri,self.healthTrackingapp]
        for h in self.healthcare_list:
            self.healthcare_hover()
            h.click()
            #self.page.wait_for_timeout(1000)
            self.page.go_back()

    def vertical_fintech_clicking(self):
        self.fintech_list=[self.posSoftDev,self.crypto]
        for f in self.fintech_list:
            self.fintech_hover()
            f.click()
            #self.page.wait_for_timeout(1000)
            self.page.go_back()

    def vertical_customapp_clicking(self):
        self.customapp_list=[self.desktopAppDev,self.hrmDev,self.travel,self.datingAppDev,self.crmDevUsa,self.crmdev,self.erpAppDev,self.elearing,self.realestate]
        for c in self.customapp_list:
            self.customapp_hover()
            c.click()
            #self.page.wait_for_timeout(1000)
            self.page.go_back()




       

            

