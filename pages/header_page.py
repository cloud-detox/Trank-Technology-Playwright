class Header_Page:
    def __init__(self,page):
        self.page=page

        self.about_us_click=page.locator('(//a[text()="About us"])[1]')

        self.click_blog=page.locator('(//a[text()="Blog"])[1]')
        self.blog_list=[ 
            page.locator('(//a[text()="App Development"])[3]'),
            page.locator('(//a[text()="Artificial Intelligence"])[3]'),
            page.locator('//a[text()="Content Marketing"]'),
            page.locator('(//a[text()="CRM Development"])[3]'),
            page.locator('(//a[text()="Digital Marketing"])[2]'),
            page.locator('(//a[text()="ECommerce Development"])[2]'),
            page.locator('(//a[text()="Email Marketing"])[2]'),
            page.locator('(//a[text()="Graphic Design"])[3]'),
            page.locator('//a[text()="Software & IT Company"]'),
            page.locator('(//a[text()="Software Development"])[2]'),
            page.locator('(//a[text()="UI UX Design"])[3]'),
            page.locator('(//a[text()="Web Development"])[6]')]
        
        self.contactus=page.locator('(//a[text()="Contact us"])[1]')
        self.Portfolio=page.locator('//a[text()="Portfolio"]')
    
    def clickaboutpage(self):
         self.about_us_click.click()
         self.page.go_back()
         self.page.wait_for_timeout(2000)

    def clickblogpage(self):
            self.click_blog.click()
            for link in self.blog_list:
                 link.click()
                 self.page.wait_for_timeout(2000)
                 self.page.go_back()
                 self.page.wait_for_timeout(2000)       
  
    def clickcontactus(self):
         self.contactus.click()
         self.page.wait_for_timeout(2000)

    def clickportfolio(self):
         self.Portfolio.click()
         self.page.go_back()
         self.page.wait_for_timeout(2000)
