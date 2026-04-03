from conftest import page
from pages.technologiespage import technologies

class Mobile_app:

    def __init__(self,page):
        self.page=page
        self.technologies=page.locator('(//a[text()="Technologies"])[1]')
        self.Mobile_app=page.locator('//strong[text()="Mobile App Development"]')

        self.React_native=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.Enterprise=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.Xamarin=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.Kotlin=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.Flutter=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.Ionic=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.Swift=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.Appointment=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.Mobile_app_list=[self.React_native,self.Enterprise,self.Xamarin,self.Kotlin,
                        self.Flutter,self.Ionic,self.Swift,self.Appointment]
        
    def  Mobile_app_list_click(self): 
        for i in self.Mobile_app_list:
            self.technologies.hover()
            self.Mobile_app.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()