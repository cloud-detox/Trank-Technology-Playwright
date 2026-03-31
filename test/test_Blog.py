import pytest

from pages.Blogpage import blogpage

@pytest.mark.smoke
def test_blog(page):
      b=blogpage(page)
      b.blog.click()
      page.wait_for_timeout(5000)
