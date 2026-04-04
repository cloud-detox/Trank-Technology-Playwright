from conftest import page
from pages.technologies import technologies

class ecommD:
    def __init__(self,page):
        self.page=page
        self.technology=page.locator('(//a[text()="Technologies"])[1]')
        self.ecommD=page.locator('//strong[text()="eCommerce Development"]')

        self.magento=page.locator('//a[text()="Magento Development"]')
        self.codeig=page.locator('(//a[text()="Codeigniter Development"])[1]')
        self.bigec=page.locator('(//a[text()="Big Commerce"])[1]')
        self.cs=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.noncom=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.larevel=page.locator('(//a[text()="Laravel Development"])[1]')
        self.drupal=page.locator('(//a[text()="Drupal Development"])[1]')
        self.loomla=page.locator('(//a[text()="Joomla Development"])[1]')
        self.expjs=page.locator('(//a[text()="Express JS Development"])[1]')
        self.opencart=page.locator('(//a[text()="Opencart Development"])[1]')
        self.wordpress=page.locator('(//a[text()="WordPress Development"])[1]')
        self.shopify=page.locator('(//a[text()="Shopify Development"])[1]')
        self.node=page.locator('(//a[text()="Node JS Development"])[1]')
        self.woo=page.locator('(//a[text()="Woo Commerce"])[1]')
        self.presta=page.locator('(//a[text()="Prestashop Development"])[1]')
        self.wix=page.locator('(//a[text()="Wix Development"])[1]')
        self.reactjs=page.locator('(//a[text()="React JS Development"])[1]')

        self.ecommD_list=[self.magento,self.codeig,self.bigec,self.cs,self.noncom,self.larevel,self.drupal,self.loomla,self.expjs,self.opencart,self.wordpress,self.shopify,self.node,self.woo,self.presta,self.wix,self.reactjs]

    def ecommD_clicking(self):
        for i in self.ecommD_list:
                self.technology.hover()
                self.ecommD.hover()
                i.click()
                self.page.wait_for_timeout(2000)
                self.page.go_back()
    