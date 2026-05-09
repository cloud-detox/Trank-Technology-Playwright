import pytest

from pages.verticals_page import VerticalsPage


@pytest.mark.smoke
def test_vertical(page):
    obj = VerticalsPage(page)
    #obj.verticalhover()
    # obj.tradinghover()   # Call Method from Pages.
    # obj.retailhover()
    # obj.healthhover()

    # obj.verticalhoverlist() # Call List Method.
   # obj.tradinghoverlist()
   # obj.retailhoverlist()
    #obj.healthcarehoverlist()

@pytest.mark.smoke
def test_trading(page):
    obj = VerticalsPage(page)
    obj.tradinghoverlist()

@pytest.mark.smoke
def test_retail(page):
    obj = VerticalsPage(page)
    obj.retailhoverlist()

@pytest.mark.smoke
def test_healtcare(page):
    obj2 = VerticalsPage(page)
    obj2.healthcarehoverlist() 

@pytest.mark.smoke
def test_fintech(page):
    obj3 = VerticalsPage(page)
    obj3.fintechhoverlist() 

@pytest.mark.smoke
def test_customapp(page):
    obj3 = VerticalsPage(page)
    obj3.customapphoverlist()                      