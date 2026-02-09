from pages.base_page import BasePage
from playwright.sync_api import Page


class TechnologiesMenuBase(BasePage):
    def __init__(self,page: Page, tab_text: str, panel_id: str):
        super().__init__(page)
        self.tab_text = tab_text
        self.panel_id = panel_id

        self.technologies = page.locator('(//a[text()="Technologies"])[1]')
        self.tab = page.locator(f'//strong[text()="{tab_text}"]')
        self.page_links = page.locator(f'//div[@id="{panel_id}"]//a')

    def open_menu(self):
        self.log_step(f" Opening technologies menu --> {self.tab_text} ")
        self.technologies.hover()
        self.tab.hover()
        self.page.wait_for_timeout(300)
    
    # def ai(self):
    #     self.open_menu()
    #     self.tab.click()
    #     self.page.wait_for_load_state("load")
    #     print(self.page.title())
    #     self.page.go_back()
    #     self.page.wait_for_load_state("domcontentloaded")

    def click_all_pages(self,expected_titles=None):
        failures = []
        count=self.page_links.count()
        for i in range(count):

            self.open_menu()
            click_link=self.page_links.nth(i)

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


        if failures:
            raise AssertionError("\n".join(failures))






        