from conftest import page
from pages.technologies import technologies


class contactus:

    def __init__(self, page):
        self.page = page
        self.technologies = page.locator("(//a[text()='Technologies'])[1]")
        self.contactus = page.locator("//ul[@class='cm-flex-type-2']//a[normalize-space()='Contact us']")

        self.yourname = page.locator("//form[@id='contact_form']//input[@placeholder='Your Name']")
        self.email = page.locator("//input[@id='email_contact']")
        self.company = page.locator("//form[@id='contact_form']//input[@placeholder='Your Company']")
        self.phone = page.locator("//form[@id='contact_form']//input[@placeholder='Your Phone']")
        self.message = page.locator("//form[@id='contact_form']//textarea[@placeholder='Message']")
        self.submit = page.locator("//input[@name='contact']")

    def contactus_filling(self):    

        self.contactus.hover()
        self.contactus.click()
        self.page.wait_for_timeout(2000)
        self.yourname.fill("Karthik")
        self.email.fill("karthik@example.com")
        self.company.fill("Example Company")
        self.phone.fill("123-456-7890")
        self.message.fill("This is a test message.")
        self.submit.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()
