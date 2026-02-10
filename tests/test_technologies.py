import pytest
from pages.technilogies_menu_base import TechnologiesMenuBase
from utils.csv_data_loader import CSVDataLoader

@pytest.mark.smoke
def test_ECommerceAndDevelopment(page):
    expected_titles = CSVDataLoader.load_expected_titles("testdata/custom_app.csv")

    tech_menu=TechnologiesMenuBase(page,"eCommerce Development","ecomm")
    tech_menu.click_all_pages(expected_titles)


@pytest.mark.mob
def test_MobileAppAndDevelopment(page):
    expected_titles = CSVDataLoader.load_expected_titles("testdata/custom_app.csv")

    tech_menu=TechnologiesMenuBase(page,"Mobile App Development","mobileApp")
    tech_menu.click_all_pages(expected_titles)

# @pytest.mark.ai
# def test_aitest(page):
#     #expected_titles = CSVDataLoader.load_expected_titles("testdata/custom_app.csv")

#     ai_menu=TechnologiesMenuBase(page,)
#     ai_menu.ai()