from config import URL

class Fintech:
    def __init__(self, page):
        self.page = page
        self.vertical = page.locator('(//a[text()="Verticals"])[1]')
        self.fintech = page.locator("//strong[text()='Fintech']")
        self.pos = page.locator("(//a[normalize-space()='Pos Software Development'])[1]")
        self.crypto = page.locator("(//li//a[contains(@href,'cryptocurrency-mobile-app-development-company-in-india')])[1]")

        self.list = [self.pos, self.crypto]

    def fintech_options(self):
        for i in self.list:
            self.vertical.hover()
            self.page.wait_for_timeout(2000)
            self.fintech.hover()
            i.click(force=True)
            self.page.wait_for_timeout(2000)
            self.page.goto(URL)