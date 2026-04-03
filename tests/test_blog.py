import pytest
from pages.Blog import Blog

@pytest.mark.smoke
def test_blog(page):
    b=Blog(page)
    b.Blog_click()