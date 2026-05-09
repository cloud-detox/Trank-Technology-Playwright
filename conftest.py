import pytest
from playwright.sync_api import sync_playwright
import allure
from config import url

@pytest.fixture(scope="session")

def page(request):
    p = sync_playwright().start()
    browser=p.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()

    page.goto(url)
    page.wait_for_load_state("load")
    
    
    yield page

    context.close()
    browser.close()
    p.stop()

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