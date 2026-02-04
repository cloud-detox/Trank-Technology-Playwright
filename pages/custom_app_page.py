class CustomApp:
    def __init__(self,page):
        self.page =page

        self.verticals = page.locator('(//a[text()="Verticals"])[1]')
        self.custom_m=page.locator('//strong[text()="Custom App"]')
        self.submenu_items=page.locator('//div[@id="customApp"]//a')

    def open_custom_app(self):
        
        self.verticals.hover()
        
        self.custom_m.hover()
        
        
       

    def click_all_custom_app(self):
        count = self.submenu_items.count()

        for i in range(count):
            self.open_custom_app()
            self.submenu_items.nth(i).wait_for(state="visible")
            #print("item 1 located",self.submenu_items.nth(i))
            self.submenu_items.nth(i).click(force=True) 
            self.page.wait_for_load_state("load")
            print("\n ", self.page.title())
            self.page.go_back()
            self.page.wait_for_load_state("load")
