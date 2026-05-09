

import pytest

from pages.contactUs_page import contactUsPage

@pytest.mark.smoke
def test_contact_menu(page):
    contact=contactUsPage(page)
    contact.fill_contact_form()

