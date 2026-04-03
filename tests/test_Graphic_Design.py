import pytest
from pages.Graphic_Design import Graphic_Design

@pytest.mark.smoke
def test_Graphic_Design(page):
    GD=Graphic_Design(page)
    GD.Graphic_Design_click()