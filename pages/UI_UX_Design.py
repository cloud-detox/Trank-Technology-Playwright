class UI_UX_Design:

    def __init__(self,page):
        self.page=page
        # self.UI_UX_Design=page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company-in-india"]')
        self.Mobile_app_Design=page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company-in-india"]')
        self.Responsibe_web=page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company-in-india"]')
        self.Brand_Identity=page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company-in-india"]')
        self.UI_UX_Design_list=[self.Mobile_app_Design,self.Responsibe_web,self.Brand_Identity]

    def UI_UX_Design_click(self):
        for i in self.UI_UX_Design_list:
            i.click()
            self.page.go_back()
