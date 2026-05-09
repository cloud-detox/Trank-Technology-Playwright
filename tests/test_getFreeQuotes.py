

import pytest

from pages.getFreeQoutes_page import GetFreeQoutesPage

@pytest.mark.smoke
def test_getfreeqoutes_menu(page):
    getfreeqoutes=GetFreeQoutesPage(page)
    getfreeqoutes.fill_get_free_qoutes_form()