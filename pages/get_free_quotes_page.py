class GetFreeQuotesPage:
    def __init__(self, page):
        self.page = page

        #Get free quote main menu
        self.get_free_quote = page.locator('(//a[text()="Get a Free Quote"])[1]')
        self.your_name = page.locator('//input[@placeholder="Your Name"]')
        self.your_email = page.locator('//input[@placeholder="Your Mail"]')
        self.send_otp = page.locator('//button[@onclick="sendcareersOTP()"]')
        self.enter_otp = page.locator('(//input[@placeholder="Enter OTP"])[1]')
        self.your_company = page.locator('//input[@placeholder="Your Company"]')
        self.choose_service = page.locator('//select[@name="service"]')
        self.your_phone = page.locator('//input[@placeholder="Your Phone"]')
        self.message = page.locator('//textarea[@placeholder="Message"]')
        self.frame = page.frame_locator('//iframe[@title="reCAPTCHA"]')
        self.not_robot = self.frame.locator('//div[@class="recaptcha-checkbox-border"]')
        self.submit = page.locator('//input[@value="Submit"]')
        self.close_button = page.locator('//div[@class="cm-close-btn"]')
        

    def get_free_quote_menu_clicking(self):
        self.get_free_quote.click()
        self.page.wait_for_timeout(1000)


    def get_free_quote_form_filling(self, name, email, otp, company, service, phone, message):
        self.your_name.fill(name)
        self.your_email.fill(email)

        self.send_otp.click()
        self.enter_otp.wait_for(state="visible")
        self.enter_otp.fill(str(otp))
        self.your_company.fill(company)
        self.choose_service.select_option(service)
        self.your_phone.fill(phone)
        self.message.fill(message)
        self.close_button.click()
        self.page.wait_for_timeout(2000)
