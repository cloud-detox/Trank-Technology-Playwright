
class Footer_page :

    def __init__(self,page):
        self.page=page
        self.footer_likns1=[ 
            page.locator('//a[text()="Web Development"]'),
            page.locator('//a[text()="CMS Website Development"]'),
            page.locator('//a[text()="eCommerce Development"]')]
        
        self.dropdown1=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]')
        self.dropdownoption1=page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company-in-delhi-ncr"]')

        self.footer_likns2 =[
            page.locator('//a[text()="Custom Web Portal Development"]'),
            page.locator('//a[text()="UI UX Design"]'),
            page.locator('//a[text()="Mobile App Design"]'),
            page.locator('//a[text()="Responsive Web Design"]'),
            page.locator('//a[text()="Brand Identity Design"]'),
            page.locator('//a[text()="App Development"]'),
            page.locator('//a[text()="iOS App Development"]'),
            page.locator('//a[text()="Android App Development"]')]
        
        self.dropdown2=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[2]')
        self.dropdownoption2=page.locator('//a[text()="Android App Development Delhi"]')
        self.dropdownoption3=page.locator('//a[text()="App Development Delhi"]')

        self.footer_likns3=[
            page.locator('//a[text()="Hybrid Mobile App Development"]'),
            page.locator('//a[text()="Cross-Platform App Development"]'),
            page.locator('//a[text()="Progressive Web App Development"]'),
            page.locator('//a[text()="Graphic Design"]'),
            page.locator('//a[text()="Logo Design"]'),
            page.locator('//a[text()="Banner Design"]'),
            page.locator('//a[text()="Packaging Design"]'),
            page.locator('//a[text()="Business cards Design"]')]
        
        #Social media
        self.SM_Links=['//img[@alt="Facebook"]','//img[@alt="LinkedIn"]','(//img[@alt="Instagram"])[1]','(//img[@alt="Instagram"])[2]','//img[@alt="Twitter"]',
             '//img[@alt="Youtube"]', '//img[@alt="Quora"]']
        
    def click_footer_links1(self):
        for link in self.footer_likns1:
            link.click()
            self.page.wait_for_load_state("load")
            self.page.wait_for_timeout(2000)
            self.page.go_back()
            self.page.wait_for_timeout(1000)

    def click_dropdown_option1(self):
        self.dropdown1.click()
        with self.page.expect_popup() as new_page_info:
            self.dropdownoption1.click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        new_page.wait_for_timeout(5000)
        new_page.close()   # close only the new tab


    def click_footer_links2(self):
        for link in self.footer_likns2:
            link.click()
            self.page.wait_for_load_state("load")
            self.page.wait_for_timeout(2000)
            self.page.go_back()
            self.page.wait_for_timeout(1000)

    def click_dropdown_option2(self):
        self.dropdown2.click()
        with self.page.expect_popup() as new_page_info:
            self.dropdownoption2.click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        new_page.wait_for_timeout(5000)
        new_page.close()   # close only the new tab
   
    def click_dropdown_option3(self):
        with self.page.expect_popup() as new_page_info:
            self.dropdownoption3.click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        new_page.wait_for_timeout(5000)
        new_page.close()   # close only the new tab


    def click_footer_links3(self):
        for link in self.footer_likns3:
            link.click()
            self.page.wait_for_load_state("load")
            self.page.wait_for_timeout(2000)
            self.page.go_back()
            self.page.wait_for_timeout(1000)           

    def click_Socialmedia_links(self):
        for link in self.SM_Links :
            with self.page.expect_popup() as new_page_info:
                self.page.locator(link).click()
            new_page=new_page_info.value
            new_page.wait_for_load_state()
            new_page.wait_for_timeout(3000)
            new_page.close()


