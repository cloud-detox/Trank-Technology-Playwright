class portfolio_page:
    def __init__(self, page):
        self.page = page
        # portfolio main menu
        self.portfolio = page.locator('//a[@href="https://www.tranktechnologies.com/portfolio"]')
        self.ics_homework = page.locator('//a[@href="https://www.icshomework.in/"]')
        self.wings_pharma = page.locator('//a[@href="https://www.wingspharma.com/"]')
        self.arena_animation = page.locator('//a[@href="https://arenasonipat.com/"]')
        self.home360 = page.locator('//a[@href="https://home360stores.com/"]')
        #self.club_meetings = page.locator('(//a[text()="View More"])[5]') - Some issue with this link
        self.card_cables = page.locator('//a[@href="https://cordscable.tranktechnologies.com/"]')

    def portfolio_menu_clicking(self):
        self.portfolio.click()
        self.page.wait_for_timeout(2000)

    def portfolio_links_clicking(self):
        self.portfolio_links_list = [self.ics_homework, self.wings_pharma, self.arena_animation, self.home360, self.card_cables]
        for i in self.portfolio_links_list:
            self.portfolio.click()
            self.page.wait_for_timeout(2000)
            with self.page.context.expect_page() as new_page_info:
                i.click()
            new_page = new_page_info.value
            self.page.wait_for_timeout(3000)
            new_page.close()