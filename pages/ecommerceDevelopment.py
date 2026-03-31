from conftest import page
from pages.technologiespage import TechnologiesPage

class ecommerceDevelopment:
    
    def __init__(self, page):
        self.page = page
        self.technologies=page.locator('(//a[text()="Technologies"])[1]')
        self.ecommerce=page.locator('//strong[text()="eCommerce Development"]')
        self.magento=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.codeigniter=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.BigCommerce=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.cartdevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')   
        self.NOPcommerce=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.Laraveldevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]') 
        self.Drupaldevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.JoomlaDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.ExpressDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.OpencartDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.WordPressDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.ShopifyDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.NodejsDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.Woocommerce=page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.PrestashopDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.Wixdevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.ReactjsDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')

        self.ecommercelist=[self.magento,self.codeigniter,self.BigCommerce,self.cartdevelopment,self.NOPcommerce,self.Laraveldevelopment,self.Drupaldevelopment,self.JoomlaDevelopment,self.ExpressDevelopment,self.OpencartDevelopment,self.WordPressDevelopment,self.ShopifyDevelopment,self.NodejsDevelopment,self.Woocommerce,self.PrestashopDevelopment,self.Wixdevelopment,self.ReactjsDevelopment]

    def ecommerce_options(self):
        for i in self.ecommercelist:
            self.technologies.hover()
            self.page.wait_for_timeout(500)
            self.ecommerce.hover()
            self.page.wait_for_timeout(500)
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()
            