from conftest import page


class portfolio:
    def __init__(self,page):
        self.page=page
        #portfolio:
        self.portfolio=page.locator('//a[@href="https://www.tranktechnologies.com/portfolio"]')
        #footer webdevelopment:
        self.cms=page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        self.ecommDrop=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]') #drop down click
        self.webdev=page.locator('(//a[@href="https://www.tranktechnologies.com/website-development-company"])')
        self.webportal=page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')
        self.webdevlist=[self.cms,self.webportal]

        #UI UX design , Graphic design:
        self.mobileDesign=page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.responsiveDesign=page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        self.brandDesign=page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')
        self.logoDesign=page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        self.bannerDesign=page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        self.packageDesign=page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.businessCardDesign=page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')
        self.uiGraphiclist=[self.mobileDesign,self.responsiveDesign,self.brandDesign,self.logoDesign,self.bannerDesign,self.packageDesign,self.businessCardDesign]

        #app development:
        self.iosdev=page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
        self.hybriddev=page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        self.crossplatformdev=page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
        self.prowebappdev=page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')
        self.androiddev=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[2]') #drop down click
        self.androidappdev=page.locator('//a[@href="https://www.tranktechnologies.com/android-app-development-company"]')
        self.appdev=page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')
        self.appdevlist=[self.iosdev,self.hybriddev,self.crossplatformdev,self.prowebappdev]
        self.androiddroplist=[self.androidappdev,self.appdev]

        #'view more' of projects:
        self.ics = page.locator('//a[@href="https://www.icshomework.in/"]')
        self.wings = page.locator('//a[@href="https://www.wingspharma.com/"]')
        self.arena = page.locator('//a[@href="https://arenasonipat.com/"]')
        self.home360 = page.locator('//a[@href="https://home360stores.com/"]')
        self.cords = page.locator('//a[@href="https://cordscable.tranktechnologies.com/"]')

        #testimonials:
        self.next=page.locator('//button[@aria-label="Next"]')
        self.prev=page.locator('//button[@aria-label="Previous"]')
        self.nextprevlist=[self.next,self.prev]

        #review us:
        self.reviewheader=page.locator('//h3[text()="Review Us"]')
        self.reviewus=page.locator('(//img[@src="https://www.tranktechnologies.com/assets/new-assets/footer-badges/top-software-developers.png"])[2]')
    
    def portfolio_click(self):
        self.portfolio.click()
        self.page.wait_for_timeout(1000)    
        self.page.go_back() 
        self.page.wait_for_timeout(2000)

    def webdev_click(self):
        self.portfolio.click()
        for i in self.webdevlist:
            self.page.wait_for_timeout(1000)
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
            self.page.wait_for_timeout(2000) 
   

    def webdrop_close(self):
        self.portfolio.click()
        self.page.wait_for_timeout(1000)
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        self.page.wait_for_timeout(1000)
        self.ecommDrop.click()
        self.webdev.click()
        #New tab open and close
        with self.page.context.expect_page() as new_page_info:  
            new_page = new_page_info.value
            new_page.wait_for_load_state()  
            new_page.close()
            self.page.wait_for_timeout(2000)

    def uiGraphic_click(self):
        self.portfolio.click()
        for i in self.uiGraphiclist:
            self.page.wait_for_timeout(1000)
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
            self.page.wait_for_timeout(2000)  

    def appdev_click(self):
        self.portfolio.click()
        for i in self.appdevlist:
            self.page.wait_for_timeout(1000)
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
            self.page.wait_for_timeout(2000) 

    def appdroplist_click(self):
        self.portfolio.click()
        self.page.wait_for_timeout(1000)
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        self.page.wait_for_timeout(1000)
        self.androiddev.click()
        for i in self.androiddroplist:           
            self.page.wait_for_timeout(1000)
            i.click()
            with self.page.context.expect_page() as new_page_info:               
                new_page = new_page_info.value
                new_page.wait_for_load_state()  
                new_page.close()                    
        self.page.wait_for_timeout(2000)    
        
    def portfolio_method(self):
        self.portfolio_list = [self.ics, self.wings, self.arena, self.home360, self.cords]
        for i in self.portfolio_list:
            self.portfolio.click()
            i.scroll_into_view_if_needed()
            with self.page.context.expect_page() as new_page_info:
                i.click()
                new_page = new_page_info.value
                new_page.wait_for_load_state()  
                new_page.close()

    def Testimonials_click(self):
        self.page.wait_for_timeout(1000)
        for i in self.nextprevlist:
            i.click()
            self.page.wait_for_timeout(1000)   
        self.page.wait_for_timeout(2000)     

    def reviewus_click(self):
        self.reviewus.click()
        with self.page.context.expect_page() as new_page_info:
            new_page = new_page_info.value
            new_page.wait_for_load_state()  
            new_page.close()
            self.page.wait_for_timeout(2000)          

    #trying to write a method which combines the dropdown and other options in one method

    #     for i in self.contactuslist:
    #        if i==self.ecommdevelopment:
    #         i.click()
    #         self.website.click()
    #        elif i==self.androidappdevelopment:
    #         i.click()
    #         self.listofdev=[self.androidappdevelopment,self.appdev]
    #         for j in self.listofdev:
    #                 with self.page.context.expect_page() as new_page_info:
    #                     j.click()
    #                     new_page = new_page_info.value
    #                     new_page.wait_for_load_state()
    #                     new_page.close()
    #        else:
    #         self.page.wait_for_timeout(1000)
    #         i.click()
    #         self.page.wait_for_timeout(1000)
    #         self.page.go_back()            