import pytest
class aboutUs:
    def __init__(self,page):
        self.page = page
        self.about_us = page.locator('a:has-text("About Us")').first
        
    def aboutUs_hover(self):
        self.about_us.hover()
        self.page.wait_for_timeout(2000)

    def open_aboutUs_page(self):
        self.about_us.click()
        self.page.wait_for_timeout(2000)

