

import pytest

from config import BASE_URL
from pages.contactpage import contact

@pytest.mark.smoke
def test_contactus(page):
    obj4 = contact(page)
    obj4.contact_method()
    