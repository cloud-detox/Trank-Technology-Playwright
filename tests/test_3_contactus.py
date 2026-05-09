import pytest

from pages.contactus_page import ContactusPage

@pytest.mark.smoke
def test_contactus(page):
    obj = ContactusPage(page)
    obj.contact_method()