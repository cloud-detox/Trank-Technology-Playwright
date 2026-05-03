


import pytest

from pages.verticals_page import verticalsPage
from pages.technologies_page import technologiesPage
from pages.aboutus_page import aboutusPage

@pytest.mark.smoke
def test_verticals(page):
    obj = verticalsPage(page)
    obj.verticals_hover()

@pytest.mark.smoke
def test_trading(page):
    vp = verticalsPage(page)
    vp.verticals_trading_clicking()
    vp.verticals_retail_ecommerce_clicking()
    vp.verticals_healthcare_clicking()
    vp.verticals_fintech_clicking()
    vp.verticals_custom_app_clicking()
    

@pytest.mark.smoke
def test_technologies(page):
    tech = technologiesPage(page)
    tech.ecommdev_clicking()
    tech.mobileappdev_clicking()
    tech.ai_clicking()

@pytest.mark.smoke
def test_aboutus(page):
    abt = aboutusPage(page)
    abt.aboutus_clicking()
    

