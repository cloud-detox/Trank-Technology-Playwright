class TechnologiesPage:
    def __init__(self, page):
        self.page=page
        #techologies main menu
        self.technologies=page.locator('(//a[text()="Technologies"])[1]')
        #sub menu techologiespage
        self.ecommDev=page.locator('//strong[text()="eCommerce Development"]')
        self.mobileAppDev=page.locator('(//img[@alt="mobile app"])[1]')
        self.artificialintel=page.locator('//strong[text()="Artificial Intelligence"]')
        #sumenu  ecommdevelopmet
        self.magentodev=page.locator('//a[text()="Magento Development"]')
        self.codeginiterDev=page.locator('(//a[text()="Codeigniter Development"])[1]')
        self.bigcommerce=page.locator('(//a[text()="Big Commerce"])[1]')
        self.cscardDev=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.nopcommerce=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.laravelDev=page.locator('(//a[text()="Laravel Development"])[1]')
        self.drupalDev=page.locator('(//a[text()="Drupal Development"])[1]')
        self.joomlaDev=page.locator('(//a[text()="Joomla Development"])[1]')
        self.expressjsDev=page.locator('(//a[text()="Express JS Development"])[1]')
        self.opencardDev=page.locator('(//a[text()="Opencart Development"])[1]')
        self.wordpressDev=page.locator('(//a[text()="WordPress Development"])[1]')
        self.shopifyDev=page.locator('(//a[text()="Shopify Development"])[1]')
        self.nodejsDev=page.locator('(//a[text()="Node JS Development"])[1]')
        self.woocommerce=page.locator('(//a[text()="Woo Commerce"])[1]')
        self.prestashopdev=page.locator('(//a[text()="Prestashop Development"])[1]')
        self.wixdev=page.locator('(//a[text()="Wix Development"])[1]')
        self.reactjsdev=page.locator('(//a[text()="React JS Development"])[1]')
        #submenu mobileAPP development
        self.reactNativeappDev=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.xamarinMobAppDev=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.flutterMobAppDev=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.swiftAppDev=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.enterpriseAppDev=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.kotlinMobAppDev=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.ionicAppDev=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.appointmentBookingDev=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

    def open_technologies(self):
        self.technologies.hover()
        #self.page.wait_for_timeout(2000)

    def ecomm_dev_hover(self):
        self.open_technologies()
        self.ecommDev.hover()
        #self.page.wait_for_timeout(2000)
        
        
        

    def mobile_app_hover(self):
        self.open_technologies()
        self.mobileAppDev.hover()
        #self.page.wait_for_timeout(2000)
        
        
        
    def artificialintel_hover(self):
        self.open_technologies()
        self.artificialintel.hover()
        #self.page.wait_for_timeout(1000)

    def ecom_dev_clickig(self):
        self.ecommDev_list=[self.magentodev,self.codeginiterDev,self.bigcommerce,self.cscardDev,self.nopcommerce,self.laravelDev,self.drupalDev,self.joomlaDev,self.expressjsDev,self.opencardDev,self.wordpressDev,self.shopifyDev,self.nodejsDev,self.woocommerce,self.prestashopdev,self.wixdev,self.reactjsdev]
        for i in self.ecommDev_list:
            self.ecomm_dev_hover()
            i.click()
            #self.page.wait_for_timeout(1000)
            self.page.go_back()
    def mobileapp_clicking(self):
        self.mobileApp_list=[self.reactNativeappDev,self.xamarinMobAppDev,self.flutterMobAppDev,self.swiftAppDev,self.enterpriseAppDev,self.kotlinMobAppDev,self.ionicAppDev,self.appointmentBookingDev]
        for m in self.mobileApp_list:
            self.mobile_app_hover()
            m.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
    def artificialintel_clicking(self):
        self.open_technologies()
        self.artificialintel.click()
        self.page.go_back() 
        #self.page.wait_for_timeout(1000)
                


        
   
        
        
        
