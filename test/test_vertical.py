import pytest


from pages.CustomApp import CustomApp
from pages.Trading import Trading
from pages.verticalpage import vertical
from pages.Fintech import Fintech
from pages.Healthcare import Healthcare
from pages.Retail import Retail

@pytest.mark.smoke
def test_trading(page):
      t=Trading(page) 
      t.trading_options()
      page.wait_for_timeout(5000)

@pytest.mark.smoke
def test_retail(page):
      r=Retail(page) 
      r.retail_options()
      page.wait_for_timeout(5000)    


@pytest.mark.smoke
def test_healthcare(page):
      h=Healthcare(page) 
      h.healthcare_options()
      page.wait_for_timeout(5000)


@pytest.mark.smoke
def test_fintech(page):
      f=Fintech(page) 
      f.fintech_options()
      page.wait_for_timeout(5000) 

@pytest.mark.smoke
def test_customapp(page):
      c=CustomApp(page) 
      c.customapp_options() 
      page.wait_for_timeout(5000)       


