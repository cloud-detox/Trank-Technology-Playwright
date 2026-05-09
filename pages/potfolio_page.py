class Portfolio:
    def __init__(self,page):
        self.page = page
        self.portfolio = page.locator('//a[text()= "Portfolio"]')
        #submenu of portfolio 
        self.icshomework= page.locator('//a[@href = "https://www.icshomework.in/"]')
        self.arena = page.locator('//a[@href="https://arenasonipat.com/"]')
        self.home360 = page.locator('//a[@href="https://home360stores.com/"]')
        self.cords = page.locator('//a[@href="https://cordscable.tranktechnologies.com/"]')
        self.wings = page.locator('//a[@href="https://www.wingspharma.com/"]')
        #self.club = page.locator('(//a[text()="View More"])[5]')


    def portfoliomethod(self):
        self.portfolio_list = [self.icshomework,self.arena, self.home360, self.cords,self.wings]
        for i in self.portfolio_list:
            self.portfolio.click()
            i.scroll_into_view_if_needed()        
            with self.page.context.expect_page() as new_page_info:
                i.click()
            new_page = new_page_info.value
            new_page.wait_for_load_state("load")  
            new_page.close()  


