import pytest
from pages.contactUs_page import Contact_Us_page_class
from utils.csv_data_loader import CSVDataLoader

@pytest.mark.smoke
def test_ContactUs(page):
    expected_titles = CSVDataLoader.load_expected_titles("testdata/contact_us.csv")

    abpout_menu=Contact_Us_page_class(page)
    abpout_menu.click_ContactUs(expected_titles) 