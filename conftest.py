from playwright.sync_api import sync_playwright
from config import BASE_URL
import pytest

@pytest.fixture(scope="session")
def page():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(ignore_https_errors=True, no_viewport=True)
    page = context.new_page()
    
    page.goto(BASE_URL)
    page.wait_for_laod_state()
    
    yield page
    
    context.close()
    browser.close()
    p.stop()