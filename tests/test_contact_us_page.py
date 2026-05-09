import pytest

from pages.contact_us_page import contact_us_page

@pytest.mark.smoke

def test_contact_us(page):
    obj = contact_us_page(page)
    obj.contact_us_hover()
    obj.contact_us_form()


