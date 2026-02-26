import pytest
from pages.blog_page import blog_page

@pytest.mark.blog
def test_Blog(page):
    obj_Blog = blog_page(page)
    obj_Blog.blog_Click()