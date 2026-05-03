import pytest
class contactUs:
    def __init__(self,page):
        self.page = page
        self.contact_us = page.locator('a:has-text("Contact Us")').first
        
    def contactUs_hover(self):
        self.contact_us.hover()
        self.page.wait_for_timeout(2000)

    def open_contactUs_page(self):
        self.contact_us.click()
        self.page.wait_for_timeout(2000)
    