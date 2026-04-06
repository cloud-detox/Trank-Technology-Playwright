from conftest import page
from pages.technologies import technologies


class artiint:

    def __init__(self, page):
        self.page = page
        self.technologies = page.locator("(//a[text()='Technologies'])[1]")
        self.artiint = page.locator("//strong[normalize-space()='Artificial Intelligence']")

    def artiint_clicking(self):
        self.technologies.hover()
        self.artiint.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()
    
    