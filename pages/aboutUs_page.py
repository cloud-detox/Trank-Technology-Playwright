from conftest import page
from utilities.screenShot import takeScrnsht
class aboutUs:
    def __init__(self, page):
        self.page = page
        self.aboutUs = page.locator('(//a[text()="About us"])[1]')
        
    def aboutUs_Click(self):
        self.aboutUs.click()
        takeScrnsht(self.page, "AboutUsPage")
    print("****************** About Us page is opened ***********************")        
        