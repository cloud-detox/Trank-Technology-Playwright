#Fixture File

import pytest
import allure
from playwright.sync_api import sync_playwright
from config import BASE_URL

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(),
                name="failure",
                attachment_type=allure.attachment_type.PNG
            )

@pytest.fixture(scope="session")
def page():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    browser_page = context.new_page()

    browser_page.goto(BASE_URL)
    browser_page.wait_for_load_state("load")
    
    yield browser_page

    context.close()
    browser.close()
    p.stop()
