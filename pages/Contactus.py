class ContactUs:
    def __init__(self, page):
        self.page = page
        self.connectus=page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')

    
#  form list :
        self.name=page.locator('(//input[@placeholder="Your Name"])[2]')
        self.mail=page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.company=page.locator('(//input[@placeholder="Your Company"])[2]')
        self.service=page.locator('(//select[@name="service"])[2]')
        self.message=page.locator('(//textarea[@placeholder="Message"])[2]')
        self.submit=page.locator('(//input[@value="Submit"])[2]')

    # Contact us links
        self.webdevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/web-development-company"])[1]')
        self.cms=page.locator('(//a[@href="https://www.tranktechnologies.com/cms-website-development-company"])[1]')
        self.ecommdevelopment=page.locator('(//span[@class="toggle-btn"])[1]')
        self.website=page.locator('(//a[@href="https://www.tranktechnologies.com/website-development-company"])[1]')
        self.customweb=page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')
        self.ui=page.locator('(//a[@href="https://www.tranktechnologies.com/ui-ux-design-company"])[1]')
        self.mobile=page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.responsive=page.locator('(//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"])[1]')
        self.brand=page.locator('(//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"])[1]')

        self.contactuslist=[self.webdevelopment,self.cms,self.ecommdevelopment,self.website,self.customweb,self.ui,self.mobile,self.responsive,self.brand]
       
# App Development
        self.appdevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[1]')
        self.iosappdevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"])[1]')
        self.androidappdevelopment=page.locator('(//span[@class="toggle-btn"])[2]')
        self.androidapp=page.locator('//a[@href="https://www.tranktechnologies.com/android-app-development-company"]')
        self.appdev=page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')
        self.hybrid=page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        self.cross=page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
        self.progressive=page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')

        self.appdevlist=[self.appdevelopment,self.iosappdevelopment,self.appdev,self.hybrid,self.cross,self.progressive]        

    # Graphic Design
        self.graphic=page.locator('//a[@href="https://www.tranktechnologies.com/graphic-design-company"]')
        self.logo=page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        self.banner=page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        self.package=page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.business=page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')

        self.graphiclist=[self.graphic,self.logo,self.banner,self.package,self.business]
       
    def fill_contact_form(self, name, email, company, service, message):
        self.name.fill("Poonam Awasthi")
        self.mail.fill("poonam@yopmail.com")
        self.company.fill("Partech")
        self.service.select_option("App Development")
        self.message.fill("I have written this message for testing purpose. Please ignore it.")
        self.submit.click()

    
    def contactus_click(self):
        for i in self.contactuslist:
           if i==self.ecommdevelopment:
            i.click()
            self.website.click()
           elif i==self.androidappdevelopment:
            i.click()
            self.listofdev=[self.androidappdevelopment,self.appdev]
            for j in self.listofdev:
                    with self.page.context.expect_page() as new_page_info:
                        j.click()
                        new_page = new_page_info.value
                        new_page.wait_for_load_state()
                        new_page.close()
           else:
            self.page.wait_for_timeout(1000)
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
    
    def appdev_click(self):
        for i in self.appdevlist:
            self.connectus.click()
            self.page.wait_for_timeout(1000)
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    def graphic_click(self):
        for i in self.graphiclist:
            self.connectus.click()
            self.page.wait_for_timeout(1000)
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

    