class technologies:
    def __init__(self,page):
        self.page=page
        self.tech=page.locator('(//a[text()="Technologies"])[1]')
        self.ecomm=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/ecomm-mob.png"]')
        self.mobileapp=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/mobileapp-mob.png"]')
        self.ai=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/ai-mob.png"]')

# E-commerce option locators
   
        self.e1=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.e2=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.e3=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.e4=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.e5=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.e6=page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.e7=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.e8=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.e9=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.e10=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.e11=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.e12=page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')

        self.ecommlist=[self.e1,self.e2,self.e3,self.e4,self.e5,self.e6,self.e7,self.e8,self.e9,self.e10,self.e11,self.e12]
    
    # Mobile app development
        self.m1=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.m2=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.m3=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.m4=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.m5=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.m6=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.m7=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.m8=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.mobileapplist=[self.m1,self.m2,self.m3,self.m4,self.m5,self.m6,self.m7,self.m8]

    # Artificial Intelligence
        self.ai=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/ai-mob.png"]')

# Mouse hover Methos
    def mousehovertechnology(self):
        self.tech.hover()

    def mousehoverecomm(self):
        self.ecomm.hover()
    
    def mousehovermobileapp(self):
        self.mobileapp.hover()
    
    def mousehoverai(self):
        self.ai.hover()

# Click Methods 
    def ecomm_click(self):
        for i in self.ecommlist:
            self.mousehovertechnology()
            self.mousehoverecomm()
            i.click()
            self.page.go_back()
            self.page.wait_for_timeout(1000)


    def mobileapp_click(self):
        for i in self.mobileapplist:
            self.mousehovertechnology()
            self.mousehovermobileapp()
            i.click()
            self.page.go_back()
            self.page.wait_for_timeout(1000)

    def ai_click(self):
        self.mousehovertechnology()
        self.mousehoverai()
        self.ai.click()
        self.page.go_back()
        self.page.wait_for_timeout(1000)
