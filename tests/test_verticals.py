
import pytest
from pages.customapp import CustomApp
from pages.fintech import Fintech
from pages.healthcare import HealthCare
from pages.trading_page import TradingPage
from pages.retailecommerce import RetailAndEcommerce


@pytest.mark.smoke
def test_trading(page):
    trading = TradingPage(page)
    trading.trading_options()

@pytest.mark.smoke
def test_retail_ecommerce(page):
    retail = RetailAndEcommerce(page)
    retail.retail_commerce()

@pytest.mark.smoke
def test_healthcare(page):
    health = HealthCare(page)
    health.health_care()

@pytest.mark.smoke
def test_fintech(page):
    fin = Fintech(page)
    fin.fintech_options()

@pytest.mark.smoke
def test_customapp(page):
    custom = CustomApp(page)
    custom.custom_app()