class blog_page:
    def __init__(self, page):
        self.page = page
        #self.home_page = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/logo/trank-logo.webp"]')
        # Main blog menu
        self.blog_menu = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')

        # blog categories
        self.app_dev_blog = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[2]')
        self.artificial_intelligence_blog = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"]')
        self.content_marketing_blog = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"]')
        self.crm_development_blog = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
        self.digital_marketing_blog = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
        self.ecommerce_blog = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
        self.email_marketing_blog = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"]')
        self.graphic_design_blog = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
        self.software_it_company_blog = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')
        self.software_dev_blog = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')
        self.ui_ux_design_blog = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
        self.web_dev_blog = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')


    def blog_menu_clicking(self):
        self.blog_menu.click()
        self.page.wait_for_timeout(2000)

    def blog_categories_clicking(self):
        self.blog_categories_list = [self.app_dev_blog, self.artificial_intelligence_blog, self.content_marketing_blog, self.crm_development_blog, self.digital_marketing_blog, self.ecommerce_blog, self.email_marketing_blog, self.graphic_design_blog, self.software_it_company_blog, self.software_dev_blog, self.ui_ux_design_blog, self.web_dev_blog]
        for i in self.blog_categories_list:
            self.blog_menu.hover()
            i.wait_for(state="visible")
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
            self.page.wait_for_load_state("load")
        self.page.go_back()
