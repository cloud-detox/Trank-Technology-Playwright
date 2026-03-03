import pytest
from pages.technologies_page import technology

@pytest.mark.technologies
def test_technologies(page):
    Technology_obj = technology(page)
    Technology_obj.ecommSubMenu_Click()
    Technology_obj.mobileAppDev_Click()
    Technology_obj.ai_Click()     