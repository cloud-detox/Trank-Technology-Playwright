

class blog:
    def __init__(self, page):
        self.page = page
        self.blog_var = page.locator('(//a[text()="Blog"])[1]')
    
    #Categories
        self.appdev = page.locator('(//a[text()="App Development"])[3]')
        self.contentmarketing = page.locator('//a[text()="Content Marketing"]')
        self.digitalmarketing = page.locator('(//a[text()="Digital Marketing"])[2]')
        self.emailmarketing = page.locator('(//a[text()="Email Marketing"])[2]')
        self.software_itcomp =page.locator('//a[text()="Software & IT Company"]')
        self.ui_ux_design = page.locator('(//a[text()="UI UX Design"])[6]')
        self.ai = page.locator('(//a[text()="Artificial Intelligence"])[3]')
        self.crm_dev = page.locator('(//a[text()="CRM Development"])[3]')
        self.ecommercedev = page.locator('(//a[text()="ECommerce Development"])[5]')
        self.graphicdesign = page.locator('(//a[text()="Graphic Design"])[3]')
        self.softwaredev = page.locator('(//a[text()="Software Development"])[2]')
        self.webdev = page.locator('(//a[text()="Web Development"])[6]')

        # def blog_method(self):
        #     self.blog_var.click()
        #     self.page.wait_for_timeout(1000)
            
    def cat_method(self):
        self.cat_list = [self.appdev,self.contentmarketing, self.digitalmarketing, self.emailmarketing, self.software_itcomp,self.ui_ux_design,self.ai, self.crm_dev, self.ecommercedev,self.graphicdesign,self.softwaredev,self.webdev]
        for i in self.cat_list:
            self.blog_var.click()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
    