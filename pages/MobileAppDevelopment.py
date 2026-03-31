from config import BASE_URL

class mobileAppDevelopment:
    
    def __init__(self, page):
        self.page = page
        self.technologies=page.locator('(//a[text()="Technologies"])[1]')
        self.mobile=page.locator('//strong[text()="Mobile App Development"]')
        self.ReactNativeDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.XamarinDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.FlutterDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.SwiftDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.EnterpriseDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.KotlinDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.IonicDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.AppointmentDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

        self.Mobilelist=[self.ReactNativeDevelopment,self.XamarinDevelopment,self.FlutterDevelopment,self.SwiftDevelopment,self.EnterpriseDevelopment,self.KotlinDevelopment,self.IonicDevelopment,self.AppointmentDevelopment]
    
    def mobile_options(self):
        for i in self.Mobilelist:
            self.technologies.hover()
            self.page.wait_for_timeout(500)
            self.mobile.hover(force=True)
            self.page.wait_for_timeout(500)
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()
            