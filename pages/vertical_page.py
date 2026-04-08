class VerticalPage:

    def __init__(self,page):
        self.page = page
        self.vertical = page.locator("(//a[text()='Verticals'])[1]")


    def vertical_hover(self):
        self.vertical.hover()