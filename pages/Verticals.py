from conftest import page
from utils.screenShot import takeScrnsht

class verticals:
    def __init__(self,page):
        self.page=page
        self.vertical= page.locator('(//a[@href="#"])[2]')
        