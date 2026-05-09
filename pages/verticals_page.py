from conftest import page


class VerticalsPage:
    def __init__(self, page):
        self.page = page

        self.vertical = page.locator('(//a[text()="Verticals"])[1]')
        self.trading = page.locator('//strong[text()="Trading"]')
        self.retail_ecommerce = page.locator('//strong[text()="Retail and Ecommerce"]')
        self.healthcare = page.locator('//strong[text()="Healthcare"]')
        self.fintech = page.locator('//strong[text()="Fintech"]')
        self.customapp = page.locator('//strong[text()="Custom App"]')

        #trading
        self.stock_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.paper_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.cfd_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.trading_app_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.algo_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.custom_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.web_app_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')

        #retail_ecommerce
        self.ecommerce_website_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.ecommerce_app_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

        #healthcare
        self.diet_and_nutritions = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.health_tracking_app = page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

        #fintech
        self.pos_soft_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

        #customapp
        self.desktop_app_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.hrm_app_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.travel = page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.dating_app_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.crm_dev_usa = page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.crm_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.erp_app_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.e_learning = page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.real_estate = page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')

    def vertical_hover(self):
        self.vertical.hover()
        self.page.wait_for_timeout(2000)

    def trading_hover(self):
        self.trading_list = [self.stock_trading, self.paper_trading, self.cfd_trading, self.trading_app_dev, self.algo_trading, self.custom_trading, self.web_app_trading]
        for i in self.trading_list:
            self.vertical.click()
            self.trading.click()
            self.page.wait_for_timeout(2000)
            i.click(force=True)
            self.page.wait_for_timeout(2000)
            self.page.go_back()

    def retail_ecommerce_hover(self):
        self.retail_ecommerce_list = [self.ecommerce_website_dev, self.ecommerce_app_dev]
        for j in self.retail_ecommerce_list:
            self.vertical.hover()
            self.retail_ecommerce.hover()
            self.page.wait_for_timeout(2000)
            j.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()


    def healthcare_hover(self):
        self.healthcare_list = [self.diet_and_nutritions, self.health_tracking_app]
        for k in self.healthcare_list:
            self.vertical.hover()
            self.healthcare.hover()
            k.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()


    def fintech_hover(self):
        self.fintech_list = [self.pos_soft_dev, self.crypto]
        for l in self.fintech_list:
            self.vertical.hover()
            self.fintech.hover()
            self.page.wait_for_timeout(2000)
            l.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
    
    def customapp_hover(self):
        self.customapp_list = [self.desktop_app_dev, self.hrm_app_dev, self.travel, self.dating_app_dev, self.crm_dev_usa, self.crm_dev, self.erp_app_dev, self.e_learning, self.real_estate]
        for m in self.customapp_list:
            self.vertical.hover()
            self.customapp.hover()
            self.page.wait_for_timeout(2000)
            m.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
