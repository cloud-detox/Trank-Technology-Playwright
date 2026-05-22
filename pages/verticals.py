class vertical:
    def __init__(self,page):
        self.page=page
        #vertical list
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.trading=page.locator('//strong[text()="Trading"]')
        self.Retail=page.locator('//strong[text()="Retail and Ecommerce"]')
        self.healthcare=page.locator('//strong[text()="Healthcare"]')
        self.fintech=page.locator('//strong[text()="Fintech"]')
        self.customap=page.locator('//strong[text()="Custom App"]')
        #trading list
        self.stockTR=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.paperTR=page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.cfdTR=page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.appdevTR=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.algoTR=page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.customTR=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.webportalTR=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')

        self.tradinglist=[self.stockTR,self.paperTR,self.cfdTR,self.appdevTR,self.algoTR,self.customTR,self.webportalTR]  
    
    #retail and Ecommerce list
        self.Retail1=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]') #not working 
        self.Retail2=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.retaillist=[self.Retail1,self.Retail2]

    #healthcare list
        self.healthcare1=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.healthcare2=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.healthlist=[self.healthcare1,self.healthcare2]    

    #fintech list
        self.fintech1=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.fintech2=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
        self.fintechlist=[self.fintech1,self.fintech2]

    #custom app list:
        self.customap1=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')  
        self.customap2=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.customap3=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.customap4=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.customap5=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.customap6=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.customap7=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.customap8=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]') 
        self.customap9=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')    
        self.customaplist=[self.customap1,self.customap2,self.customap3,self.customap4,self.customap5,self.customap6,self.customap7,self.customap8,self.customap9]    

    def mousehoververtical(self):
        self.vertical.hover()
        self.page.wait_for_timeout(2000)
    def mousehovertrading(self):    
        self.trading.hover()
        self.page.wait_for_timeout(2000)
    def mousehoverretail(self):    
        self.Retail.hover()
        self.page.wait_for_timeout(2000)
    def mousehoverhealthcare(self):
        self.healthcare.hover()
        self.page.wait_for_timeout(2000)
    def mousehoverfintech(self):
        self.fintech.hover()  
        self.page.wait_for_timeout(2000)
    def mousehovercustomap(self):
        self.customap.hover()
        self.page.wait_for_timeout(2000) 

    def trading_list_click(self):
        for i in self.tradinglist:
            self.mousehoververtical()
            self.mousehovertrading() 
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
            self.page.wait_for_timeout(1000)  


    def retailEcommlist_click(self):
        for i in  self.retaillist:
            self.mousehoververtical()
            self.mousehoverretail()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
            self.page.wait_for_timeout(2000)    

    def healthlist_click(self):
        for i in self.healthlist:
            self.mousehoververtical()
            self.mousehoverhealthcare()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
            self.page.wait_for_timeout(2000)          

    def fintech_click(self):
        for i in self.fintechlist:
            self.mousehoververtical()
            self.mousehoverfintech()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
            self.page.wait_for_timeout(2000)

    def customap_click(self):
        for i in self.customaplist:
            self.mousehoververtical()
            self.mousehovercustomap()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
            self.page.wait_for_timeout(2000)       
