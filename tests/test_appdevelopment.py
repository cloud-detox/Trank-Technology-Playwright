import pytest
from pages.AppDevelopment import AppDevelopment

@pytest.mark.smoke
def test_appdevelopment(page):
    ap=AppDevelopment(page)
    ap.ios_clicking()
    ap.andriod_clicking()
    ap.hyb_click()
    ap.crs_clicking()
    ap.prg_clicking()