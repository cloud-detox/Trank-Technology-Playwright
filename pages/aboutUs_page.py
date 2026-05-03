
class aboutusPage:
    def __init__(self,page):
        self.page=page
        self.aboutus=page.locator('(//a[text()="About us"])[1]')


    def aboutus_clicking(self):
        self.aboutus.click()
        self.page.wait_for_timeout(2000)
        # self.page.go_back()