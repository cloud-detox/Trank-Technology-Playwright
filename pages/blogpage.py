class BlogPage:
    def __init__(self,page):
        self.page = page
        #self.home = page.locator('(//img[@alt="Trank Technologies"])[1]')
        self.blog = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')
        

#Categoried
        self.appdev = page.locator('(//a[text()="App Development"])[3]')  
        self.ContentMarketing = page.locator('//a[text()="Content Marketing"]')
        self.artifical = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"]')
        self.crm = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
        self.digital = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
        self.ecommerce = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
        self.email = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"]')
        self.graphic = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
        self.software = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')
        self.softwareDev=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')
        self.uiux=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
        self.webDev=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')


    def click_blog(self):
        self.page.wait_for_timeout(1000)
        #self.home.click()
        self.blog.click()
        self.page.go_back()


    def click_blog_again(self):
        list_blog = [self.ContentMarketing,self.appdev,self.artifical,self.crm,self.digital,self.ecommerce,self.email,self.graphic,self.software,self.softwareDev,self.uiux,self.webDev]
        for k in list_blog:
            self.blog.click()
            k.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()              
