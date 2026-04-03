class Contact_us:

    def __init__(self,page):
        self.page=page
        self.contact=page.locator('(//a[text()="Contact us"])[1]')
    
        self.Name=page.locator('(//input[@placeholder="Your Name"])[2]')
        self.Email=page.locator('//input[@placeholder="Your Email"]')
        self.Enter_otp=page.locator('(//input[@placeholder="Enter OTP"])[2]')
        self.Company=page.locator('(//input[@placeholder="Your Company"])[2]')
        self.service=page.locator('(//select[@name="service"])[2]')
        self.service=page.locator('(//select[@name="service"])[2]')
        self.Phone=page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.Message=page.locator('(//textarea[@placeholder="Message"])[2]')
        # self.submit=page.locator('(//input[@type="submit"])[2]')
    
    
    def Contact_us_click(self):
        self.contact.click()
        self.Name.fill("sid")
        self.Email.fill("sidraj@gamil.com")
        self.Enter_otp.fill("111111")
        self.Company.fill("abc")
        self.service.select_option("Web Development")
        self.service.press("Enter")
        self.Phone.fill("9658955430")
        self.Message.fill("abc")
        self.page.go_back()


