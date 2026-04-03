import pytest
from pages.UI_UX_Design import UI_UX_Design

@pytest.mark.smoke
def test_UI_UX_Design(page):
    UX=UI_UX_Design(page)
    UX.UI_UX_Design_click()