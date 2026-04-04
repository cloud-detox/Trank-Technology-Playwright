import pytest
from pages.ecomm import ecommD
from pages.mobDev import mobDev
from pages.AI import AI
from pages.technologies import technologies

@pytest.mark.smoke
def test_technology(page):
    te=technologies(page)

    ec=ecommD(page)
    ec.ecommD_clicking()

    md=mobDev(page)
    md.mobDev_clicking()

    a=AI(page)
    a.AI_clicking()

