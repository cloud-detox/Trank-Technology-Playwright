import pytest
from config import url
from pages.verticals_page import VerticalsPage
from pages.aboutUs_page import aboutUs
from pages.blog_page import blog
from pages.contactUs_pages import contactUs
from pages.getFreeQuotes_page import getFreeQuotes
from pages.portfolio_page import PortfolioPage
from pages.technologies_page import TechnologiesPage

@pytest.mark.smoke
def test_verticals(page):
    obj = VerticalsPage(page)
    obj.vertical_hover()
    obj.open_verticalspage()

@pytest.mark.smoke
def test_aboutUs(page):
    obj = aboutUs(page)
    obj.aboutUs_hover()
    obj.open_aboutUs_page()

@pytest.mark.smoke
def test_blog(page):
    obj = blog(page)
    obj.blog_hover()
    obj.open_blog_page()

@pytest.mark.smoke
def test_contactUs(page):
    obj = contactUs(page)
    obj.contactUs_hover()
    obj.open_contactUs_page()

@pytest.mark.smoke
def test_portfolio(page):
    obj = PortfolioPage(page)
    obj.portfolio_hover()
    obj.open_portfolio_page()

@pytest.mark.smoke
def test_technologies(page):
    obj = TechnologiesPage(page)
    obj.technologies_hover()
    obj.open_technologies_page()

@pytest.mark.smoke
def test_getFreeQuotes(page):
    obj = getFreeQuotes(page)
    obj.getFreeQuotes_hover()
    obj.open_getFreeQuotes_page()