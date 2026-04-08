from conftest import page
from pages.technology import technology


class MobilePage(technology):

    def __init__(self, page):
        super().__init__(page)
        self.page=page
        
        self.trade=page.locator('//strong[text()="Mobile App Development"]')
        self.RNMAP=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.XMAP=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.FMAP=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.SAP=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.EMAP=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.KMAP=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.IAP=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.ABD=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

        self.MD = [self.RNMAP,self.XMAP,self.FMAP,self.SAP,self.EMAP,self.KMAP,self.IAP,self.ABD]

    def mobileoption_clicking(self):
          
        for i in self.MD:
            self.technology_hover()
            self.mobileapp_hover()
            i.click()
            self.page.wait_for_timeout(2500)
            self.page.go_back()