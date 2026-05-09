import pytest

from pages.about_us_page import aboutUs_page

@pytest.mark.smoke
def test_about_us_page(page):
    obj = aboutUs_page(page)
    obj.about_us_hover()

@pytest.mark.smoke
def test_about_us_web_dev_menu(page):
    obj = aboutUs_page(page)
    obj.about_us_web_dev_menu_clicking()

@pytest.mark.smoke
def test_about_us_app_dev_menu(page):
    obj = aboutUs_page(page)
    obj.about_us_app_dev_menu_clicking()

@pytest.mark.smoke
def test_about_us_graphic_design_menu(page):
    obj = aboutUs_page(page)
    obj.about_us_graphic_design_menu_clicking()

@pytest.mark.smoke
def test_about_us_ui_ux_design_menu(page):
    obj = aboutUs_page(page)
    obj.about_us_ui_ux_design_menu_clicking()