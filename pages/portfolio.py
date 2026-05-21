class Portfolio:
    def __init__(self, page):
        self.page = page
        self.portfolio = page.locator('//a[text()="Portfolio"]')
        self.ics = page.locator('//a[@href="https://www.icshomework.in/"]')
        self.wings = page.locator('//a[@href="https://www.wingspharma.com/"]')
        self.arena = page.locator('//a[@href="https://arenasonipat.com/"]')
        self.home360 = page.locator('//a[@href="https://home360stores.com/"]')
        self.cords = page.locator('//a[@href="https://cordscable.tranktechnologies.com/"]')

    def portfolio_method(self):
        portfolio_list = [self.ics, self.wings, self.arena, self.home360, self.cords]
        for i in portfolio_list:
            self.portfolio.click()
            # scroll method to scroll the element into view if it's not already visible
            i.scroll_into_view_if_needed()
            # method to switch into new tab
            with self.page.context.expect_page() as new_page_info:
                i.click()
            new_page = new_page_info.value
            new_page.wait_for_load_state()
            new_page.close()