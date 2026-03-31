class Aboutus:

    def __init__(self, page):
        self.page = page
        self.aboutus = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')

