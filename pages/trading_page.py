class TradingPage:

    def __init__(self, page):
        self.page = page

        self.verticals = page.locator('(//a[text()="Verticals"])[1]')
        self.trading = page.locator('//strong[text()="Trading"]')
        self.trading_items = page.locator('//div[@id="trading"]//a')

    def open_trading_menu(self):
        self.verticals.hover()
        self.trading.hover()

    def click_all_trading_items(self):
        count = self.trading_items.count()

        for i in range(count):
            self.open_trading_menu()
            self.trading_items.nth(i).wait_for(state="visible")
            self.trading_items.nth(i).click(force=True)
            #self.page.wait_for_load_state("load")
            self.page.wait_for_load_state("load")
            print("\n",self.page.title())
            self.page.go_back()
            self.page.wait_for_load_state("domcontentloaded")
            
