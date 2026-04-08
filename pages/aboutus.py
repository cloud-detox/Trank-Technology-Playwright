from conftest import page
class AboutPage:

    def __init__(self, page):
        self.page=page
        self.aboutus=page.locator('(//a[@href="https://www.tranktechnologies.com/about"])[1]')
        # self.CMSWD=page.locator('(//a[@href="https://www.tranktechnologies.com/cms-website-development-company-in-india"])[1]')
        # self.ECD=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company-in-india"])[7]')
        # self.CWPD=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company-in-india"])[1]')
        # self.MAD=page.locator('(//a[@href="https://www.tranktechnologies.com/mobile-app-design-company-in-india"])[1]')
        # self.RWD=page.locator('(//a[@href="https://www.tranktechnologies.com/responsive-web-design-company-in-india"])[1]')
        # self.BID=page.locator('(//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company-in-india"])[1]')
        # self.IAD=page.locator('(//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company-in-india"])[1]')
        # self.AAD=page.locator('(//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company-in-india"])[1]')
        # self.HMAD=page.locator('(//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company-in-india"])[1]')
        # self.CPAD=page.locator('(//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company-in-india"])[1]')
        # self.LD=page.locator('(//a[@href="https://www.tranktechnologies.com/logo-design-company-in-india"])[1]')
        # self.BD=page.locator('(//a[@href="https://www.tranktechnologies.com/banner-design-company-in-india"])[1]')
        # self.PD=page.locator('(//a[@href="https://www.tranktechnologies.com/packaging-design-company-in-india"])[1]')
        # self.BCD=page.locator('(//a[@href="https://www.tranktechnologies.com/business-cards-design-company-in-india"])[1]')

        # self.AU = [self.CMSWD,self.ECD,self.CWPD,self.MAD,self.RWD,self.BID,self.IAD,self.AAD,self.HMAD,self.CPAD,self.LD,self.BD,self.PD,self.BCD]


    def aboutusoption_clicking(self):
        self.aboutus.click()
        

        # for i in self.AU:
            
        #     i.click()
           
        #     self.page.go_back()
            