import pytest
from pages.technilogies_menu_base import TechnologiesMenuBase
from utils.csv_data_loader import CSVDataLoader

@pytest.mark.smoke
def test_custom_app_navigation(page):
    expected_titles = CSVDataLoader.load_expected_titles("testdata/custom_app.csv")

    TechnologiesMenuBase(page).click_all_links(expected_titles)
