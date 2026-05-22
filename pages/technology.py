class technology:
    def __init__(self,page):
        self.page=page
        #technology list
        self.tech=page.locator('(//a[text()="Technologies"])[1]')
        self.ecommerce=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/ecomm-mob.png"]')
        self.mad=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/mobileapp-mob.png"]')
        self.ai=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/ai-mob.png"]')

        #ecommerce list:    
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
        self.e11=page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.e12=page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')  
        self.ecommercelist=[self.e1,self.e2,self.e3,self.e4,self.e5,self.e6,self.e7,self.e8,self.e9,self.e10,self.e11,self.e12]
    
        #mobile app development
        self.mad1=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')        
        self.mad2=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.mad3=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')  
        self.mad4=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')  
        self.mad5=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')  
        self.mad6=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')  
        self.mad7=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')  
        self.mad8=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')  
        self.madlist=[self.mad1,self.mad2,self.mad3,self.mad4,self.mad5,self.mad6,self.mad7,self.mad8]

    def mousehovertech(self):
        self.tech.hover()
        self.page.wait_for_timeout(2000)    
    def mousehoverecommerce(self):
        self.ecommerce.hover()
        self.page.wait_for_timeout(2000)
    def mousehovermad(self):
        self.mad.hover()
        self.page.wait_for_timeout(2000)
    def mousehoverai(self):
        self.ai.hover()
        self.page.wait_for_timeout(2000)  
    def ecommerce_click(self):
        for i in self.ecommercelist:
            self.mousehovertech()
            self.mousehoverecommerce()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
            self.page.wait_for_timeout(2000) 

    def mad_click(self):
        for i in self.madlist:
            self.mousehovertech()
            self.mousehovermad()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
            self.page.wait_for_timeout(2000)  

                           