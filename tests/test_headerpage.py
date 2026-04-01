import pytest

from pages.header_page import Header_Page

@pytest.mark.smoke
def test_headerlink(page):
    h=Header_Page(page)
    h.clickaboutpage()
    h.clickblogpage()
    h.clickcontactus()
    h.clickportfolio()
    page.wait_for_timeout(3000)