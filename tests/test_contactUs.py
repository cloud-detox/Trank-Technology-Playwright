import pytest
from pages.contactus import contactus

@pytest.mark.smoke
def test_contactus(page):
    co=contactus(page)
    co.contactus_clicking()
