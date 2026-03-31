import pytest

from pages.AboutUspage import Aboutus

@pytest.mark.smoke
def test_aboutus(page):
      a=Aboutus(page)
      a.aboutus.click()
      page.wait_for_timeout(5000)
