
class blogPage:
    def __init__(self, page):
        self.page = page
        self.blog=page.locator('(//a[text()="Blog"])[1]')

    def blog_clicking(self):
        self.blog.click()
        self.page.wait_for_timeout(2000)
        # self.page.go_back()