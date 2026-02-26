import pytest

from pages.technology_page import technology

@pytest.mark.mob
def test_ecommerce(page):
    technology_obj = technology(page)
    technology_obj.ecommerceSubMenu_click()
    technology_obj.mobileappSubMenu_click()
    technology_obj.ai_click()
