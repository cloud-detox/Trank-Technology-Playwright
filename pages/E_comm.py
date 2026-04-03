from conftest import page
from pages.technologiespage import technologies

class E_comm:

    def __init__(self,page):
        self.page=page
        self.technologies=page.locator('(//a[text()="Technologies"])[1]')
        self.E_comm=page.locator('//strong[text()="eCommerce Development"]')

        self.Magenta=page.locator('//a[text()="Magento Development"]')
        self.Opencart=page.locator('(//a[text()="Opencart Development"])[1]')
        self.Codeigniter=page.locator('(//a[text()="Codeigniter Development"])[1]')
        self.Wordpress=page.locator('(//a[text()="WordPress Development"])[1]')
        self.Big_comm=page.locator('(//a[text()="Big Commerce"])[1]')
        self.Shopify=page.locator('(//a[text()="Shopify Development"])[1]')
        self.CS_cart=page.locator('(//a[text()="CS-Cart Development"])[1]')
        self.Node_js=page.locator('(//a[text()="Node JS Development"])[1]')
        self.Nop_comm=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.Woo_comm=page.locator('(//a[text()="Woo Commerce"])[1]')
        self.Laravel_Dev=page.locator('(//a[text()="Laravel Development"])[1]')
        self.Prestashop=page.locator('(//a[text()="Prestashop Development"])[1]')
        self.Drupal=page.locator('(//a[text()="Drupal Development"])[1]')
        self.Wix=page.locator('(//a[text()="Wix Development"])[1]')
        self.Joomala=page.locator('(//a[text()="Joomla Development"])[1]')
        self.React_js=page.locator('(//a[text()="React JS Development"])[1]')
        self.Express_js=page.locator('(//a[text()="Express JS Development"])[1]')
        self.E_comm_list=[self.Magenta,self.Opencart,self.Codeigniter,self.Wordpress,self.Big_comm,self.Shopify,self.CS_cart,self.Node_js,self.Nop_comm,
                    self.Woo_comm,self.Laravel_Dev,self.Prestashop,self.Drupal,self.Wix,self.Joomala,self.React_js,self.Express_js]
        
    def E_comm_clicking(self):   
        for i in self.E_comm_list:
            self.technologies.hover()
            self.E_comm.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()
