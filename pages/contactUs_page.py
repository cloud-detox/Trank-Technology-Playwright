from pages.base_page import BasePage
from playwright.sync_api import Page

class Contact_Us_page_class(BasePage):
    def __init__(self,page: Page):
        super().__init__(page)
        self.click_link= self.page.locator('(//a[text()="Contact us"])[1]')

    def click_ContactUs(self,expected_titles : dict):      
        menu_text = self.click_link.inner_text().strip().lower()
        print("menu_text:",menu_text)  

        self.click_link.wait_for(state='visible')
        self.click_link.click(force=True)
        self.page.wait_for_load_state("domcontentloaded")

        actual_title = self.page.url

        print("actual_title :",actual_title)    
        print("expected_titles.get(menu_text) :",expected_titles.get(menu_text))  
        expected_title = expected_titles.get(menu_text)
        
        assert expected_title is not None, (
            f"No expected title found in CSV for '{menu_text}'"
        )

        assert expected_title in actual_title, (f"Validation failed for '{menu_text}'. "f"Expected '{expected_title}', got '{actual_title}'")

        self.page.go_back()
        self.page.wait_for_load_state("domcontentloaded")

              
