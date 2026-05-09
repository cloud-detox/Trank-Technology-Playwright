class TechnologiesPage:
    def __init__(self,page):
        self.page = page
        self.technologies = page.locator("(//a[text()='Technologies'])[1]")
        self.ecommercedev = page.locator("(//strong[text()='eCommerce Development'])[1]")
        self.retail = page.locator("//strong[text()='Mobile App Development']")
        self.health = page.locator("//strong[text()='Artificial Intelligence']")

        #ecommercedev
        self.magento = page.locator ('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.opencart = page.locator ('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.codeigniter = page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.wordpress = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.bigcomm = page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.cscardDev=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.nopcommerce=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.laravelDev=page.locator('(//a[text()="Laravel Development"])[1]')
        self.drupalDev=page.locator('(//a[text()="Drupal Development"])[1]')
        self.joomlaDev=page.locator('(//a[text()="Joomla Development"])[1]')
        self.expressjsDev=page.locator('(//a[text()="Express JS Development"])[1]')
        self.shopifyDev=page.locator('(//a[text()="Shopify Development"])[1]')
        self.nodejsDev=page.locator('(//a[text()="Node JS Development"])[1]')
        self.woocommerce=page.locator('(//a[text()="Woo Commerce"])[1]')
        self.prestashopdev=page.locator('(//a[text()="Prestashop Development"])[1]')
        self.wixdev=page.locator('(//a[text()="Wix Development"])[1]')
        self.reactjsdev=page.locator('(//a[text()="React JS Development"])[1]')
       
        # Mobiel APP
        self.native = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.enterprise = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.xamarinMobAppDev=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.flutterMobAppDev=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.swiftAppDev=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.kotlinMobAppDev=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.ionicAppDev=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.appointmentBookingDev=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')


    def technologyhover(self):
        self.technologies.hover()
        self.page.wait_for_timeout(1000)


############ Child Xpath Get #########################
    def ecommercedevhoverlist(self):
        list_ecommerce = [self.magento,self.opencart,self.codeigniter,self.wordpress,self.bigcomm,self.cscardDev,self.nopcommerce,self.laravelDev,self.drupalDev,self.joomlaDev,self.expressjsDev,self.shopifyDev,self.nodejsDev,self.woocommerce,self.prestashopdev,self.wixdev,self.reactjsdev]
        for i in list_ecommerce:
            self.technologies.hover()
            self.ecommercedev.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()         
    
    def mobileapphoverlist(self):
        list_mobileapp = [self.native,self.enterprise,self.xamarinMobAppDev,self.flutterMobAppDev,self.swiftAppDev,self.kotlinMobAppDev,self.ionicAppDev,self.appointmentBookingDev]
        for j in list_mobileapp:
            self.technologies.hover()
            self.retail.hover()
            j.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    