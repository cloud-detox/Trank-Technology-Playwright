import pytest
from pages.webdevelopment import webdevelopment

@pytest.mark.smoke
def test_webdevelopment(page):
    we=webdevelopment(page)
    we.cms_clicking()
    we.ecomdec_clicking()
    we.custom_clicking()

    