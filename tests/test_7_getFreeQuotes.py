import pytest

from pages.getFreeQoutes_page import GetFreeQoutesPage

@pytest.mark.smoke
def test_getfreeqoutes_button(page):
    getfreeqoutes=GetFreeQoutesPage(page)
    getfreeqoutes.free_qoutes_form()
    getfreeqoutes.page.wait_for_timeout(6000)
