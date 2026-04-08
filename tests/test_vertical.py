import pytest


from pages.fintech import FintechPage
from pages.healthcare import HealthCarePage
from pages.retail import RetailPage
from pages.trade import TradingPage
from pages.vertical import vertical
from pages.custom import CustomAppPage


@pytest.mark.smoke
def test_vertical(page):
       
    t=TradingPage(page)
    t.tradingoption_clicking()
    page.wait_for_timeout(3000)

    a=RetailPage(page)
    a.retailoption_clicking()
    page.wait_for_timeout(3000)

    
    b=HealthCarePage(page)
    b.healthcareoption_clicking()
    page.wait_for_timeout(3000)

    f=FintechPage(page)
    f.fintechoption_clicking()
    page.wait_for_timeout(3000)

    c=CustomAppPage(page)
    c.customoption_clicking()
    page.wait_for_timeout(3000)



    


   

