class TechnologiesPage:
    def __init__(self, page):
        self.page = page

        self.technologies = page.locator('(//a[text()="Technologies"])[1]')
        self.ecommerce_dev = page.locator('//strong[text()="eCommerce Development"]')
        self.mobile_app_dev = page.locator('//strong[text()="Mobile App Development"]')
        self.artificial_intelligence = page.locator('//strong[text()="Artificial Intelligence"]')

        #ecommerce develpoment
        self.magneto_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.codeigniter_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.big_commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.cs_cart_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.nop_commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.laravel_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.drupal_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.joomla_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.express_js_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.open_cart_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.wordpress_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.shopify_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.node_js_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.woo_commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.prestashop_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.wix_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.react_js_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')


        #mobile app development
        self.react_native_mob_app = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.xamarin_mob_app = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.flutter_mob_app = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.swift_mob_app = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.enterprise_mob_app = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.kotlin_mob_app = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.ionic_mob_app = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.appoint_book_app = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

    def technologies_hover(self):
        self.technologies.hover()
        self.page.wait_for_timeout(2000)

    def ecommerce_dev_hover(self):
        ecommerce_dev_list = [self.magneto_dev, self.codeigniter_dev, self.big_commerce, self.cs_cart_dev, self.nop_commerce, self.laravel_dev, self.drupal_dev, self.joomla_dev, self.express_js_dev, self.open_cart_dev, self.wordpress_dev, self.shopify_dev, self.node_js_dev, self.woo_commerce, self.prestashop_dev, self.wix_dev, self.react_js_dev]
        for i in ecommerce_dev_list:                 
            self.technologies.hover()
            self.ecommerce_dev.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def mobile_app_dev_hover(self):
        mobile_app_dev_list = [self.react_native_mob_app, self.xamarin_mob_app, self.flutter_mob_app, self.swift_mob_app, self.enterprise_mob_app, self.kotlin_mob_app, self.ionic_mob_app, self.appoint_book_app]
        for j in mobile_app_dev_list:
            self.technologies.hover()
            self.mobile_app_dev.hover()
            j.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def artificial_intelligence_hover(self):
        self.technologies.hover()
        self.artificial_intelligence.hover()
        self.page.wait_for_timeout(1000)
        self.page.go_back()

        