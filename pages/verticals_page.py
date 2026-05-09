class VerticalsPage:
    def __init__(self,page):
        self.page = page
        self.verticals = page.locator("(//a[text()='Verticals'])[1]")
        self.trading = page.locator("(//strong[text()='Trading'])[1]")
        self.retail = page.locator("//strong[text()='Retail and Ecommerce']")
        self.health = page.locator("//strong[text()='Healthcare']")
        self.fintech = page.locator("//strong[text()='Fintech']")
        self.custom = page.locator("//strong[text()='Custom App']")
        #trading
        self.stock = page.locator ('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.algo = page.locator ('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.paper = page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.custra = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.cfd = page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.tradappdev = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.webapp = page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        #retail_ecommerce
        self.ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.ecomapp = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
       #healthcare
        self.dietnut = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.healthtrack = page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
       #fintech
        self.psdev = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.cry = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
        #customapp
        self.desktop_app_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.hrm_app_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.travel = page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.dating_app_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.crm_dev_usa = page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.crm_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.erp_app_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.e_learning = page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.real_estate = page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')


    def verticalhover(self):
        self.verticals.hover()
        self.page.wait_for_timeout(1000)

#     def verticalhover(self):
#         self.verticals.hover()
#         self.page.wait_for_timeout(2000)   
#         self.trading.hover() 
#         self.page.wait_for_timeout(2000)   
#         self.retail.hover() 
#         self.page.wait_for_timeout(2000)
#         self.health.hover()
#         self.page.wait_for_timeout(2000) 
#         self.fintech.hover()
#         self.page.wait_for_timeout(2000)  
#         self.custom.hover() 
#         self.page.wait_for_timeout(2000)

# ############################################################
#     # second option create seprate method.
#     def tradinghover(self):
#         self.trading.hover()
#         self.page.wait_for_timeout(2000)
        
#     def retailhover(self):
#         self.retail.hover()
#         self.page.wait_for_timeout(2000) 

#     def healthhover(self):
#         self.health.hover()
#         self.page.wait_for_timeout(2000)

##########################################################
    # third Method with listing.
    # def verticalhoverlist(self):
    #     list_vertical = [self.trading,self.retail,self.health,self.fintech,self.custom]
    #     for j in list_vertical:
    #         self.verticals.hover()
    #         j.click()
    #         self.page.wait_for_timeout(1000)
    #         self.page.go_back()         

############ Child Xpath Get #########################
    def tradinghoverlist(self):
        list_trading = [self.stock,self.algo,self.paper,self.custra,self.cfd,self.tradappdev,self.webapp]
        for i in list_trading:
            self.verticals.hover()
            self.trading.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()         
    
    def retailhoverlist(self):
        list_retail = [self.ecom,self.ecomapp]
        for j in list_retail:
            self.verticals.hover()
            self.retail.hover()
            j.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def healthcarehoverlist(self):
        list_health = [self.dietnut,self.healthtrack]
        for k in list_health:
            self.verticals.hover()
            self.health.hover()
            k.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()                

    def fintechhoverlist(self):
        list_fintech = [self.psdev, self.cry]
        for i in list_fintech:
            self.verticals.hover()
            self.fintech.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def customapphoverlist(self):
        self.customapp_list = [self.desktop_app_dev, self.hrm_app_dev, self.travel, self.dating_app_dev, self.crm_dev_usa, self.crm_dev, self.erp_app_dev, self.e_learning, self.real_estate]
        for m in self.customapp_list:
            self.verticals.hover()
            self.custom.hover()
            m.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()











