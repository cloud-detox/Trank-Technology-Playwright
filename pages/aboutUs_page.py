from conftest import page

class aboutus:
    def __init__(self):
        self.aboutus = page.locator('(//a[text()="About us"])[1]')

    def aboutus_click(self):
        self.page.wait_for_timeout(5000)
        self.aboutus.click()
        self.page.wait_for_timeout(5000)
        print("****************** About Us page is opened ***********************")
