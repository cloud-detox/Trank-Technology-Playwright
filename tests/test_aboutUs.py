import pytest
from pages.AboutUs_page import aboutUs

@pytest.mark.aboutUs
def test_aboutUs(page):
    obj_aboutUs = aboutUs(page)
    obj_aboutUs.aboutUs_Click()
     