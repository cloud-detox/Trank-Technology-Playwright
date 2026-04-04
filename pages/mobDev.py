from conftest import page
from pages.technologies import technologies

class mobDev:
    def __init__(self,page):
        self.page=page
        self.technology=page.locator('(//a[text()="Technologies"])[1]')
        self.MADev=page.locator('//strong[text()="Mobile App Development"]')

        self.reactnative=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.xam=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.flutter=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.swift=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.enterprs=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.kotlin=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.ionic=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.apbookingdev=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

        self.mobile_list=[self.reactnative,self.xam,self.flutter,self.swift,self.enterprs,self.kotlin,self.ionic,self.apbookingdev]
    
    def mobDev_clicking(self):
        for i in self.mobile_list:
            self.technology.hover()
            self.MADev.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()
