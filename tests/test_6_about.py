import pytest

from pages.aboutuspage import AboutPage

@pytest.mark.smoke
def test_about(page):
    aboutus=AboutPage(page)
    #aboutus.open_about_us()
    aboutus.webDevelopment_menus_clicking()
    aboutus.appDevloment_menus_clicking()
    aboutus.graphicDesign_menus_clicking()
    aboutus.followUs_menus_clicking()
    
