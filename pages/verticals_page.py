class verticalsPage:
    def __init__(self,page):
        self.page=page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.trading=page.locator('//a[strong[text()="Trading"]]')
        self.retailecom=page.locator('//a[strong[text()="Retail and Ecommerce"]]')
        self.healthcare=page.locator('//a[strong[text()="Healthcare"]]')
        self.fintech=page.locator('//a[strong[text()="Fintech"]]')
        self.customapp=page.locator('//a[strong[text()="Custom App"]]')

        #Trading
        self.stocktrading=page.locator('(//a[text()="Stock Trading"])[1]')
        self.papertrading=page.locator('//a[text()="Paper Trading"]')
        self.cfdtrading=page.locator('(//a[text()="CFD Trading"])[1]')
        self.tadm=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.algotrading=page.locator('//a[text()="Algo Trading"]')
        self.customtrading=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.webportaltrading=page.locator('(//a[text()="Web Portal Trading"])[1]')


        #Retail and eCommerce
        self.ecomwebdev=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.ecomappdev=page.locator('//a[text()="eCommerce App Development"]')

        #Healthcare
        self.diet=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.healthtracking=page.locator('(//a[text()="Health tracking App"])[1]')

        #Fintech
        self.possoftwaredev=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto=page.locator('(//a[text()="Crypto"])[1]')

        #Custom App
        self.desktopaap=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.hrm=page.locator('(//a[text()="HRM Development"])[1]')
        self.travel=page.locator('(//a[text()="Travel"])[1]')
        self.datingapp=page.locator('(//a[text()="Dating App Development"])[1]')
        self.crmdevusa=page.locator('(//a[text()="CRM Development USA"])[1]')

    def open_verticals(self):
        self.vertical.hover()


    def verticals_hover(self):
        # self.vertical.hover()
        # self.page.wait_for_timeout(1000)
        # self.trading.hover()
        # self.page.wait_for_timeout(1000)
        # self.retailecom.hover()
        # self.page.wait_for_timeout(1000)
        # self.healthcare.hover()
        # self.page.wait_for_timeout(1000)
        # self.fintech.hover()
        # self.page.wait_for_timeout(1000)
        # self.customapp.hover()
        # self.page.wait_for_timeout(1000)
        #self.trading.hover()
        #self.stocktrading.click()
        #self.page.wait_for_timeout(1000)
        self.verticals_list=[self.trading,self.retailecom,self.healthcare,self.fintech,self.customapp]
        for i in self.verticals_list:
            self.open_verticals()
            i.hover()
            self.page.wait_for_timeout(1000)
            

    

    def verticals_trading_clicking(self):
        # First hover over Verticals to make the menu visible
        self.open_verticals()
        self.trading.hover()
        self.trading_list=[self.stocktrading,self.papertrading,self.cfdtrading,self.tadm,self.algotrading,self.customtrading,self.webportaltrading]
        for i in self.trading_list:
            self.open_verticals()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def verticals_retail_ecommerce_clicking(self):      
        self.retail_ecommerce_list=[self.ecomappdev]
        for i in self.retail_ecommerce_list:
            self.open_verticals()
            self.retailecom.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def verticals_healthcare_clicking(self):
        self.healthcare_list=[self.diet,self.healthtracking]
        for i in self.healthcare_list:
            self.open_verticals()
            self.healthcare.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def verticals_fintech_clicking(self):
        self.fintech_list=[self.possoftwaredev,self.crypto]
        for i in self.fintech_list:
            self.open_verticals()
            self.fintech.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def verticals_custom_app_clicking(self):
        self.customapp_list=[self.desktopaap,self.hrm,self.travel,self.datingapp,self.crmdevusa]
        for i in self.customapp_list:
            self.open_verticals()
            self.customapp.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    


