import pytest
import sys
import os
import allure
from playwright.sync_api import sync_playwright
from config import BASE_URL

# Add parent directory to Python path so pages module can be imported
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture(scope="session")
def page(request):
    p = sync_playwright().start()
    browser=p.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()

    page.goto(BASE_URL)
    page.wait_for_load_state("load")
    
    
    yield page

    context.close()
    browser.close()
    p.stop()

# @pytest.fixture(autouse=True)
# def reset_page(page):
#     """Reset page to BASE_URL before each test to prevent state pollution"""
#     page.goto(BASE_URL)
#     page.wait_for_load_state("load")
#     yield
#     page.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    # if the test fails, then only the screenshot will be attached to the allure report
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            try:
                allure.attach(
                    page.screenshot(),
                    name="failure_screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                # Handle case where page is already closed
                print(f"Could not capture screenshot: {e}")