from conftest import page
from utilities.screenShot import takeScrnsht
class blog_page:
    def __init__(self, page):
        self.page = page

        #Blog
        self.blog = page.locator('(//a[text()="Blog"])[1]')
        
        # self.appDev = page.locator('(//a[text()="App Development"])[1]')
        # self.webDev = page.locator('(//a[text()="Web Development"])[1]')
        # self.softwareDev = page.locator('(//a[text()="Software Development"])[1]')
        # self.digitalMarketing = page.locator('(//a[text()="Digital Marketing"])[1]')
        # self.emailMarketing = page.locator('(//a[text()="Email Marketing"])[1]')
        # self.artificialIntelligence = page.locator('(//a[text()="Artificial Intelligence"])[1]')
        # self.uiuxDesign = page.locator('(//a[text()="UI UX Design"])[1]')
        
        #Search
        self.search = page.locator('(//span[text()="Search"])[1]')
        self.searchBox = page.locator('//input[@class="search_text"]')
        self.searchButton = page.locator('(//i[@class="fa fa-search"])[1]')
        self.searchCloseButton = page.locator('//div[@class="close_srch_panel"]')
        
    def blog_Click(self):
        self.blog.click()
        takeScrnsht(self.page, "BlogPage")
    print("**************Blog page is opened************")
    
    def searchFunc(self):
        self.search.click()
        self.page.wait_for_load_state()
        self.searchBox.fill("UI UX Design")
        takeScrnsht(self.page, "Searched Text")
        self.page.wait_for_load_state()
        self.searchButton.click()
        takeScrnsht(self.page, "SearchFunc-BlogPage")