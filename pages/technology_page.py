from conftest import page
class technology:
    def __init__(self, page):
        self.page = page
        self.technology = page.locator('(//a[text()="Technologies"])[1]')
        self.ecommerce = page.locator('(//strong[text()="eCommerce Development"])[1]')
        self.mobileapp = page.locator('(//strong[text()="Mobile App Development"])[1]')
        self.ai = page.locator('(//strong[text()="Artificial Intelligence"])[1]')

        #ecommerce sub menu 

        self.mangdev = page.locator('(//a[text()="Magento Development"])[1]')
        self.codedev = page.locator('(//a[text()="Codeigniter Development"])[1]')
        self.bigcom = page.locator('(//a[text()="Big Commerce"])[1]')
        self.cscartdev = page.locator('(//a[text()="CS-Cart Development"])[1]')
        self.noncomm = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.laradev = page.locator('(//a[text()="Laravel Development"])[1]')
        self.drupdev = page.locator('(//a[text()="Drupal Development"])[1]')
        self.joomdev = page.locator('(//a[text()="Joomla Development"])[1]')
        self.expjsdev = page.locator('(//a[text()="Express JS Development"])[1]')
        self.opendev = page.locator('(//a[text()="Opencart Development"])[1]')
        self.wordpredev=page.locator('(//a[text()="WordPress Development"])[1]')
        self.shopdev = page.locator('(//a[text()="Shopify Development"])[1]')
        self.nodejs = page.locator('(//a[text()="Node JS Development"])[1]')
        self.woocomm = page.locator('(//a[text()="Woo Commerce"])[1]')
        self.prestadev = page.locator('(//a[text()="Prestashop Development"])[1]')
        self.wixdev = page.locator('(//a[text()="Wix Development"])[1]')
        self.reactjsdev =page.locator('(//a[text()="React JS Development"])[1]')

        #mobileappdevopement submenu

        self.reactnmadev = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.xamarianmdev = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.flutter = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.swift = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.enterprise = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.kotlin = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.ionic = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.appointment = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

    def technology_Mouseover(self):
        self.technology.hover()

    def ecommerce_Mouseover(self):
        self.ecommerce.hover()
    
    def mobileapp_Mouseover(self):
        self.mobileapp.hover()
    
    def ai_Mouseover(self):
        self.ai.hover()

    def ecommerceSubMenu_click(self):
        self.lstecommerce = [self.mangdev,self.codedev,self.bigcom,self.cscartdev,self.noncomm,self.laradev,self.drupdev,self.joomdev,self.expjsdev,self.opendev,self.wordpredev,self.shopdev,self.nodejs,self.woocomm,self.prestadev,self.wixdev,self.reactjsdev]
        for i in self.lstecommerce:
            self.technology_Mouseover()
            self.ecommerce_Mouseover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()
        
    def mobileappSubMenu_click(self):
        self.lstmobileappdev = [self.reactnmadev,self.xamarianmdev,self.flutter,self.swift,self.enterprise,self.kotlin,self.ionic,self.appointment]
        for i in self.lstmobileappdev:
            self.technology_Mouseover()
            self.mobileapp_Mouseover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()

    def ai_click(self):
        self.technology_Mouseover()
        self.ai_Mouseover()
        self.ai.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()


            

    
    


