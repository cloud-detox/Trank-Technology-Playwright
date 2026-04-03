import pytest
from pages.Custom_app import Custom_app
from pages.Fintech import Fintech
from pages.Healthcare import Healthcare
from pages.Retail_Ecommerce import Retail_Ecommerce
from pages.verticalpage import vertical
from pages.trading import trading

@pytest.mark.smoke
def test_vertical(page):
    ver=vertical(page)
    
    t=trading(page)
    t.tradinglist_clicking()
    
    RE=Retail_Ecommerce(page)
    RE.Retail_Ecommerce_clicking()

    HC=Healthcare(page)
    HC.Healthcare_clicking()

    F=Fintech(page)
    F.Fintech_clicking()

    C=Custom_app(page)
    C.Custom_app_clicking()
    
    




