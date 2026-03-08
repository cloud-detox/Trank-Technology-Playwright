from conftest import page
from utils.screenShot import takeScrnsht
class homepage:
    def __init__(self, page):
        self.page=page
        self.vertical= page.locator('(//a[@href="#"])[2]')
        self.trading=page.locator('//strong[text()="Trading"]')
        self.retailing=page.locator("//strong[text()='Retail and Ecommerce']")
        self.healthcare=page.locator("//strong[text()='Healthcare']")
        self.fintech=page.locator("//strong[text()='Fintech']")
        self.customapp=page.locator("//strong[text()='Custom App']")
        Homepageoptns=[self.vertical,self.trading,self.retailing,self.healthcare,self.fintech,self.customapp]
        self.homepageopns=Homepageoptns

        #trading

        self.trading=page.locator('//strong[text()="Trading"]')
        self.stockTrad=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company-in-india"])[1]')
        self.paperTrading=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company-in-india"])[1]')
        self.customTrading=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.webPortalTrd=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.algoTrad=page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.Masscu=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        tradOptions=[self.stockTrad,self.paperTrading,self.customTrading,self.webPortalTrd,self.algoTrad,self.Masscu]
        self.tradoptns=tradOptions

        #Retail
        self.retail=page.locator("//strong[text()='Retail and Ecommerce']")
        self.ecomm=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company-in-india"])[1]')
        self.appDev=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        retailOptns=[self.ecomm,self.appDev]
        self.retailopts=retailOptns

        #HealthCare
        self.hc=page.locator("//strong[text()='Healthcare']")
        self.diet=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.healthTrackApp=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        HealthCareOptns=[self.diet,self.healthTrackApp]
        self.healthCareOptns=HealthCareOptns

        #Fintech
        self.ft= page.locator("//strong[text()='Fintech']")
        self.swDev=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company-in-india"])[1]')
        FinTechOptns=[self.swDev,self.crypto]
        self.fintechOptns=FinTechOptns


        #customapp
        self.deskApp=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.crm=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.hrm=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.erp=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.travel=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company-in-india"])[1]')
        self.elearn=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company-in-india"])[1]')
        self.dating=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.relEstate=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company-in-india"])[1]')
        self.crm=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')

        custAppOpns=[self.deskApp,self.crm,self.hrm,self.erp,self.travel,self.elearn,self.dating,self.relEstate,self.crm]
        self.customappoptns=custAppOpns

    def mouseHoverVertical(self):
        self.vertical.hover()
    
    def mouseOverTrading(self):
        self.trading.hover()
    
    def mousOverRetail(self):
        self.retail.hover()
    def mouseOverHC(self):
        self.hc.hover()
    def mouseHoverFintech(self):
        self.ft.hover()
    def mouseHoverCustApp(self):
        self.customapp.hover()
    
    
    def clickTradOptns(self):
        for i in self.tradoptns:
            self.mouseHoverVertical()
            self.mouseOverTrading()
            i.click()
            self.page.go_back()
            takeScrnsht(self.page, "Trading")
    
    def retailOptns(self):
        for i in self.retailopts:
            self.mouseHoverVertical()
            self.mousOverRetail()
            i.click()
            self.page.go_back()
            takeScrnsht(self.page, "Retail")
    
    def clickHealthCare(self):
        for i in self.healthCareOptns:
            self.mouseHoverVertical()
            self.mouseOverHC()
            i.click()
            self.page.go_back()
            takeScrnsht(self.page,"HealthCare")
    
    def clickFintech(self):
        for i in self.fintechOptns:
            self.mouseHoverVertical()
            self.mouseHoverFintech()
            i.click()
            takeScrnsht(self.page,"Fintech")
            self.page.go_back()
    
    def customApp(self):
        for i in self.customappoptns:
            self.mouseHoverVertical()
            self.mouseHoverCustApp()
            i.click()
            takeScrnsht(self.page,"Custom App")
            self.page.go_back()
    


    

        
        



        
