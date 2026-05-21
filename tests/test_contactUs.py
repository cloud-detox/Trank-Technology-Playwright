from playwright.sync_api._generated import Page
import pytest

from pages.Contactus import ContactUs

@pytest.mark.smoke
def test_contact_us_form(page: Page):
    contact_us = ContactUs(page)
    contact_us.fill_contact_form("John Doe", "john@example.com", "Example Inc.", "Web Development", "Hello, this is a test message.")
    contact_us.submit_form()

@pytest.mark.smoke
def test_contact_us_links(page: Page):
    contact_us = ContactUs(page)
    contact_us.contactus_click()

@pytest.mark.smoke
def test_appdev_links(page: Page):
    contact_us = ContactUs(page)
    contact_us.appdev_click()

@pytest.mark.smoke
def test_graphic_links(page: Page):
    contact_us = ContactUs(page)
    contact_us.graphic_click()  

