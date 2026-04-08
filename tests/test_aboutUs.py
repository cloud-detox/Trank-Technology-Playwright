import pytest
from pages.aboutus import AboutUs


@pytest.mark.smoke
def test_aboutus(page):
    about = AboutUs(page)
    about.about_us()