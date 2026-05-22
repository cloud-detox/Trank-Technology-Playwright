import pytest
from pages.homepage import homepage

@pytest.mark.smoke
def test_homepage_click(page): 
    homePage=homepage(page)
    homePage.exploreSolu_click()