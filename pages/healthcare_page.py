class Healthcare:
    def __init__(self,page):
      self.page=page

      self.verticals = page.locator('(//a[text()="Verticals"])[1]')
      self.healthcare=page.locator('//strong[text()="Healthcare"]')
      self.submenu_items=page.locator('//div[@id="healthcare"]/ul/li')

           
    def open_healthcare(self):
        self.verticals.hover()
        self.healthcare.hover()
    
    def click_all_healthcare(self):
       count = self.submenu_items.count()

       for i in range(count):
          self.open_healthcare()
          self.submenu_items.nth(i).click()
          self.page.wait_for_load_state("domcontentloaded")
          print("\n", self.page.title())
          self.page.go_back()
          self.page.wait_for_load_state("load")

