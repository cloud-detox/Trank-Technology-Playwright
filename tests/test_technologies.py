import pytest

from pages.technologies_locator import technologies

@pytest.mark.smoke
def test_Tech(page):
    techObj=technologies(page)
    #techObj.clickAllEcommOptions()
    techObj.mobileAppDev_Click()
    techObj.ai_Click()

   
   
    