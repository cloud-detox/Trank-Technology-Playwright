import pytest

from pages.ecommerceDevelopment import ecommerceDevelopment
from pages.technologiespage import TechnologiesPage
from pages.MobileAppDevelopment import mobileAppDevelopment

# @pytest.mark.smoke
# def test_technologies(page):
#       t=TechnologiesPage(page) 
#       t.technologies_options() 
#       page.wait_for_timeout(5000)

@pytest.mark.smoke
def test_ecommerce(page):
      m=ecommerceDevelopment(page)
      m.ecommerce_options()
      page.wait_for_timeout(5000)

@pytest.mark.smoke
def test_mobileapp(page):     
      m=mobileAppDevelopment(page)
      m.mobile_options()
      page.wait_for_timeout(5000)