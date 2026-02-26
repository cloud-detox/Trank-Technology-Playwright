
import pytest

from pages.verticals_page import vertical

@pytest.mark.trading
def test_trading(page):
    verticals_obj = vertical(page)
    verticals_obj.tradingSubMenu_Click()
    verticals_obj.retailSubMenu_Click()
    verticals_obj.HealthCareSubMenu_Click()
    verticals_obj.fintechSubMenu_Click()
    verticals_obj.customAppSubMenu_Click()




