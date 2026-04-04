import pytest
from pages.UIUX import UIUX

@pytest.mark.smoke
def test_UIUX(page):
    ui=UIUX(page)
    ui.UIUX_clicking()