import pytest
from pages.contactUs_page import contactUs

@pytest.mark.order(5)
def test_ContactUs(page):
    contactUs_obj = contactUs(page)
    contactUs_obj.contactUs_Click()
    contactUs_obj.fillConsultationForm()
    