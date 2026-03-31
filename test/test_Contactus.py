import pytest

from pages.Contactus import ContactUs

@pytest.mark.smoke
def test_contactus(page):
      c = ContactUs(page)
      c.contactus.click()
      page.wait_for_timeout(5000)
      c.fill_details(
            name="Pankaj",
            company="S&P Global",
            service="Web Development",
            phone="1234567890",
            message="Hello, I need your services."
      )
      page.wait_for_timeout(3000)
      c.click_captcha()
      page.wait_for_timeout(3000)
      c.submit.click(force=True)
      page.wait_for_timeout(5000)
