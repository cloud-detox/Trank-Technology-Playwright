from conftest import page
from pages.verticalpage import vertical


class trading:

    def __init__(self,page):
        self.page=page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.Trading=page.locator('(//a[@href="#"])[3]')

        self.Stock=page.locator('(//a[text()="Stock Trading"])[1]')
        self.Paper=page.locator('(//a[text()="Paper Trading"])[1]')
        self.Algo=page.locator('(//a[text()="Algo Trading"])[1]')
        self.CFD=page.locator('(//a[text()="CFD Trading"])[1]')
        self.Custom=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.Web_portal=page.locator('(//a[text()="Web Portal Trading"])[1]')
        self.Trading_app=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.Trading_list=[self.Stock,self.Paper,self.Algo,self.CFD,self.Custom,self.Web_portal,self.Trading_app]

    
    def tradinglist_clicking(self):
        for i in self.Trading_list:
            self.vertical.hover()
            self.Trading.hover()
            i.click()
            self.page.go_back()
            
