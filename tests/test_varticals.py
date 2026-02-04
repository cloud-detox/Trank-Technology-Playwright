import pytest
from pages.trading_page import TradingPage
from pages.retailandecommerce_page import RetailAndEcommerce
from pages.healthcare_page import Healthcare
from pages.fintech_page import Fintech
from pages.custom_app_page import CustomApp




@pytest.mark.smoke
def test_trading(page):
    trading = TradingPage(page)
    trading.click_all_trading_items()
    print(" ****************** Trading completed **********************************")
    

@pytest.mark.smoke
def test_retail_ecommerce(page):
    Retail_ecom = RetailAndEcommerce(page)
    Retail_ecom.click_all_RetailerAndEcommerse()
    print(" ****************** Retail And Ecommerce completed **********************************")

@pytest.mark.smoke
def test_healthcare(page):
    health_care = Healthcare(page)
    health_care.click_all_healthcare()
    print(" ****************** Health care completed**********************************")
 

@pytest.mark.smoke
def test_fintech(page):

    fin_obj=Fintech(page)
    fin_obj.click_all_fintech()
    print(" ****************** Fintech completed **********************************")


@pytest.mark.smoke
def test_custom_app(page):
     
     cust_app=CustomApp(page)
     cust_app.click_all_custom_app()
     print(" ****************** custom app completed **********************************")
