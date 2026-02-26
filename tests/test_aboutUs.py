import pytest
from pages.aboutUs_page import aboutUs

@pytest.mark.order(3)
def test_aboutUs(page):
    obj_aboutUs = aboutUs(page)
    obj_aboutUs.aboutUs_Click()
     