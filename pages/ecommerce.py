from config import URL


class EcommerceDev:
    def __init__(self,page):
        self.page = page
        # explicit first match to avoid strict mode múltiples match error
        self.technology = page.locator("//a[text()='Technologies']").first
        self.ecommerce = page.locator("//strong[normalize-space()='eCommerce Development']")
        self.magenato = page.locator("//a[normalize-space()='Magento Development']")
        self.opencart = page.locator("(//a[normalize-space()='Opencart Development'])[1]")
        self.codeignitor = page.locator("(//a[normalize-space()='Codeigniter Development'])[1]")
        self.wordpress = page.locator("(//a[normalize-space()='WordPress Development'])[1]")
        self.bigcommerce = page.locator("(//a[normalize-space()='Big Commerce'])[1]")
        self.shopify = page.locator("(//a[normalize-space()='Shopify Development'])[1]")
        self.cscart = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='CS-Cart Development']")
        self.nodejs = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Node JS Development']")
        self.nop = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Nop')]")
        self.woo = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Woo Commerce']")
        self.laravel = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Laravel Development']")
        self.prestashop = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Prestashop Development']")
        self.drupal = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Drupal Development']")
        self.wix = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Wix Development']")
        self.joomla = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Joomla Development']")
        self.reactjs = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='React JS Development']")
        self.expressjs = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Express JS Development']")

        self.list = [self.magenato,self.opencart,self.codeignitor,self.wordpress,self.bigcommerce,self.shopify,self.cscart,self.nodejs,self.nop,self.woo,self.laravel,self.prestashop,self.drupal,self.wix,self.joomla,self.reactjs,self.expressjs]

    def ecommerce_dev(self):
        for i in self.list:
            self.technology.hover()
            self.page.wait_for_timeout(2000)
            self.ecommerce.hover()
            i.click(force=True)
            self.page.wait_for_timeout(2000)
            self.page.goto(URL)