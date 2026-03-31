class Fintech:

    def __init__(self, page):
        self.page = page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.fintech=page.locator('//strong[text()="Fintech"]')
        self.PSD=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.CPT=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company-in-india"])[1]')

        self.Fin=[self.PSD,self.CPT]

    def fintech_options(self):
        for i in self.Fin:
            self.vertical.hover()
            self.fintech.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()
