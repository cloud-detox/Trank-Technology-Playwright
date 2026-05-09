

import pytest

from pages.aboutUs_page import AboutUsPage

@pytest.mark.smoke
def test_aboutUs_menu(page):
    aboutus=AboutUsPage(page)
    #aboutus.open_about_us()
    aboutus.webDevelopment_menus_clicking()
    aboutus.appDevloment_menus_clicking()
    aboutus.graphicDesign_menus_clicking()
    aboutus.followUs_menus_clicking()
    

    

