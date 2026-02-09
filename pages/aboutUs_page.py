from pages.base_page import BasePage
from playwright.sync_api import Page

class AbourUs(BasePage):
    def __init__(self,page: Page):
        super().__init__(page)

    def click_about(self,expected_titles=None):       
        failures = []        
        click_link= self.page.locator('(//a[text()="About us"])[1]') #About us mainmenu
        #self.page.wait_for_load_state("load")
        link_text =click_link.inner_text()
        self.log_step(f"clicking link --> {link_text}")

        click_link.wait_for(state='visible')
        click_link.click(force=True)

        self.page.wait_for_load_state('domcontentloaded')
        actual_title = self.page.title()            
        self.log_step(f"Landed on page: {actual_title}")
        if expected_titles:
                ex = expected_titles.get(link_text)
                if ex and ex not in actual_title:
                    failures.append(f" {link_text} → Expected '{ex}', got '{actual_title}'")
            
        self.page.go_back()
        self.page.wait_for_load_state("domcontentloaded")


     



        