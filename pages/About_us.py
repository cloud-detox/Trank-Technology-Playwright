class About_us:

    def __init__(self,page):
        self.page=page
        self.About_us=page.locator('(//a[text()="About us"])[1]')


    def about_us_click(self):
        self.About_us.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()

        