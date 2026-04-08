import pytest

from pages.aboutus import AboutPage

@pytest.mark.smoke
def test_aboutus(page):

    i=AboutPage(page)
    i.aboutusoption_clicking()
    page.wait_for_timeout(3000)