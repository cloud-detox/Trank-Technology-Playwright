class RetailAndEcommerce:
    def __init__(self,page):
        self.page=page

        self.verticals = page.locator('(//a[text()="Verticals"])[1]')
        
        self.rande=page.locator('//strong[text()="Retail and Ecommerce"]')
        self.items_in_rande=page.locator('//div[@id="retailEcommerce"]/ul/li')

       
    def Open_Rertail_Ecom(self):
        self.verticals.hover()
        self.rande.hover()


    def click_all_RetailerAndEcommerse(self):
        count=self.items_in_rande.count()

        for i in range(count):
            self.Open_Rertail_Ecom()
            self.items_in_rande.nth(i).click()
            self.page.wait_for_load_state("load")
            print("\n", self.page.title())
            self.page.go_back()
            self.page.wait_for_load_state("load")
            

    

        
   