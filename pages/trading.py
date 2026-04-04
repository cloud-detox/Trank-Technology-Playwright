from conftest import page #conftest is used where hover is there
from pages.vertical import vertical

class trading:
    def __init__(self,page):
        self.page =page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.trading=page.locator('//strong[text()="Trading"]')
        self.page.wait_for_timeout(5000) # self is used within the function.when u are using func use self.
       
#verticle-trading
        self.stocktrading=page.locator('(//a[text()="Stock Trading"])[1]')
        self.papaerT=page.locator('(//a[text()="Paper Trading"])[1]')
        self.CFD=page.locator('(//a[text()="CFD Trading"])[1]')
        self.Tapp=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.aldo=page.locator('(//a[text()="Algo Trading"])[1]')
        self.customp=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.WebT=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.stock_list=[self.stocktrading,self.papaerT,self.CFD,self.Tapp,self.aldo,self.customp,self.WebT]
        
    def tradinglist_clicking(self):
        for i in self.stock_list:
            self.vertical.hover()
            self.trading.hover()
            #self.stocktrading.hover()
            #self.page.locator.wait_for(state="visible", timeout=30000)
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()