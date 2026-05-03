

import pytest
from config import BASE_URL

from pages.technologypage import technology


@pytest.mark.smoke
def test_technology_page(page):
    obj2 = technology(page)
    obj2.ecommercedevelopment_hover()

@pytest.mark.smoke
def test_mobile(page):
    obj2 = technology(page)
    obj2.mobile_hover()

@pytest.mark.smoke
def test_ai(page):
    obj2 = technology(page)
    obj2.artificial_intelligence_hover()