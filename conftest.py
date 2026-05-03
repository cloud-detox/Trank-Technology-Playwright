
# Fixture File
# in Fixture file we write the commands which will be reused in other files

# import pytest
# from config import base_url

# @pytest.fixture(scope="function")
# def start_page(page):
#     page.goto(base_url)
#     page.wait_for_load_state("load")
#     # Set a default timeout for all actions
#     page.set_default_timeout(10000)  # 10 seconds
#     return page


import pytest
from playwright.sync_api import sync_playwright
from config import BASE_URL

@pytest.fixture(scope="session")

def page(request):
    p = sync_playwright().start()
    browser=p.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    browser_page = context.new_page()

    browser_page.goto(BASE_URL)
    browser_page.wait_for_load_state("load")
    
    
    yield browser_page

    context.close()
    browser.close()
    p.stop()

# Alias for start_page to match test file expectations
# @pytest.fixture(scope="session")
# def start_page(page):
#     return page