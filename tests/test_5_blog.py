import pytest

from pages.blogpage import BlogPage

@pytest.mark.smoke
def test_blog(page):
    obj = BlogPage(page)
    obj.click_blog_again()