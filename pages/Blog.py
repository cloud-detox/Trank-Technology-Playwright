class Blog:

    def __init__(self,page):
        self.page=page
        self.Blog=page.locator('(//a[text()="Blog"])[1]')


    def Blog_click(self):
        
        self.Blog.click()
    
        self.page.go_back()
        