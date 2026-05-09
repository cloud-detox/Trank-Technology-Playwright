

import pytest

from pages.blog_page import BlogPage

@pytest.mark.smoke
def test_blog_menu(page):
    blog=BlogPage(page)
    blog.open_blog()

    