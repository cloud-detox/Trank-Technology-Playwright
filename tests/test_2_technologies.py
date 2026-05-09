import pytest


from pages.technology_page import TechnologiesPage


@pytest.mark.smoke
def test_technologies(page):
    obj = TechnologiesPage(page)
   
@pytest.mark.smoke
def test_ecommerce(page):
    obj = TechnologiesPage(page)
    obj.ecommercedevhoverlist()

@pytest.mark.smoke
def test_mobile_app(page):
    obj = TechnologiesPage(page)
    obj.mobileapphoverlist()

