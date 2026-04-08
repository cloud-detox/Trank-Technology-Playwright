from conftest import page
from pages.technology import technology


class CommercePage(technology):

    def __init__(self, page):
        super().__init__(page)
        self.page=page
        
        self.trade=page.locator('//strong[text()="eCommerce Development"]')
        self.MD=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.CD=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.BC=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.CSCD=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.NC=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.LD=page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.DD=page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.JD=page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.EJSD=page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.OCD=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.WPD=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.SD=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.NJD=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.WC=page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.PSD=page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.WXD=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.RJSD=page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
        

        self.CP = [self.MD,self.CD,self.BC,self.CSCD,self.NC,self.LD,self.DD,self.JD,self.EJSD,self.OCD,self.WPD,self.SD,self.NJD,self.WC,self.PSD,self.WXD,self.RJSD]
        
        
    def commerceoption_clicking(self):
          
        for i in self.CP:
            self.technology_hover()
            self.commerce_hover()
            i.click()
            self.page.wait_for_timeout(2500)
            self.page.go_back()