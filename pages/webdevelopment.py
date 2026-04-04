class webdevelopment:
    def __init__(self,page):
        self.page=page
        self.cms=page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company-in-india"]')
        self.ecomdec=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company-in-india"])[7]')
        self.arrow=page.locator('(//span[@class="toggle-btn"])[1]')
        self.website=page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company-in-delhi-ncr"]')
        self.cuswebdev=page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company-in-india"]')

    def cms_clicking(self):
        self.cms.click()
        self.page.go_back()

    def ecomdec_clicking(self):
        self.ecomdec.click()
        self.page.go_back()
        self.arrow.click()
        with self.page.expect_popup() as popup_info:
            self.page.click('//a[text()="Website Development Delhi"]')
            self.page.wait_for_timeout(5000)
        new_tab = popup_info.value
        new_tab.close() #website tab which newly opened should close
        
        
    def custom_clicking(self):
        self.cuswebdev.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()
