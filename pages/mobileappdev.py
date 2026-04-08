


from config import URL


class MobileAppDev:
    def __init__(self, page):
        self.page = page
        self.technology = page.locator("//a[text()='Technologies']").first
        self.mobileappdev = page.locator("//strong[normalize-space()='Mobile App Development']")
        self.react = page.locator("//a[contains(text(),'React Native Mobile')]")
        self.enterprise = page.locator("//a[contains(text(),'Enterprise Mobile App')]")
        self.xamarin = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Xamarin Mobile App')]")
        self.kotlin = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Kotlin Mobile App')]")
        self.flutter = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Flutter Mobile App')]")
        self.ionic = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Ionic App')]")
        self.swift = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Swift App')]")
        self.appointment = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Appointment Booking')]")

        self.list = [self.react,self.enterprise,self.xamarin,self.kotlin,self.flutter,self.ionic,self.swift,self.appointment]   

    def mobile_app_dev(self):
        for i in self.list:
            self.technology.hover()
            self.page.wait_for_timeout(2000)
            self.mobileappdev.hover()
            i.click(force=True)
            self.page.wait_for_timeout(2000)
            self.page.goto(URL)