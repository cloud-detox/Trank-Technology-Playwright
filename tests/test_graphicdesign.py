import pytest
from pages.Graphicdesign import Graphicdesign

@pytest.mark.smoke
def test_graphicdesign(page):
    gr=Graphicdesign(page)
    gr.graphicdesign_clicking()
    