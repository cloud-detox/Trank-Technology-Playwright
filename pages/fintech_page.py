class Fintech:
    def __init__(self,page):
        self.page=page

        self.verticals = page.locator('(//a[text()="Verticals"])[1]')
        self.fintech=page.locator('//strong[text()="Fintech"]')
        self.submenu_items=page.locator('//div[@id="fintech"]/ul/li')

    def open_fintech(self):
        self.verticals.hover()
        self.fintech.hover()
    
    def click_all_fintech(self):
        count=self.submenu_items.count()

        for i in range(count):
            self.open_fintech()
            
            self.submenu_items.nth(i).click()
            self.page.wait_for_load_state("domcontentloaded")
            print("\n ", self.page.title())
            self.page.go_back()
            self.page.wait_for_load_state("load")
