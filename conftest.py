import pytest
from playwright.sync_api import sync_playwright
from config import baseurl

# @pytest.fixture(scope="session")
# # def page(request):
#     # p = sync_playwright().start()
#     # browser=p.chromium.launch(headless=False)
#     # context = browser.new_context(ignore_https_errors=True)
#     # page = context.new_page()
# # 
#     # page.goto(baseurl)
#     # page.wait_for_load_state("load")
#     # 
#     # 
#     # yield page
# # 
#     # context.close()
#     # browser.close()
#     # p.stop()

#import pytest
#from playwright.sync_api import Playwright, sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(baseurl)
        yield page
        browser.close()

    