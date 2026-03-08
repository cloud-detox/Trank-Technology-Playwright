from conftest import page
from utils.screenShot import takeScrnsht

class technologies:
    def __init__(self,page):
        self.page=page
        self.technologies=page.locator('(//a[@href="#"])[5]')
    
    
    #ecomoptyns
        self.ecommerc=page.locator("//strong[text()='eCommerce Development']")
        self.magDev=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.openCart=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.codeDesigner=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.wordPress=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.bigCommerce=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.shopify=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.nodeJS=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.nopeCommerce=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.wooCommerce=page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.laravel=page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.presta=page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.drupal=page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.wix=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.reactJS=page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
        self.expressJS=page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.jhoomla=page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.eCommerceList=[self.magDev,self.openCart,self.codeDesigner,self.wordPress,self.bigCommerce,self.shopify,self.nodeJS,self.nopeCommerce,self.wooCommerce,self.laravel,self.presta,self.drupal,self.wix,self.reactJS,self.expressJS,self.jhoomla]
        
        # Mobile app dev sub-menus
        self.MAD = page.locator('(//strong[text()="Mobile App Development"])[1]')
        self.reactNativeMobApp = page.locator('(//a[contains(normalize-space(.),"React Native Mobile App")])[1]')
        self.xamarinMobApp = page.locator('(//a[contains(normalize-space(.),"Xamarin Mobile App")])[1]')
        self.flutterMobApp = page.locator('(//a[contains(normalize-space(.),"Flutter Mobile App")])[1]')
        self.swiftApp = page.locator('(//a[contains(normalize-space(.),"Swift App")])[1]')
        self.entMobApp = page.locator('(//a[contains(normalize-space(.),"Enterprise Mobile App")])[1]')
        self.kotlinMobApp = page.locator('(//a[contains(normalize-space(.),"Kotlin Mobile App")])[1]')
        self.ionicApp = page.locator('(//a[contains(normalize-space(.), "Ionic App")])[1]')
        self.appntmentBookng = page.locator('(//a[contains(normalize-space(.), "Appointment Booking")])[1]')
        
        self.lstMobAppSubMenus = [self.reactNativeMobApp, self.xamarinMobApp, self.flutterMobApp, self.swiftApp,self.entMobApp,self,self.kotlinMobApp,self.ionicApp,self.appntmentBookng]
        
        # Artificial Intelligence and it has no su menus
        self.ArtIntel = page.locator('//strong[text()="Artificial Intelligence"]')
        
    def mouseHoverTechn(self):
        self.technologies.hover()
    def mouseHoverEcomm(self):
        self.ecommerc.hover()
    
    def clickAllEcommOptions(self):
        
        for i in self.eCommerceList:
            self.mouseHoverTechn()
            self.mouseHoverEcomm()
            i.click()
            takeScrnsht(self.page,"Technologies")
            self.page.go_back()
    
    def MApp_Mouseover(self):
        self.MAD.hover()
    
    def ai_click(self):
        self.ArtIntel.click()
              
        
    def mobileAppDev_Click(self):    
        for i in self.lstMobAppSubMenus:    
            self.mouseHoverTechn()
            self.MApp_Mouseover()
            i.click()
            takeScrnsht(self.page, "TechnologiesSubmenu") 
            self.page.go_back()
                 
    
    def ai_Click(self):
        self.mouseHoverTechn()
        self.ai_click()
        takeScrnsht(self.page, "TechnologiesSubmenu")





                            
