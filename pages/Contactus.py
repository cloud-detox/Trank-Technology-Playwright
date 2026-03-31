class ContactUs:

    def __init__(self, page):
        self.page = page
        self.contactus = page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        self.yourname = page.locator('(//input[@placeholder="Your Name"])[2]')
        self.otp = page.locator('(//input[@placeholder="Enter OTP"])[2]')
        self.yourcompany = page.locator('(//input[@placeholder="Your Company"])[2]')
        self.Service= page.locator('(//select[@name="service"])[2]')
        self.phone = page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.message = page.locator('(//textarea[@placeholder="Message"])[2]')
        self.captcha=page.locator('(//iframe[@role="presentation"])[2]')
        self.submit = page.locator('(//input[@value="Submit"])[2]')



    def click_captcha(self):
        frame = self.page.frame_locator('(//iframe[@title="reCAPTCHA"])[2]')
        frame.locator('//div[@class="recaptcha-checkbox-border"]').click()

    def fill_details(self, name, company, service, phone, message):
        self.yourname.fill(name)
        self.otp.fill("123456")
        self.yourcompany.fill(company)
        self.Service.select_option(service)
        self.phone.fill(phone)
        self.message.fill(message)