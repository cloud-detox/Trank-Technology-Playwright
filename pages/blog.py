from conftest import page
from pages.technologies import technologies


class blog:

    def __init__(self, page):
        self.page = page
        self.technologies = page.locator("(//a[text()='Technologies'])[1]")
        self.blog = page.locator("//ul[@class='cm-flex-type-2']//a[normalize-space()='Blog']")

    def blog_clicking(self):
        self.blog.hover()
        self.blog.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()