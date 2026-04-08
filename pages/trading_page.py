from config import URL

class TradingPage:
    
    def __init__(self, page):
        self.page = page 
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.trading=page.locator("//strong[text()='Trading']")
        self.ST=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company-in-india"])[1]')
        self.AT=page.locator('(//a[text()="Algo Trading"])[1]')
        self.PT=page.locator('(//a[text()="Paper Trading"])[1]')
        self.CustT=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.CFDT=page.locator('(//a[text()="CFD Trading"])[1]')
        self.Webport=page.locator('(//a[text()="Web Portal Trading"])[1]')
        self.STDM=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        
        self.list=[self.ST,self.AT,self.PT,self.CustT,self.CFDT,self.Webport,self.STDM]    

    
    def trading_options(self):
        for i in self.list:
            self.vertical.hover()
            self.page.wait_for_timeout(2000)  # Wait for Trading submenu to appear
            i.click(force=True)
            self.page.wait_for_timeout(3000)
            self.page.goto(URL)