class contactus:
    def __init__(self,page):
        self.page=page
        #Contact Us:
        self.contactus=page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')

        #contact us form:
        self.name=page.locator('(//input[@name="name"])[2]')
        self.email=page.locator('(//input[@type="email"])[2]')
        self.company=page.locator('(//input[@name="company"])[2]')
        self.service=page.locator('(//select[@name="service"])[2]')
        self.phone=page.locator('(//input[@name="phone"])[2]')
        self.message=page.locator('(//textarea[@name="message"])[2]')
        self.submit=page.locator('(//input[@type="submit"])[2]')

    def contactus_click(self):
        self.contactus.click()
        self.page.wait_for_timeout(1000)    
        self.page.go_back() 
        self.page.wait_for_timeout(2000)    

    def contactus_form(self):
        self.contactus.click()
        self.page.wait_for_timeout(1000)
        self.name.fill("Puja")
        self.email.fill("puja@yopmail.com")
        self.company.fill("Oracle")
        self.service.select_option("UI / UX Design")
        self.phone.fill("78976689778")
        self.message.fill("hi there , testing")
        self.submit.click()
        self.page.wait_for_timeout(2000)