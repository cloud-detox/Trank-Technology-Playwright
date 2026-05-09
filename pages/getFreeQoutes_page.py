class GetFreeQoutesPage:
    def __init__(self, page):
        self.page = page
        self.getFreeQoutes = page.locator('(//a[text()="Get a Free Quote"])[1]')
        # Form fields of Get Free Qoutes  
        self.name=page.locator('//input[@placeholder="Your Name"]')
        self.email=page.locator('//input[@id="email_career"]')
        self.otpbutton=page.locator('//button[@id="send_career_otp"]')
        self.enterotp=page.locator('(//input[@type="text"])[2]')
        self.company=page.locator('//input[@placeholder="Your Company"]')
        self.service=page.locator('//select[@name="service"]')
        self.phone=page.locator('//input[@placeholder="Your Phone"]')
        self.message=page.locator('//textarea[@placeholder="Message"]')
        #self.submitbtn=page.locator('//input[@type="submit"]')
        self.cform=page.locator('//div[@class="cm-close-btn"]')
      
    def free_qoutes_form(self):
        self.getFreeQoutes.click()
        self.name.fill('Piyush Vyas')
        self.email.fill('piyush@gmail.com')
        self.otpbutton.click()
        self.page.wait_for_load_state("networkidle")

        self.page.wait_for_timeout(1000)
        self.enterotp.fill('123456')
        self.company.fill('pray')
        self.service.select_option('App Development')
        self.phone.fill('9876543210')
        self.page.wait_for_timeout(2000)
        self.message.fill('Thi is my first automation testing')
        #self.submitbtn.click()  
        self.page.wait_for_timeout(3000)
        self.cform.click()
        


    



        



        
