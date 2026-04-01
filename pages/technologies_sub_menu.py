
from pages.technologiespage import TechnologiesPage

class technologies_sub_menu:

    def __init__(self,page):
        self.page=page
        self.technologies=TechnologiesPage(page)
        self.eCOMdev_locators=[
            page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')]
        
        self.mobileapp_locators=[ 
            page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]'),
            page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')]
        
        self.artificial_locators= page.locator('//li[@data-id="aipage"]')
        
    def click_options(self,category_method, locators):
        for option in locators:
            self.technologies.hover_technologies()
            category_method()
            option.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def technologies_clicking(self):
        self.click_options(self.technologies.hover_technologies,self.eCOMdev_locators)

    def eComdev_clicking(self):
        self.click_options(self.technologies.hover_eComdev,self.eCOMdev_locators)

    def mobileapp_clicking(self):
        self.click_options(self.technologies.hover_mobileapp,self.mobileapp_locators)

    def artificial_clicking(self):
        self.technologies.technologies_menu.hover()
        self.artificial_locators.click()



        



