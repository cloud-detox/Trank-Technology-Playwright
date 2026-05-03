

import pytest
from config import BASE_URL

from pages.verticalpage import vertical

@pytest.mark.smoke
def test_vertical_page(page):
    obj_1 = vertical(page)
    obj_1.vert_trading_click()

@pytest.mark.smoke
def test_retail(page):
    obj_1 = vertical(page)
    obj_1.vert_ret_ecom_click()

@pytest.mark.smoke
def test_health(page):
    obj_1 = vertical(page)
    obj_1.vert_health_click()

pytest.mark.smoke
def test_fintech(page):
    obj_1 = vertical(page)
    obj_1.vert_fintech_click()

@pytest.mark.smoke
def test_custom(page):
    obj_1 = vertical(page)
    obj_1.vert_custom_click()
    

    