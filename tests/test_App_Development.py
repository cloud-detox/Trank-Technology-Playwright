import pytest
from pages.appdev_page import Appdev

@pytest.mark.smoke
def test_appdevelopment(page):
    ap=Appdev(page)
    ap.ios_clicking()
    ap.android_clicking()
    ap.hyb_click()
    ap.crs_click()
    ap.prg_clicking()