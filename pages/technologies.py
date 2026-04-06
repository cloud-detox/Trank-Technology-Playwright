class technologies:

    def __init__(self, page):
        self.page = page
        self.technologies = page.locator('(//a[text()="Technologies"])[1]')


    def technologies_hover(self):
        self.technologies.hover()

    def ecomdev_hover(self):
        self.ecomdev.hover()

    def mobappdev_hover(self):
        self.mobappdev.hover()

    def artiint_hover(self):
        self.artiint.hover() 

    def aboutus_hover(self):
        self.aboutus.hover()

    def blog_hover(self):
        self.blog.hover()   

    def contactus_hover(self):
        self.contactus.hover()      

    def portfolio_hover(self):
        self.portfolio.hover()                         
