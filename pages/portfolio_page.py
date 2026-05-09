class PortfolioPage:
    def __init__(self, page):
        self.page = page
        # portfolio main menu
        self.portfolio = page.locator('//a[@href="https://www.tranktechnologies.com/portfolio"]')
        #sub menu
        self.icsHomework_view_more=page.locator('//a[@href="https://www.icshomework.in/"]')
        self.wingspharma_view_more=page.locator('//a[@href="https://www.wingspharma.com/"]')
        self.arenaAnimation_view_more=page.locator('//a[@href="https://arenasonipat.com/"]')
        self.home360_view_more=page.locator('//a[@href="https://home360stores.com/"]')
        self.clubMeeting_view_more=page.locator('(//a[text()="View More"])[5]')
        self.cordscable_view_more=page.locator('//a[@href="https://cordscable.tranktechnologies.com/"]')

    def open_portfolio(self):
        
        #self.page.wait_for_timeout(1000)  
        self.portfolio_list=[self.icsHomework_view_more,self.wingspharma_view_more,self.arenaAnimation_view_more,self.home360_view_more,self.clubMeeting_view_more,self.cordscable_view_more]
        for i in self.portfolio_list:
            self.portfolio.click()
            #self.page.wait_for_timeout(1000)
            #i.click()
            i.hover()
            #self.page.wait_for_timeout(1000)
            self.page.go_back()


        


        

