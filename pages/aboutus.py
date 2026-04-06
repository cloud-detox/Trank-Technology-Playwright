from conftest import page
from pages.technologies import technologies


class aboutus:

    def __init__(self, page):
        self.page = page
        self.technologies = page.locator("(//a[text()='Technologies'])[1]")
        self.aboutus = page.locator("//ul[@class='cm-flex-type-2']//a[normalize-space()='About us']")
 
    def aboutus_clicking(self):
        self.aboutus.hover()
        self.aboutus.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()

