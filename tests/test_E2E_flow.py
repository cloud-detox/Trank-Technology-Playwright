import pytest

from pages.vertical_sub_menu import vertical_sub_menu
from pages.technologies_sub_menu import technologies_sub_menu
from pages.header_page import Header_Page
from pages.footer_page import Footer_page 

@pytest.mark.smoke

def test_vertical(page):
    t=vertical_sub_menu(page)
    t.tradingoption_clicking()
    t.retail_clicking()
    t.healthcare_clicking()
    t.fintech_clicking()
    t.customerapp_clicking()
    page.wait_for_timeout(1000)

@pytest.mark.smoke

def test_technologies(page):
    t=technologies_sub_menu(page)
    t.technologies_clicking()
    t.eComdev_clicking()
    t.mobileapp_clicking()
    t.artificial_clicking()
    page.wait_for_timeout(1000)

@pytest.mark.smoke

def test_headerlink(page):
    h=Header_Page(page)
    h.clickaboutpage()
    h.clickblogpage()
    h.clickcontactus()
    h.clickportfolio()
    page.wait_for_timeout(1000)
    
@pytest.mark.smoke

def test_footer_links(page):
    f=Footer_page(page)
    f.click_footer_links1()
    f.click_dropdown_option1()
    f.click_footer_links2()
    f.click_dropdown_option2()
    f.click_dropdown_option3()
    f.click_footer_links3()
    f.click_Socialmedia_links()
    page.wait_for_timeout(5000)