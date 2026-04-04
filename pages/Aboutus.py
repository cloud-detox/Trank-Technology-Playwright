class Aboutus:
    def __init__(self,page):
        self.page=page
        self.Aboutus=page.locator('(//a[text()="About us"])[1]')

    def Aboutus_clicking(self):
        self.Aboutus.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()