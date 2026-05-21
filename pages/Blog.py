class Blog:
    def __init__(self,page):
        self.page=page
        #Blog:
        self.blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')

        #categories list:
        self.appdev=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[2]') 
        self.ai=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"])[1]')
        self.contmarketing=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"]')
        self.CRMdev=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
        self.digiMarketing=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
        self.ecommerceDev=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
        self.emailMArketing=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"]')
        self.graDesign=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
        self.softITcomp=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')
        self.softdev=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')
        self.uiuxDesign=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
        self.webDev=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')
        self.categorylist=[self.appdev,self.ai,self.contmarketing,self.CRMdev,self.digiMarketing,self.ecommerceDev,self.emailMArketing,self.graDesign,self.softITcomp,self.softdev,self.uiuxDesign,self.webDev]



    def blog_click(self):
        self.blog.click()
        self.page.wait_for_timeout(1000)
        self.page.go_back()
        self.page.wait_for_timeout(1000)   

    def category_click(self):
        for i in self.categorylist:
            self.blog.click()
            self.page.wait_for_timeout(1000) 
            i.click()
            self.page.wait_for_timeout(1000) 
            self.page.go_back()
            self.page.wait_for_timeout(1000)
    
