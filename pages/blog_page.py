import pytest
class blog:
    def __init__(self,page):
        self.page = page
        self.blog = page.locator('a:has-text("Blog")').first
       
    def blog_hover(self):
        self.blog.hover()
        self.page.wait_for_timeout(2000)

    def open_blog_page(self):
        self.blog.click()
        self.page.wait_for_timeout(3000)