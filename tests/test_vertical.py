import pytest

from pages.vertical_sub_menu import vertical_sub_menu

@pytest.mark.smoke

def test_vertical(page):
    t=vertical_sub_menu(page)
    t.tradingoption_clicking()
    t.retail_clicking()
    t.healthcare_clicking()
    t.fintech_clicking()
    t.customerapp_clicking()
    page.wait_for_timeout(5000)
    