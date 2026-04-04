import pytest
from pages.blog import blog

@pytest.mark.smoke
def test_blog(page):
    bl=blog(page)
    bl.blog_clicking()
