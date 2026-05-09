from conftest import page


class contactUsPage:
    def __init__(self, page):
        self.page = page
        # Contact Us main menu
        self.contactUs = page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        # Form fields
        self.name = page.locator('(//input[@placeholder="Your Name"])[2]')
        self.email = page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.sentotp_button=page.locator('(//button[@type="button"])[2]')
        self.enterotp=page.locator('(//input[@placeholder="Enter OTP"])[2]')
        self.company=page.locator('(//input[@name="company"])[2]')
        self.selectService=page.locator('(//select[@name="service"])[2]')
        self.phone = page.locator('(//input[@name="phone"])[2]')
        self.message = page.locator('(//textarea[@name="message"])[2]')
       
        
        
        #self.page.wait_for_timeout(2000)

        self.submitBtn = page.locator('(//input[@value="Submit"])[2]')


    

    def fill_contact_form(self):
        self.contactUs.click()
        self.page.wait_for_timeout(2000)
        self.name.fill('Amardeep Kumar')
        self.email.fill('testamar@gmail.com')
        #self.sentotp_button.click()
        self.page.wait_for_timeout(2000)
        self.enterotp.fill('123456')
        self.company.fill('trank')
        self.selectService.select_option('App Development')
        self.phone.fill('7018975624')
        self.message.fill('testing')
        self.page.go_back()
       # self.page.wait_for_timeout(5000)
        #  #recaotcha
        # self.frame=page.locator('(//iframe[@title="reCAPTCHA"])[2]')
        # self.frame_locator('(//div[@role="presentation"])[1]').click()
        # self.submitBtn.click()
        #self.page.wait_for_timeout(2000)
        
        #self.page.wait_for_timeout(5000)
        


        
                   