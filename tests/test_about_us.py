import pytest
from pages.About_us import About_us




@pytest.mark.smoke
def test_aboutus(page):
    abt=About_us(page)
    abt.about_us_click()

    