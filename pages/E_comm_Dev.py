class E_comm_Dev:

    def __init__(self,page):
        self.page=page
        self.CMS_Web=page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company-in-india"]')
        self.E_comm_Dev = page.locator('//a[text()="eCommerce Development"]')
        self.toggle_1 = page.locator('(//span[@class="toggle-btn"])[1]')
        self.website = page.locator('//a[text()="Website Development Delhi"]')
        self.Custom_Webportal=page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company-in-india"]')


    def CMS_Web_click(self):
        self.CMS_Web.click()
        self.page.go_back()
        
    

    def E_comm_Dev_click(self):
        self.E_comm_Dev.click()
        if not self.website.is_visible():
            self.toggle_1.click()
        self.website.wait_for(state="visible")
        with self.page.expect_popup() as popup_info:
            self.website.click(no_wait_after=True)
        new_tab = popup_info.value
        new_tab.wait_for_load_state()
        new_tab.close()


    def Custom_Webportal_click(self):
        self.Custom_Webportal.click()
        self.page.go_back()
        

        