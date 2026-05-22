class aboutus:
    def __init__(self,page):
        self.page=page
    # about us:
        self.about_us=page.locator('(//a[@href="https://www.tranktechnologies.com/about"])[1]')

    #follow us:
        self.fb=page.locator('//img[@alt="Facebook"]')    
        self.lnkin=page.locator('//img[@alt="LinkedIn"]')
        self.insta=page.locator('(//img[@alt="Instagram"])[1]')
        self.pinterest=page.locator('(//img[@alt="Instagram"])[2]')
        self.twitter=page.locator('//img[@alt="Twitter"]')
        self.youtube=page.locator('//img[@alt="Youtube"]')
        self.quara=page.locator('//img[@alt="Quora"]')
        self.follow_list=[self.fb,self.lnkin,self.insta,self.pinterest,self.twitter,self.youtube,self.quara]

    def aboutus_click(self):
        self.about_us.click()
        self.page.wait_for_timeout(1000)    
        self.page.go_back()
        self.page.wait_for_timeout(2000) 

    def follow_us(self):
        self.about_us.click()
        self.page.wait_for_timeout(1000)
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        self.page.wait_for_timeout(1000)
        for i in self.follow_list:
            i.click()
            with self.page.context.expect_page() as new_page_info:
                new_page = new_page_info.value
                new_page.wait_for_load_state()  
                new_page.close()
                self.page.wait_for_timeout(1000)