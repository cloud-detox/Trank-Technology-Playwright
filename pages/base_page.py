# BasePage (generic, reusable)
from playwright.sync_api import Page
class BasePage:
    def __init__(self, page:Page):
        self.page = page


    def log_step(self, message: str):
        print(f"[STEP] {message}")