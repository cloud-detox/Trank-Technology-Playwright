import pytest
from conftest import page
from pages.aboutus import aboutus
from pages.blog import blog 
from pages.contactus import contactus
from pages.portfolio import portfolio
from pages.artiint import artiint
from pages.ecomdev import ecomdev
from pages.mobappdev import mobappdev
from pages.technologies import technologies


@pytest.mark.smoke
def test_technologies(page):
    t = technologies(page)
    t.technologies_hover()
    page.wait_for_timeout(2000)

@pytest.mark.smoke
def test_ecomdev(page):
     e = ecomdev(page)
     e.ecomdev_clicking()

@pytest.mark.smoke
def test_mobappdev(page):
     m = mobappdev(page)
     m.mobappdev_clicking()   

@pytest.mark.smoke
def test_artiint(page):
     a = artiint(page)
     a.artiint_clicking()
 
@pytest.mark.smoke
def test_aboutus(page):
    b = aboutus(page)
    b.aboutus_clicking()

@pytest.mark.smoke
def test_blog(page):
    bl = blog(page)
    bl.blog_clicking()    

@pytest.mark.smoke
def test_contactus(page):
    c = contactus(page)
    c.contactus_filling()    

@pytest.mark.smoke
def test_portfolio(page):
    p = portfolio(page)
    p.portfolio_clicking()

