import pytest

from pages.verticals_page import VerticalsPage

@pytest.mark.smoke
def test_vertical(page): 
    obj = VerticalsPage(page)
    obj.vertical_hover()

@pytest.mark.smoke
def test_trading(page): 
    obj = VerticalsPage(page)
    obj.trading_hover()

@pytest.mark.smoke
def test_retail_ecommerce(page): 
    obj = VerticalsPage(page)
    obj.retail_ecommerce_hover()

@pytest.mark.smoke
def test_healthcare(page): 
    obj = VerticalsPage(page)
    obj.healthcare_hover()

@pytest.mark.smoke
def test_fintech(page): 
    obj = VerticalsPage(page)
    obj.fintech_hover()

@pytest.mark.smoke
def test_customapp(page):
    obj = VerticalsPage(page)
    obj.customapp_hover()

