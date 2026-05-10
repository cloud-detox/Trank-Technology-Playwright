class ContactusPage:
    def __init__(self,page):
        self.page = page
        self.home = page.locator('(//img[@alt="Trank Technologies"])[1]')
        self.contact = page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        self.name = page.locator('(//input[@placeholder="Your Name"])[2]')
        self.email = page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.enterotp=page.locator('(//input[@placeholder="Enter OTP"])[2]')
        self.company=page.locator('(//input[@name="company"])[2]')
        self.selectService=page.locator('(//select[@name="service"])[2]')
        self.phone = page.locator('(//input[@name="phone"])[2]')
        self.message = page.locator('(//textarea[@name="message"])[2]')
        self.submitBtn = page.locator('(//input[@value="Submit"])[2]')


    def contact_method(self):
        #self.home.click()
        self.contact.click()
        self.page.wait_for_timeout(1000)
        self.name.fill("Piyush")
        self.email.fill("apn.kvb@gmail.com")
        #self.sentotp_button.click()
        self.page.wait_for_timeout(2000)
        # self.otpsend.click()
        # self.page.once("dialog", lambda dailog : dailog.accept())
        # self.otp.fill("1234")
        self.enterotp.fill('123456')
        self.company.fill('trank')
        self.selectService.select_option('App Development')
        self.phone.fill('7018975624')
        self.message.fill('testing')
        self.page.go_back()