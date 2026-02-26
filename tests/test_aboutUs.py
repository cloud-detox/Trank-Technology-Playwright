import pytest 

from pages.aboutus_page import aboutus

@pytest.mark.about
def aboutus_page(page):
    aboutus_obj = aboutus(page)
    aboutus_obj.aboutus_click()