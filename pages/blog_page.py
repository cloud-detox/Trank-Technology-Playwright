class BlogPage:
    def __init__(self, page):
        self.page = page
        # blog main menu
        self.blog = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')
        # sub menu blog category
        self.appDevelopment = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[2]')
        self.ai=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"]')
        self.contentMarketing=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"]')
        self.crmDevelopment=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
        self.digitalMarketing=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
        self.ecommdevlopment=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
        self.emailmarketing=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"]')
        self.graphicDesign=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
        self.softanadIT=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')
        self.softwareDevelopment=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')
        self.uiux=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
        self.webDevelopment=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')
        
    def open_blog(self):
        #self.blog.click()   
        self.page.wait_for_timeout(1000)
        self.blog_list=[self.appDevelopment,self.ai,self.contentMarketing,self.crmDevelopment,self.digitalMarketing,self.ecommdevlopment,self.emailmarketing,self.graphicDesign,self.softanadIT,self.softwareDevelopment,self.uiux,self.webDevelopment]
        for i in self.blog_list:
          self.blog.click()
          i.click()
          self.page.go_back()
        self.page.go_back()
        
  
        

