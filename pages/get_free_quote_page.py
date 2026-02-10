from pages.base_page import BasePage
from playwright.sync_api import Page

class Get_Free_Quote_page_class(BasePage):
    def __init__(self,page: Page):
        super().__init__(page)
 
    def get_free_quote(self):
        self.page.locator('(//a[text()="Get a Free Quote"])[1]').click()
        self.page.locator('//input[@placeholder="Your Name"]').fill("Haritha")
        self.page.locator('//input[@placeholder="Your Mail"]').fill("victory.haritha@gmail.com")
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.get_by_role("button",name = "Send OTP").click()
        self.page.get_by_placeholder("Enter OTP").fill("12345")
        self.page.get_by_placeholder("Your Company").fill("xyz")
        self.page.select_option('//select[@name="service"]',value="Web Development")
        self.page.get_by_placeholder("Your Phone").fill("1234567891")
        self.page.get_by_placeholder("Message").fill("text message")
        
        #self.page.frame_locator('//iframe[@title="reCAPTCHA"]').locator('//div[@class="recaptcha-checkbox-checkmark"]').check()
        
        
        self.page.locator('//input[@value="Submit"]').scroll_into_view_if_needed()
        self.page.wait_for_timeout(3000)
        self.page.locator('//input[@value="Submit"]').click()
        print("Your application submited ")
        self.page.go_back()
