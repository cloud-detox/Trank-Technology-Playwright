import pytest

from pages.technologies_page import TechnologiesPage

@pytest.mark.smoke
@pytest.mark.rande
def test_technologies(page):
    obj = TechnologiesPage(page)
    obj.technologies_hover()

@pytest.mark.smoke
@pytest.mark.rande
def test_ecommerce_dev(page):
    obj = TechnologiesPage(page)
    obj.ecommerce_dev_hover()

@pytest.mark.smoke
@pytest.mark.rande
def test_mobile_app_dev(page):
    obj = TechnologiesPage(page)
    obj.mobile_app_dev_hover()

@pytest.mark.smoke
@pytest.mark.rande
def test_artificial_intelligence(page):
    obj = TechnologiesPage(page)
    obj.artificial_intelligence_hover()

