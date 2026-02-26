from conftest import page

class contactUs:
    def __init__(self, page):
        self.page = page
        #Contact Us
        self.contactUs = page.locator('(//a[text()="Contact us"])[1]')
            
        # Consultation Form
        self.name = page.locator('(//input[@placeholder="Your Name"])[2]')
        self.email = page.locator('//input[@placeholder="Your Email"]')
        self.sendOtp = page.locator('//button[@id="send_otp"]')
        self.enterOTP = page.locator('(//input[@placeholder="Enter OTP"])[2]')
        #self.company = page.locator('(//input[@placeholder="Your Company"])[2]')
        self.service = page.locator('(//select[@name="service"])[2]')
        self.phone = page.locator('(//input[@name="phone"])[2]')
        self.message = page.locator('(//textarea[@placeholder="Message"])[2]')
        self.submit = page.locator('//input[@name="contact"]')
        
    def contactUs_Click(self):
        self.contactUs.click()
        
    def fillConsultationForm(self):
        self.name.fill("vijay")
        self.email.fill("email@test.com")
        self.sendOtp.click()
        # Assuming OTP is received and entered correctly
        self.enterOTP.fill("123456")  
        #self.company.fill("company1")
        self.service.select_option(label = "App Development")
        self.phone.fill("9922112345")
        self.message.fill("Message from a Tester")
        self.submit.click()
        