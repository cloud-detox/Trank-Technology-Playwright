
class technologiesPage:
    def __init__(self,page):
        self.page=page
        self.technologies=page.locator('(//a[text()="Technologies"])[1]')
        self.ecommdev=page.locator('//strong[text()="eCommerce Development"]')
        self.mobileappdev=page.locator('//strong[text()="Mobile App Development"]')
        self.ai=page.locator('//strong[text()="Artificial Intelligence"]')

        #eCommerce Development
        self.magnetodev=page.locator('//a[text()="Magento Development"]')
        self.codeingniterdev=page.locator('(//a[text()="Codeigniter Development"])[1]')
        self.bigcommerce=page.locator('(//a[text()="Big Commerce"])[1]')
        self.cartdev=page.locator('(//a[text()="CS-Cart Development"])[1]')
        self.nopcommerce=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.laraveldev=page.locator('(//a[text()="Laravel Development"])[1]')
        self.drupaldev=page.locator('(//a[text()="Drupal Development"])[1]')
        self.joomladev=page.locator('(//a[text()="Joomla Development"])[1]')
        self.opencartdev=page.locator('(//a[text()="Opencart Development"])[1]')
        self.wordpressdev=page.locator('(//a[text()="WordPress Development"])[1]')
        self.shopifydev=page.locator('(//a[text()="Shopify Development"])[1]')
        self.nodejsdev=page.locator('(//a[text()="Node JS Development"])[1]')
        self.webcommerce=page.locator('(//a[text()="Woo Commerce"])[1]')
        self.prestashop=page.locator('(//a[text()="Prestashop Development"])[1]')
        self.wixdev=page.locator('(//a[text()="Wix Development"])[1]')
        self.reactjsdev=page.locator('(//a[text()="React JS Development"])[1]')

        #Mobile App Development
        self.raectnative=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.xamarian=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.flutter=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.swift=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.enterprise=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.kotlin=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.ionic=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.appointment=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

    def technologies_hover(self):
        self.technologies.hover()
        self.page.wait_for_timeout(1000)

    def ecommdev_clicking(self):
        ecommdev_list=[self.magnetodev,self.codeingniterdev,self.bigcommerce,self.cartdev,self.nopcommerce,self.laraveldev,self.drupaldev,self.joomladev,self.opencartdev,
                       self.wordpressdev,self.shopifydev,self.nodejsdev,self.webcommerce,self.prestashop,self.wixdev,self.reactjsdev]
        for i in ecommdev_list:
            self.technologies_hover()
            self.ecommdev.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back

    def mobileappdev_clicking(self):
        mobileappdev_list=[self.raectnative,self.xamarian,self.flutter,self.swift,self.enterprise,self.kotlin,self.ionic,self.appointment]
        for i in mobileappdev_list:
            self.technologies_hover()
            self.mobileappdev.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def ai_clicking(self):
        self.technologies_hover()
        self.ai.hover()
        self.page.wait_for_timeout(1000)
        self.page.go_back()



