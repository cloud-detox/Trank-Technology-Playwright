import pytest
from pages.get_free_quote_page import Get_Free_Quote_page_class
#from utils.csv_data_loader import CSVDataLoader

@pytest.mark.smoke
def test_get_free_quote(page):
    #expected_titles = CSVDataLoader.load_expected_titles("testdata/contact_us.csv")

    free_quote=Get_Free_Quote_page_class(page)
    free_quote.get_free_quote()