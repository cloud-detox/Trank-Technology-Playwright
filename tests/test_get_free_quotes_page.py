import pytest

from pages.get_free_quotes_page import GetFreeQuotesPage

@pytest.mark.smoke
def test_get_free_quotes_page(page):
    get_free_quotes_page = GetFreeQuotesPage(page)
    get_free_quotes_page.get_free_quote_menu_clicking()

@pytest.mark.smoke
def test_get_free_quote_form_filling(page):
    get_free_quotes_page = GetFreeQuotesPage(page)
    get_free_quotes_page.get_free_quote_form_filling('Navyashree', 'navyashree.cd@gmail.com', 123456, 'Trank Technologies', 'Web Development', '9876543210', 'This is a test message.')