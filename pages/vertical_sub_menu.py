
from pages.verticalpage import VerticalPage


class vertical_sub_menu:

    def __init__(self, page):
        self.page = page
        self.vertical = VerticalPage(page)

        self.trading_locators=[
        page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company-in-india"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')]

        self.retail_locators=[
        page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company-in-india"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]') ]

        self.healthcare_locators=[
        page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')]

        self.fintech_locators=[ 
        page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company-in-india"])[1]')]

        self.customerapp_locators=[
        page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company-in-india"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company-in-india"])[1]')]

    def click_options(self,category_method,locators):
        for option in locators:
            self.vertical.hover_vertical()
            category_method()
            option.click()

            self.page.wait_for_load_state("load")
            self.page.go_back()

    def tradingoption_clicking(self):
        self.click_options(self.vertical.hover_trading,self.trading_locators)

    def retail_clicking(self):
        self.click_options(self.vertical.hover_retail,self.retail_locators)

    def healthcare_clicking(self):
        self.click_options(self.vertical.hover_healthcare, self.healthcare_locators)

    def fintech_clicking(self):
        self.click_options(self.vertical.hover_fintech, self.fintech_locators)

    def customerapp_clicking(self):
        self.click_options(self.vertical.hover_customerapp,self.customerapp_locators)
   
   
    # def tradingoption_clicking(self):
    #     for i in self.trading_locators:
    #         self.vertical.hover_vertical()
    #         self.vertical.hover_trading()
    #         i.click()
    #         self.page.wait_for_load_state("load")
    #         self.page.go_back()

    # def retail_clicking(self):
    #     for i in self.retail_locators:
    #         self.vertical.hover_vertical()
    #         self.vertical.hover_retail()
    #         i.click()
    #         self.page.wait_for_load_state("load")
    #         self.page.go_back()


