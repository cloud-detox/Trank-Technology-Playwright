import pytest
from pages.Aboutus import Aboutus

@pytest.mark.smoke
def test_Aboutus(page):
    ab=Aboutus(page)
    ab.Aboutus_clicking()