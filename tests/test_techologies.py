

import pytest

from pages.techolologies_page import TechnologiesPage
'''
@pytest.mark.smoke
def test_technogies_menu(page):
    tech=TechnologiesPage(page)
    tech.open_technologies()
    '''
@pytest.mark.smoke
def test_ecomdev(page):
    tech=TechnologiesPage(page)
    tech.ecom_dev_clickig()
    tech.mobileapp_clicking()
    tech.artificialintel_clicking()

# @pytest.mark.smoke
# def test_mobileappdev(page):
#     tech=TechnologiesPage(page)
#     #tech.mobile_app_hover()
#     tech.mobileapp_clicking()

# def test_artificialintel(page):
#     tech=TechnologiesPage(page)
#     #tech.artificialintel_hover()
#     tech.artificialintel_clicking()
    
    
   





    