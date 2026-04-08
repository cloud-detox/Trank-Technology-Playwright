import pytest
from playwright.sync_api import sync_playwright
from config import URL

@pytest.fixture(scope="function")
def page(request):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.set_default_timeout(30000)
    page.set_default_navigation_timeout(30000)

    page.goto(URL, wait_until="domcontentloaded")
    page.wait_for_load_state("load")
    
    yield page

    try:
        context.close()
    except:
        pass
    try:
        browser.close()
    except:
        pass
    p.stop()

