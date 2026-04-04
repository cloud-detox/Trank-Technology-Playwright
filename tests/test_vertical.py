import pytest
from pages.vertical import vertical
from pages.trading import trading
from pages.customapp import customapp
from pages.fintech import fintech
from pages.healthcare import healthcare
from pages.retail_ecommerce import retail_ecommerce

@pytest.mark.smoke
def test_vertical(page):
    ver=vertical(page)
    
   
    tr=trading(page)
    #page is included as it is inbuild func of plywrt
    tr.tradinglist_clicking()
   
    re=retail_ecommerce(page)
    re.retail_clicking()
   
    
    he=healthcare(page)
    he.health_clicking()
    
    
    cus=customapp(page)
    cus.customapp_clicking()
    
    fin=fintech(page)
    fin.fintech_clicking()
   
   

