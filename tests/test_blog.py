import pytest
from pages.blog_page import blog_page

@pytest.mark.order(4)
def test_Blog(page):
    obj_Blog = blog_page(page)
    obj_Blog.blog_Click()
    obj_Blog.searchFunc()