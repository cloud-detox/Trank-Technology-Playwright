from utilities.screenShot import takeScrnsht
class verticals:
    def __init__(self, page):
        self.page = page
        self.vertical = page.locator('(//a[text()="Verticals"])[1]')
        
        self.trading = page.locator('(//strong[text()="Trading"])[1]')
        self.retail = page.locator('(//strong[text()="Retail and Ecommerce"])[1]')
        self.healthCare = page.locator('(//strong[text()="Healthcare"])[1]')
        self.fintech = page.locator('(//strong[text()="Fintech"])[1]')
        self.CusApp = page.locator('(//strong[text()="Custom App"])[1]')
        
        #Trading sub-menus
        self.stkTrd = page.locator('(//a[text()="Stock Trading"])[1]')    
        self.paperTrdng = page.locator('//a[text()="Paper Trading"]')
        self.CFD_Trdng = page.locator('(//a[text()="CFD Trading"])[1]')
        self.tadm = page.locator('(//a[contains(text(),"Development in Massachusetts")])[1]')
        self.algoTrdng = page.locator('//a[text()="Algo Trading"]')
        self.custmTrng = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.webPrtlTrdng= page.locator('(//a[text()="Web Portal Trading"])[1]')
        
        #Retail and E-commerce sub-menus
        self.eCommWebDev = page.locator('(//a[contains(., "eCommerce") and contains(., "Website Development")])[1]')
        self.eCommAppDev = page.locator('//a[text()="eCommerce App Development"]')
        
        #HealthCare sub-menus
        self.dietNutri = page.locator('(//a[contains(normalize-space(.),"Diet & Nutritions")])[1]')
        self.healthTrckngApp = page.locator('(//a[text() = "Health tracking App"])[1]') 
        
        #Fintech sub-menus
        self.posSoftwareDev = page.locator('(//a[contains(normalize-space(.), "Pos Software Development")])[1]')
        self.crypto = page.locator('(//a[text() = "Crypto"])[1]')
                  
        # Custom App sub-menus
        self.dsktpAppDev = page.locator('(//a[contains(normalize-space(.),"Desktop App Development")])[1]')
        self.hrmDev = page.locator('(//a[text()="HRM Development"])[1]')
        self.travel = page.locator('(//a[text()="Travel"])[1]')
        self.datingAppDev = page.locator('(//a[text()="Dating App Development"])[1]')
        self.crmDevUSA = page.locator('(//a[text()="CRM Development USA"])[1]')
        self.crmDev = page.locator('(//a[text()="CRM Development"])[1]')
        self.erpAppDev = page.locator('(//a[text()="ERP App Development"])[1]')
        self.eLearning = page.locator('(//a[text()="E-Learning"])[1]')
        self.realEstate = page.locator('(//a[text()="Real Estate"])[1]')          
            
    def vertical_Mouseover(self):
        self.vertical.hover()
        
    def trading_Mouseover(self):
        self.trading.hover()
        
    def retail_Mouseover(self):
        self.retail.hover()
        
    def healthCare_Mouseover(self):
        self.healthCare.hover()
        
    def fintech_Mouseover(self):
        self.fintech.hover()
        
    def customApp_Mouseover(self):
        self.CusApp.hover()
        
    def tradingSubMenu_Click(self):
        self.lstVTrd = [self.stkTrd, self.paperTrdng, self.CFD_Trdng, self.tadm, self.algoTrdng, self.custmTrng, self.webPrtlTrdng]
        for i in self.lstVTrd:
            self.vertical_Mouseover()
            self.trading_Mouseover()
            i.click()
            self.page.go_back()
            takeScrnsht(self.page, "VerticalsSubmenu")
        print(" ****************** Trading completed **********************************")
            
    def retailSubMenu_Click(self):
        self.lstVRetail = [self.eCommWebDev, self.eCommAppDev]
        for i in self.lstVRetail:
            self.vertical_Mouseover()
            self.retail_Mouseover()
            i.click()
            self.page.go_back()
            takeScrnsht(self.page, "VerticalsSubmenu")
        print(" ****************** Retail and e-commerce completed **********************************")
            
    def HealthCareSubMenu_Click(self):
        self.lstVHealth = [self.dietNutri, self.healthTrckngApp]
        for i in self.lstVHealth:
            self.vertical_Mouseover()
            self.healthCare_Mouseover()
            i.click()
            self.page.go_back()
            takeScrnsht(self.page, "VerticalsSubmenu")
        print(" ****************** Health care completed **********************************")    
            
    def fintechSubMenu_Click(self):
        self.listVFintech = [self.posSoftwareDev, self.crypto]      
        for i in self.listVFintech:
            self.vertical_Mouseover()
            self.fintech_Mouseover()
            i.click()
            self.page.go_back()
            takeScrnsht(self.page, "VerticalsSubmenu")
        print(" ****************** FinTech completed **********************************")
            
    def customAppSubMenu_Click(self):
        self.__lstCustomAppSubs = [self.dsktpAppDev, self.hrmDev, self.travel, self.datingAppDev, self.crmDevUSA, self.crmDev, self.erpAppDev, self.eLearning, self.realEstate]
        for i in self.__lstCustomAppSubs:
            self.vertical_Mouseover()
            self.customApp_Mouseover()
            i.click()
            self.page.go_back()
            takeScrnsht(self.page, "VerticalsSubmenu")
        print(" ****************** Custom App completed **********************************")            
                                
        