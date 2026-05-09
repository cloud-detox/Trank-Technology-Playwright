class contact_us_page:
    def __init__(self, page):
        self.page = page

        self.contact_us = page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        self.name = page.locator('(//input[@placeholder="Your Name"])[2]')
        self.email = page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.send_otp = page.locator('(//button[text()="Send OTP"])[2]')
        self.enter_otp = page.locator('(//input[@placeholder="Enter OTP"])[2]')
        self.your_company = page.locator('(//input[@placeholder="Your Company"])[2]')
        self.service_type = page.locator('(//select[@name="service"])[2]')
        self.phone = page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.message = page.locator('(//textarea[@placeholder="Message"])[2]')
        self.frame = page.frame_locator('(//iframe[@title="reCAPTCHA"])[2]')
        self.not_robot = self.frame.locator('//div[@class="recaptcha-checkbox-border"]')
        self.submit_btn = page.locator('(//input[@value="Submit"])[2]')

    def contact_us_hover(self):
        self.contact_us.click()
        self.page.wait_for_timeout(2000)

    def contact_us_form(self):
        self.contact_us.click()
        self.name.fill("Trank Technologies")
        self.email.fill("navyashree.cd@gmail.com")
        self.send_otp
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.send_otp.click()
        self.page.wait_for_timeout(35000)
        self.enter_otp.fill("1234")
        self.your_company.fill("Trank Technologies")
        self.service_type.select_option("Web Development")
        self.phone.fill("1234567890")
        self.message.fill("This is a test message.")
        self.message.blur()  # Move focus out of the textbox
        # Wait for reCAPTCHA iframe to load and checkbox to be visible
        # self.page.wait_for_timeout(3000)
        # self.not_robot.scroll_into_view_if_needed()
        # self.not_robot.wait_for(state="visible", timeout=15000)
        # self.not_robot.click()
        # # Wait for reCAPTCHA verification to complete
        # self.page.wait_for_timeout(8000)
        # self.submit_btn.click()
        self.page.wait_for_timeout(5000)
        self.page.go_back()