


class contact:
    def __init__(self, page):
        self.page = page
        self.contact = page.locator('(//a[text()="Contact us"])[1]')

        self.name = page.locator('(//input[@placeholder="Your Name"])[2]')
        self.mail = page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.send_otp = page.locator('(//button[@type="button"])[2]')
        self.enter_otp = page.locator('(//input[@placeholder="Enter OTP"])[2]')
        self.company = page.locator('(//input[@placeholder="Your Company"])[2]')
        self.choose_serv = page.locator('(//select[@name="service"])[2]')
        self.phn_nbr = page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.message = page.locator('(//textarea[@placeholder="Message"])[2]')
        self.submit = page.locator('(//input[@value="Submit"])[2]')

    def contact_method(self):
        self.contact.click()
        self.choose_serv.select_option("Web Development")
        self.name.fill("kavya")
        self.mail.fill("kavyashree0215@gmail.com")
        self.send_otp.click()
        self.page.once("dailog", lambda dailog : dailog.accept())
        self.enter_otp.fill("4144")
        self.company.fill("SBS")
        self.phn_nbr.fill("9986790411")
        self.message.fill("Thanks")
        self.submit.click()
        self.page.go_back()
        
