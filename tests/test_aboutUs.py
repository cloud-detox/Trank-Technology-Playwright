import pytest
from pages.aboutUs_page import AbourUs
from utils.csv_data_loader import CSVDataLoader

@pytest.mark.smoke
def test_AboutUs(page):
    expected_titles = CSVDataLoader.load_expected_titles("testdata/aboutUs.csv")

    abpout_menu=AbourUs(page)
    abpout_menu.click_about(expected_titles) 