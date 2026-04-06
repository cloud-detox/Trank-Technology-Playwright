from conftest import page
from pages.technologies import technologies


class portfolio:

    def __init__(self, page):
        self.page = page
        self.technologies = page.locator("(//a[text()='Technologies'])[1]")
        self.portfolio = page.locator("//body/header/div[@class='menu']/ul[@class='cm-flex-type-2']/li[6]")

    def portfolio_clicking(self):
        self.portfolio.hover() 
        self.portfolio.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()