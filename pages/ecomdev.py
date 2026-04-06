from conftest import page
from pages.technologies import technologies


class ecomdev:

    def __init__(self, page):
        self.page = page
        self.technologies = page.locator("(//a[text()='Technologies'])[1]")
        self.ecomdev = page.locator("//strong[normalize-space()='eCommerce Development']")

        self.op1 = page.locator("//a[normalize-space()='Magento Development']")
        self.op2 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Codeigniter Development']")
        self.op3 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Big Commerce']")
        self.op4 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='CS-Cart Development']")
        self.op5 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='CS-Cart Development']")
        self.op6 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Nop')]")
        self.op7 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Laravel Development']")
        self.op8 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Drupal Development']")
        self.op9 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Joomla Development']")
        self.op10 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Opencart Development']")
        self.op11 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='WordPress Development']")
        self.op12 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Shopify Development']")
        self.op13 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Node JS Development']")
        self.op14 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Woo Commerce']")
        self.op15 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Prestashop Development']")
        self.op16 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Wix Development']")
        self.op17 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='React JS Development']")

        self.ecomdev_locators=[self.op1,self.op2,self.op3,self.op4,self.op5,self.op6,self.op7,self.op8,self.op9,self.op10,self.op11,self.op12,self.op13,self.op14,self.op15,self.op16,self.op17]

    def ecomdev_clicking(self):
        for i in self.ecomdev_locators:
            self.technologies.hover()
            self.ecomdev.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()
        


       
