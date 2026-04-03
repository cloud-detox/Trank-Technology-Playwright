
class Appdev:

    def __init__(self,page):
        self.page=page
        self.ios=page.locator('//a[text()="iOS App Development"]')
        self.toggle_2=page.locator('(//span[@class="toggle-btn"])[2]')
        self.andr=page.locator('//a[text()="Android App Development"]')
        self.ad1=page.locator('//a[text()="Android App Development Delhi"]')
        self.ad2=page.locator('//a[text()="App Development Delhi"]')
        self.hyb=page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company-in-india"]')
        self.crs=page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company-in-india"]')
        self.prg=page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company-in-india"]')
    
    def ios_clicking(self):
        self.ios.click()
        self.page.wait_for_load_state()
        self.page.go_back()

    def android_clicking(self):
        self.andr.click()
        # Ensure toggle open
        if not self.ad1.is_visible():
            self.toggle_2.click()
        self.ad1.wait_for(state="visible")
        with self.page.expect_popup() as popup_info:
            self.ad1.click(no_wait_after=True)

        new_tab = popup_info.value
        new_tab.wait_for_load_state()
        new_tab.close()

        if not self.ad2.is_visible():
            self.toggle_2.click()
        self.ad2.wait_for(state="visible")
        with self.page.expect_popup() as popup_info:
            self.ad2.click(no_wait_after=True)

        new_tab = popup_info.value
        new_tab.wait_for_load_state()
        new_tab.close()

    def hyb_click(self):
        self.hyb.click()
        self.page.wait_for_load_state()


    def crs_click(self):
        self.crs.click()
        self.page.wait_for_load_state()
 

    def prg_clicking(self):
        self.prg.click()
        self.page.wait_for_load_state()
        

