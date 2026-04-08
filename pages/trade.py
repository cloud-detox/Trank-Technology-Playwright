from conftest import page
from pages.vertical import vertical


class TradingPage(vertical):

    def __init__(self, page):
        super().__init__(page)
        self.page=page
        
        self.trade=page.locator('//strong[text()="Trading"]')
        self.ST=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company-in-india"])[1]')
        self.PT=page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.CFD=page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.TADM=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.AT=page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.CT=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.WPT=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')

        self.locators = [self.ST,self.PT,self.CFD,self.TADM,self.AT,self.CT,self.WPT]
        
        
    def tradingoption_clicking(self):
          
        for i in self.locators:
            self.vertical_hover()
            self.trade_hover()
            i.click()
            self.page.wait_for_timeout(2500)
            self.page.go_back()


