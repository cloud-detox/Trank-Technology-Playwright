

class vertical:
    def __init__(self, page):
        self.page = page
        self.verti_var = page.locator('(//a[text()="Verticals"])[1]') #hover
        self.trading = page.locator('//strong[text()="Trading"]')
        self.ret_ecom = page.locator('//strong[text()="Retail and Ecommerce"]')
        self.healthcare = page.locator('//strong[text()="Healthcare"]')
        self.fintech = page.locator('//strong[text()="Fintech"]')
        self.custom = page.locator('//strong[text()="Custom App"]')

        #Trading
        self.st = page.locator('(//a[text()="Stock Trading"])[1]')
        self.pt =page.locator('(//a[text()="Paper Trading"])[1]')
        self.cfd = page.locator('(//a[text()="CFD Trading"])[1]')
        self.tadm = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.at = page.locator('(//a[text()="Algo Trading"])[1]')
        self.ct = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.wpt = page.locator('(//a[text()="Web Portal Trading"])[1]')

        #retail and ecommerce
        self.ewd = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.ead = page.locator('//a[text()="eCommerce App Development"]')

        #healthcare
        self.diet = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.HTA = page.locator('(//a[text()="Health tracking App"])[1]')

        #Fintech
        self.psd = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto = page.locator('(//a[text()="Crypto"])[1]')
        

        #custom
        self.desktop=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.HRM = page.locator('(//a[text()="HRM Development"])[1]')
        self.travel =page.locator('(//a[text()="Travel"])[1]')
        self.datingapp =page.locator('(//a[text()="Dating App Development"])[1]')
        self.crm_usa =page.locator('(//a[text()="CRM Development USA"])[1]')
        self.crm =page.locator('(//a[text()="CRM Development"])[1]')
        self.erp =page.locator('(//a[text()="ERP App Development"])[1]')
        self.e_larning = page.locator('(//a[text()="E-Learning"])[1]')
        self.real = page.locator('(//a[text()="Real Estate"])[1]')        

    def vert_trading_click(self):
        self.tra_list = [self.st, self.pt, self.cfd, self.tadm, self.at, self.ct, self.wpt]
        for i in self.tra_list:
            self.verti_var.hover()
            self.trading.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()


    def vert_ret_ecom_click(self):
        self.ret_list = [self.ewd, self.ead] #
        for j in self.ret_list:
            self.verti_var.hover()
            self.page.wait_for_timeout(500)
            self.ret_ecom.hover()
            self.page.wait_for_timeout(500)
            j.click(force=True)
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def vert_health_click(self):
        self.health_list = [self.diet, self.HTA]
        for k in self.health_list:
            self.verti_var.hover()
            self.healthcare.hover()
            k.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def vert_fintech_click(self):
        self.fintech_list = [self.psd, self.crypto]
        for l in self.fintech_list:
            self.verti_var.hover()
            self.fintech.hover()
            l.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def vert_custom_click(self):
        self.custom_list = [self.desktop, self.HRM, self.travel, self.datingapp, self.crm_usa, self.crm, self.erp, self.e_larning, self.real]
        for m in self.custom_list:
            self.verti_var.hover()
            self.page.wait_for_timeout(1000)
            self.custom.hover()
            self.page.wait_for_timeout(1000)
            m.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
