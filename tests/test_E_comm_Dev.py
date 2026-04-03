import pytest
from pages.E_comm_Dev import E_comm_Dev


@pytest.mark.smoke
def test_E_comm_Dev(page):
    ECD=E_comm_Dev(page)
    
    ECD.CMS_Web_click()
    ECD.E_comm_Dev_click()
    ECD.Custom_Webportal_click()
    