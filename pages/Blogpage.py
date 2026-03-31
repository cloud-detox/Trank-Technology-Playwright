class blogpage:

    def __init__(self, page):
        self.page = page
        self.blog = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')


