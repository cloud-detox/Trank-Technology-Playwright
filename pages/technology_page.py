from conftest import page
from utilities.screenShot import takeScrnsht

class technology:
    def __init__(self, page):
        self.page = page

        #Technology
        self.technology = page.locator('(//a[text()="Technologies"])[1]')
        
        self.ecomm = page.locator('(//strong[text()="eCommerce Development"])[1]')
        self.MAD = page.locator('(//strong[text()="Mobile App Development"])[1]')
        self.ai = page.locator('(//strong[text()="Artificial Intelligence"])[1]')
        
        # eCommerceDev sub-menus
        self.magentoDev = page.locator('(//a[text()="Magento Development"])[1]')
        self.codeigniterDev = page.locator('(//a[text()="Codeigniter Development"])[1]')
        self.bigComm = page.locator('(//a[text()="Big Commerce"])[1]')
        self.csCartDev = page.locator('(//a[text()="CS-Cart Development"])[1]')
        self.nopComm = page.locator('(//a[contains(normalize-space(.),"Nop Commerce")])[1]')
        self.laravelDev = page.locator('(//a[text()="Laravel Development"])[1]')
        self.drupalDev = page.locator('(//a[text()="Drupal Development"])[1]')
        self.joomlaDev = page.locator('(//a[text()="Joomla Development"])[1]')
        self.expressJSDev = page.locator('(//a[text()="Express JS Development"])[1]')
        self.openCartDev = page.locator('(//a[text()="Opencart Development"])[1]')
        self.wordPressDev = page.locator('(//a[text()="WordPress Development"])[1]')
        self.shopifyDev = page.locator('(//a[text()="Shopify Development"])[1]')
        self.nodeJSDev = page.locator('(//a[text()="Node JS Development"])[1]')
        self.wooComm = page.locator('(//a[text()="Woo Commerce"])[1]')
        self.prestashopDev = page.locator('(//a[text()="Prestashop Development"])[1]')
        self.wixDev = page.locator('(//a[text()="Wix Development"])[1]')
        self.reactJSDev = page.locator('(//a[text()="React JS Development"])[1]')
        
        self.lsteCommSubMenus = [self.magentoDev, self.codeigniterDev, self.bigComm, self.csCartDev, self.nopComm, self.laravelDev, self.drupalDev, self.joomlaDev, self.expressJSDev, self.openCartDev, self.wordPressDev, self.shopifyDev, self.nodeJSDev, self.wooComm, self.prestashopDev, self.wixDev, self.reactJSDev]
        
        # Mobile app dev sub-menus
        self.reactNativeMobApp = page.locator('(//a[contains(normalize-space(.),"React Native Mobile App")])[1]')
        self.xamarinMobApp = page.locator('(//a[contains(normalize-space(.),"Xamarin Mobile App")])[1]')
        self.flutterMobApp = page.locator('(//a[contains(normalize-space(.),"Flutter Mobile App")])[1]')
        self.swiftApp = page.locator('(//a[contains(normalize-space(.),"Swift App")])[1]')
        self.entMobApp = page.locator('(//a[contains(normalize-space(.),"Enterprise Mobile App")])[1]')
        self.kotlinMobApp = page.locator('(//a[contains(normalize-space(.),"Kotlin Mobile App")])[1]')
        self.ionicApp = page.locator('(//a[contains(normalize-space(.), "Ionic App")])[1]')
        self.appntmentBookng = page.locator('(//a[contains(normalize-space(.), "Appointment Booking")])[1]')
        
        self.lstMobAppSubMenus = [self.reactNativeMobApp, self.xamarinMobApp, self.flutterMobApp, self.swiftApp, self.entMobApp, self.kotlinMobApp, self.ionicApp, self.appntmentBookng]
        
        # Artificial Intelligence and it has no su menus
        self.ArtIntel = page.locator('//strong[text()="Artificial Intelligence"]')
        
    def technology_Mouseover(self):
        self.technology.hover()
        
    def ecomm_Mouseover(self):
        self.ecomm.hover()
        
    def MAD_Mouseover(self):
        self.MAD.hover()
        
    def ai_click(self):
        self.ArtIntel.click()
    
    def ecommSubMenu_Click(self):    
     for i in self.lsteCommSubMenus:    
            self.technology_Mouseover()
            self.ecomm_Mouseover()
            i.click()
            self.page.go_back()
            takeScrnsht(self.page, "TechnologiesSubmenu")
    print("****************** eCommerce Development completed ***********************")           
    
    
    def mobileAppDev_Click(self):    
     for i in self.lstMobAppSubMenus:    
            self.technology_Mouseover()
            self.MAD_Mouseover()
            i.click()
            self.page.go_back()
            takeScrnsht(self.page, "TechnologiesSubmenu")
    print("****************** Mobile App Development completed ***********************")           
    
    def ai_Click(self):
        self.technology_Mouseover()
        self.ai_click()
        takeScrnsht(self.page, "TechnologiesSubmenu")
    print("****************** Artificial Intelligence completed ***********************")