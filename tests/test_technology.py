import pytest
from pages.ecommerce import EcommerceDev
from pages.mobileappdev import MobileAppDev


@pytest.mark.smoke
def test_ecommerce(page):
    techno = EcommerceDev(page)
    techno.ecommerce_dev()

@pytest.mark.smoke
def test_mobile(page):
    techno = MobileAppDev(page)
    techno.mobile_app_dev()
