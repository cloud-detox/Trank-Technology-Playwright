class AboutUs:
    def __init__(self, page):
        self.page = page
        self.aboutus = page.locator("//ul[@class='cm-flex-type-2']//a[normalize-space()='About us']")

    def about_us(self):
        self.aboutus.click()