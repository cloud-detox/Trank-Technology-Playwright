class contactus:
    def __init__(self,page):
        self.page=page
        self.contactus=page.locator('(//a[text()="Contact us"])[1]')
        self.name=page.locator('(//input[@placeholder="Your Name"])[2]')
        self.email=page.locator('//input[@id="email_contact"]')
        self.company=page.locator('(//input[@placeholder="Your Company"])[2]')
        self.svc=page.locator('(//select[@name="service"])[2]')
        self.phn=page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.msg=page.locator('(//textarea[@placeholder="Message"])[2]')
        self.submit=page.locator('(//input[@type="submit"])[2]')
    
    def contactus_clicking(self):
        self.contactus.click()  
        self.name.fill("Priyanka")
        self.email.fill("Password")
        self.company.fill("company1")
        self.svc.select_option("Web Development")
        self.phn.fill("9890900989")
        self.msg.fill("abc")
        self.submit.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()