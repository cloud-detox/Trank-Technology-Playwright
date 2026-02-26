import pytest
from pages.technology_page import technology

@pytest.mark.order(2)
def test_technologies(page):
    technology_obj = technology(page)
    technology_obj.ecommSubMenu_Click()
    technology_obj.mobileAppDev_Click()
    technology_obj.ai_Click()