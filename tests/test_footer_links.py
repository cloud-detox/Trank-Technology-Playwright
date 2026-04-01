import pytest

from pages.footer_page import Footer_page 

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

