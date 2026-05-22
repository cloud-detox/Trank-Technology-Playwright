
from playwright.sync_api import expect

class homepage:
    def __init__(self, page):
        self.page = page
        # homepage links - explore solution:
        self.exploreSolu = page.locator('(//a[@href="https://www.tranktechnologies.com/web-development-company"])[1]')

    def exploreSolu_click(self):
        self.exploreSolu.click()
        expect(self.page.locator("body")).to_contain_text("Web Development Company")
        
        print("Successfully landed on correct page")
        self.page.wait_for_timeout(1000)
        self.page.go_back()
        self.page.wait_for_timeout(2000)    