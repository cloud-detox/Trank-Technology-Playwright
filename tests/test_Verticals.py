import pytest

from pages.homepage_locators import homepage

@pytest.mark.smoke
def test_Trading(page):
    homeObj=homepage(page)
    homeObj.mouseHoverVertical()
    page.wait_for_timeout(2000)
    #homeObj.clickTradOptns()
    # homeObj.retailOptns()
    # homeObj.clickHealthCare()
    #homeObj.clickFintech()
    #homeObj.customApp()
    
    
