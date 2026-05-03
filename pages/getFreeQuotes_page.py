import pytest
class getFreeQuotes:
    def __init__(self,page):
        self.page = page
        self.get_free_quotes = page.locator('(//a[text()="Get a Free Quote"])[1]')

    def getFreeQuotes_hover(self):
        self.get_free_quotes.hover()
        self.page.wait_for_timeout(2000)

    def open_getFreeQuotes_page(self):
        self.get_free_quotes.click()
        self.page.wait_for_timeout(2000)