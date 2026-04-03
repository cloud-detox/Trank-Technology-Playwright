import pytest
from pages.Contact_us import Contact_us


@pytest.mark.smoke
def test_contact_us(page):
    c=Contact_us(page)
    c.Contact_us_click()