import pytest
from pages.verticals_page import verticals

@pytest.mark.verticals
def test_verticals(page):
    Verticals_obj = verticals(page)
    Verticals_obj.tradingSubMenu_Click()
    Verticals_obj.retailSubMenu_Click()
    Verticals_obj.HealthCareSubMenu_Click()
    Verticals_obj.fintechSubMenu_Click()
    Verticals_obj.customAppSubMenu_Click()
    
    