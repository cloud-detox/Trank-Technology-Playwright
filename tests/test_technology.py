import pytest

from pages.commerce import CommercePage
from pages.mobileapp import MobilePage
from pages.technology import technology


@pytest.mark.smoke
def test_technology(page):

    t=CommercePage(page)
    t.commerceoption_clicking()
    page.wait_for_timeout(3000)

    m=MobilePage(page)
    m.mobileoption_clicking()
    page.wait_for_timeout(3000)