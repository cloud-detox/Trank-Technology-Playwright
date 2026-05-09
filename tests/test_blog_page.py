import pytest
from pages.blog_page import blog_page

@pytest.mark.smoke
def test_blog_page_navigation(page):
    obj = blog_page(page)
    # Test blog menu hovering
    obj.blog_menu_clicking()

@pytest.mark.smoke
def test_blog_categories_navigation(page):
    obj = blog_page(page)
    # Test clicking on each blog category
    obj.blog_categories_clicking()
