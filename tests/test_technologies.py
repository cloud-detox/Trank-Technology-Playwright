import pytest

from pages.technologies_sub_menu import technologies_sub_menu

@pytest.mark.smoke

def test_technologies(page):
    t=technologies_sub_menu(page)
    t.technologies_clicking()
    t.eComdev_clicking()
    t.mobileapp_clicking()
    t.artificial_clicking()
   
    page.wait_for_timeout(5000)
    