class GetFreeQoutesPage:
    def __init__(self, page):
        self.page = page
        # Get Free Qoutes main menu
        self.getFreeQoutes = page.locator('(//a[text()="Get a Free Quote"])[1]')
        # Form fields   
        self.yourname=page.locator('//input[@name="name"]')
        self.youremail=page.locator('//input[@id="email_career"]')
        self.otpbutton=page.locator('//button[@id="send_career_otp"]')
        self.enterotp=page.locator('(//input[@type="text"])[2]')
        self.yourcompany=page.locator('//input[@placeholder="Your Company"]')
        self.selectservice=page.locator('//select[@name="service"]')
        self.yourphone=page.locator('//input[@placeholder="Your Phone"]')
        self.yourmessage=page.locator('//textarea[@placeholder="Message"]')
        self.submitbtn=page.locator('//input[@type="submit"]')
        self.crossform=page.locator('//div[@class="cm-close-btn"]')
      
    def fill_get_free_qoutes_form(self):
        self.getFreeQoutes.click()
        self.page.wait_for_timeout(2000)
        self.yourname.fill('Amardeep Kumar')
        self.youremail.fill('testamar@gmail.com')
        self.otpbutton.click()
        self.page.wait_for_timeout(3000)
        self.enterotp.fill('123456')
        self.yourcompany.fill('trank')
        self.selectservice.select_option('App Development')
        self.yourphone.fill('7018975624')
        self.yourmessage.fill('testing')
        #self.submitbtn.click()  
        self.crossform.click()
        #self.page.wait_for_timeout(5000)
        


    



        



        
