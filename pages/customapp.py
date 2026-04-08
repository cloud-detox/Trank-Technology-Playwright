from config import URL

class CustomApp:
    def __init__(self, page):
        self.page = page
        self.vertical = page.locator('(//a[text()="Verticals"])[1]')
        self.custapp = page.locator("//strong[text()='Custom App']")
        self.dekappdev = page.locator("(//li//a[contains(@href,'desktop-application-development-company')])[1]")
        self.crmdev = page.locator("(//a[text()='CRM Development'])[1]")
        self.hrmdev = page.locator("(//a[text()='HRM Development'])[1]")
        self.erpdev = page.locator("(//a[text()='ERP App Development'])[1]")
        self.traveldev = page.locator("(//a[text()='Travel'])[1]")
        self.eldev = page.locator("(//a[text()='E-Learning'])[1]")
        self.datingappdev = page.locator("(//a[text()='Dating App Development'])[1]")
        self.realestate = page.locator("(//a[text()='Real Estate'])[1]")
        self.crm = page.locator("(//a[text()='CRM Development USA'])[1]")

        self.list = [self.dekappdev, self.crmdev, self.hrmdev, self.erpdev, self.traveldev, self.eldev, self.datingappdev, self.realestate, self.crm]

    def custom_app(self):
        for i in self.list:
            self.vertical.hover()
            self.page.wait_for_timeout(2000)
            self.custapp.hover()
            i.click(force=True)
            self.page.wait_for_timeout(2000)
            self.page.goto(URL)