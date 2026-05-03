

import pytest
from config import BASE_URL

from pages.blogpage import blog

@pytest.mark.smoke
def test_categories_click(page):
    obj3 = blog(page)
    obj3.cat_method()