from conftest import page
class blog_page:
    def __init__(self, page):
        self.page = page

        #Blog
        self.blog = page.locator('(//a[text()="Blog"])[1]') 
    def blog_Click(self):
        self.blog.click()
    print("**************Blog page is opened************")
    