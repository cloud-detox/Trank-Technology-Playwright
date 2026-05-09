import pytest
from config import url
from pages.verticals_page import verticalsPage

'''
@pytest.mark.smoke
def test_verticals_menu(page):
    vp = verticalsPage(page)
    vp.open_verticals()


@pytest.mark.smoke
def test_trading(page):
    vp = verticalsPage(page)
    vp.trading_hover()
    '''
@pytest.mark.smoke
def test_trading(page):
    vp=verticalsPage(page)
    vp.verticals_trading_clicking()
    
   
@pytest.mark.smoke
def test_retails(page):
    vp = verticalsPage(page)
    vp.vertical_retail_clicking()

@pytest.mark.smoke
def test_healthcare(page):
    vp = verticalsPage(page)
    vp.vertical_healthcare_clickig()
    


@pytest.mark.smoke
def test_fintech(page):
    vp = verticalsPage(page)
    vp.vertical_fintech_clicking()
    
   


@pytest.mark.smoke
def test_custom_apps(page):
    vp = verticalsPage(page)
    vp.vertical_customapp_clicking()
    