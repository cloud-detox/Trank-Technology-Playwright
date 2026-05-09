class AboutUsPage:
    def __init__(self, page):
        self.page = page
        # About Us main menu
        self.aboutUs = page.locator('(//a[@href="https://www.tranktechnologies.com/about"])[1]')
        #  Aboutus webDevelopment
        self.webDevelopment=page.locator('//a[@href="https://www.tranktechnologies.com/web-development-company"]')
        self.cmswebDev=page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        self.ecommDev=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[7]')#not work
        self.ecomm_toggle=page.locator('(//i[@aria-hidden="true"])[3]')
        self.websiteDev=page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company"]')
        self.customWebportalDev=page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')

        #aboutus appDevelopment
        self.appDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[1]')
        self.iosAppDev=page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
        self.androidAppDev=page.locator('//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company"]')
        self.androidappDev_toggle=page.locator('(//i[@aria-hidden="true"])[4]')
        self.androidAppDevDelhi=page.locator('//a[@href="https://www.tranktechnologies.com/android-app-development-company"]')
        self.appDeveopmentDelhi=page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')
        self.hybridAppDev=page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        self.cross_platformAppDev=page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
        self.prograssiveAppDev=page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')


        #aboutus Graphic Design
        self.graphicDesign=page.locator('//a[@href="https://www.tranktechnologies.com/graphic-design-company"]')
        self.logoDesign=page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        self.bannerDesign=page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        self.packagingDesign=page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.businessCardDesign=page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')
        
        #aboutus followUs
        self.followUsFacebook=page.locator('//img[@alt="Facebook"]')
        self.followUsInstagram=page.locator('(//img[@alt="Instagram"])[1]')
        self.followUsTwitter=page.locator('//img[@alt="Twitter"]')
        self.followUsYoutube=page.locator('//img[@alt="Youtube"]')
        self.followUsLinkedin=page.locator('//img[@alt="LinkedIn"]')
        self.followUsPinterest=page.locator('(//img[@alt="Instagram"])[2]')
        self.followUsQuora=page.locator('//img[@alt="Quora"]')





    def open_about_us(self):
        self.aboutUs.click()
    def webDevelopment_menus_clicking(self):
        self.aboutUs.click()
        #self.page.wait_for_timeout(1000)
        
        self.webDevelopment_list=[self.webDevelopment,self.cmswebDev,self.customWebportalDev]
        for i in self.webDevelopment_list:
            #self.open_about_us()
            i.click()
            self.page.go_back()
    def appDevloment_menus_clicking(self):
        self.appDevelopment_list=[self.appDevelopment,self.iosAppDev,self.androidAppDev,self.hybridAppDev,self.cross_platformAppDev,self.prograssiveAppDev]
        for a in self.appDevelopment_list:
           # self.open_about_us()
            a.click()
            self.page.go_back()
        # self.androidappDev_toggle.click()
        # self.androidAppDevDelhi.click()
        # self.page.go_back()
            
        # self.page.wait_for_timeout(1000)
        # self.androidappDev_toggle.click()
        # self.appDeveopmentDelhi.click()
        # self.page.go_back()


    def graphicDesign_menus_clicking(self):
        
        self.graphicDesign_list=[self.graphicDesign,self.logoDesign,self.bannerDesign,self.packagingDesign,self.businessCardDesign]
        for g in self.graphicDesign_list:
            self.open_about_us()
            g.click()
            #self.page.wait_for_timeout(2000)
            self.page.go_back()
    def followUs_menus_clicking(self):
        
        self.followUs_list=[self.followUsFacebook,self.followUsInstagram,self.followUsTwitter,self.followUsYoutube,self.followUsLinkedin,self.followUsPinterest,self.followUsQuora]
        for f in self.followUs_list:
            self.open_about_us()
            with self.page.context.expect_page() as new_page_info: 
                f.click()
            new_page = new_page_info.value
            new_page.wait_for_load_state()  
            new_page.close()

            #self.page.wait_for_timeout(2000)
            self.page.go_back()


          
   
        

