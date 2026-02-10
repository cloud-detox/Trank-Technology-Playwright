import pytest
from pages.blog_page import Blog_page_class
from utils.csv_data_loader import CSVDataLoader

@pytest.mark.smoke
def test_blog(page):
    expected_titles = CSVDataLoader.load_expected_titles("testdata/blog.csv")

    abpout_menu=Blog_page_class(page)
    abpout_menu.click_blog(expected_titles)