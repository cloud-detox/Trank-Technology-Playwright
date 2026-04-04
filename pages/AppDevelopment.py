class AppDevelopment:
    def __init__(self,page):
        self.page=page
        self.ios=page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company-in-india"]')
        self.andr=page.locator('//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company-in-india"]')
        self.arrow2=page.locator('(//span[@class="toggle-btn"])[2]')
        self.ad1=page.locator('//a[@href="https://www.tranktechnologies.com/android-app-development-company-in-delhi-ncr"]')
        self.ad2=page.locator('//a[@href="https://www.tranktechnologies.com/app-development-company-in-delhi-ncr"]')
        self.hyb=page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company-in-india"]')
        self.crs=page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company-in-india"]')
        self.prg=page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company-in-india"]')

    def ios_clicking(self):
        self.ios.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()

    def andriod_clicking(self):
        self.andr.click()
        self.page.go_back()
        self.arrow2.click()
        with self.page.expect_popup() as popup_info:
            self.ad1.click()
            self.page.wait_for_timeout(5000)
        new_tab = popup_info.value
        new_tab.close()

        self.arrow2.click()
        with self.page.expect_popup() as popup_info:
            self.ad2.click()
            self.page.wait_for_timeout(5000)
        new_tab = popup_info.value
        new_tab.close()

    def hyb_click(self):
        self.hyb.click()

    def crs_clicking(self):
        self.crs.click()

    def prg_clicking(self):
        self.prg.click()
        

