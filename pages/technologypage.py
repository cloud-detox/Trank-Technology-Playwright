


class technology:

    def __init__(self, page):
        self.page = page
        self.technology = page.locator('(//a[text()="Technologies"])[1]')
        self.ecom_dev = page.locator('//strong[text()="eCommerce Development"]')
        self.mobile= page.locator('//strong[text()="Mobile App Development"]')
        self.AI = page.locator('//strong[text()="Artificial Intelligence"]')
        
        #ecommerce_dev
        self.m_dev = page.locator('//a[text()="Magento Development"]')
        self.code_dev = page.locator('(//a[text()="Codeigniter Development"])[1]')
        self.big_comm = page.locator('(//a[text()="Big Commerce"])[1]')
        self.cs_dev = page.locator('(//a[text()="CS-Cart Development"])[1]')
        self.nop_comm = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.lar_dev = page.locator('(//a[text()="Laravel Development"])[1]')
        self.dru_dev = page.locator('(//a[text()="Drupal Development"])[1]')
        self.joo_dev = page.locator('(//a[text()="Joomla Development"])[1]')
        self.open_dev = page.locator('(//a[text()="Opencart Development"])[1]')
        self.wordp_dev = page.locator('(//a[text()="WordPress Development"])[1]')
        self.shop_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.nodejsdev = page.locator('(//a[text()="Node JS Development"])[1]')
        self.woo_comm = page.locator('(//a[text()="Woo Commerce"])[1]')
        self.pre_dev = page.locator('(//a[text()="Prestashop Development"])[1]')
        self.wixdev = page.locator('(//a[text()="Wix Development"])[1]')
        self.reactjsdev = page.locator('(//a[text()="React JS Development"])[1]')    

        #mobile app dev
        self.react_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.xama_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.flut_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.swift_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.enter_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.kotlin_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.ionic_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.appointment_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

    # def technologies_hover(self):
    #     self.technology.hover()
    #     self.page.wait_for_timeout(2000)

    def ecommercedevelopment_hover(self):
            self.ecom_dev_list = [self.m_dev,self.code_dev,self.big_comm,self.cs_dev,self.nop_comm,self.lar_dev,self.dru_dev,self.joo_dev,self.open_dev,self.wordp_dev,self.shop_dev,self.nodejsdev,self.woo_comm,self.pre_dev,self.wixdev,self.reactjsdev]
            for i in self.ecom_dev_list:
                 self.technology.hover()
                 self.page.wait_for_timeout(500)
                 self.ecom_dev.hover()
                 self.page.wait_for_timeout(500)
                 i.click(force=True)
                 self.page.wait_for_timeout(2000)
                 self.page.go_back()


    def mobile_hover(self):
        self.mobile_list = [self.react_dev,self.xama_dev,self.flut_dev,self.swift_dev,self.enter_dev,self.kotlin_dev,self.ionic_dev,self.appointment_dev]
        for j in self.mobile_list:
             self.technology.hover()
             self.mobile.hover()
             j.click()
             self.page.wait_for_timeout(2000)
             self.page.go_back()

    def artificial_intelligence_hover(self):
        self.technology.hover()
        self.AI.hover()
    