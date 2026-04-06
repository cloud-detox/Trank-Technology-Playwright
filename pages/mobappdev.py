from conftest import page
from pages.technologies import technologies


class mobappdev:

    def __init__(self, page):
        self.page = page
        self.technologies = page.locator("(//a[text()='Technologies'])[1]")
        self.mobappdev = page.locator("//strong[normalize-space()='Mobile App Development']")

        self.op1 = page.locator("//a[contains(text(),'React Native Mobile')]")
        self.op2 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Xamarin Mobile App')]")
        self.op3 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Flutter Mobile App')]")
        self.op4 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Swift App')]")
        self.op5 = page.locator("//a[contains(text(),'Enterprise Mobile App')]")
        self.op6 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Kotlin Mobile App')]")
        self.op7 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Ionic App')]")
        self.op8 = page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[contains(text(),'Appointment Booking')]")

        self.mobappdev_locators=[self.op1,self.op2,self.op3,self.op4,self.op5,self.op6,self.op7,self.op8] 

    def mobappdev_clicking(self):
        for i in self.mobappdev_locators:
            self.technologies.hover()
            self.mobappdev.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()