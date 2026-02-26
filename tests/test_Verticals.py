import pytest
from pages.verticals_page import verticals

@pytest.mark.order(1)
def test_verticals(page):
    verticals_obj = verticals(page)
    verticals_obj.tradingSubMenu_Click()
    verticals_obj.retailSubMenu_Click()
    verticals_obj.HealthCareSubMenu_Click()
    verticals_obj.fintechSubMenu_Click()
    verticals_obj.customAppSubMenu_Click()
    
    