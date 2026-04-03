import pytest
from pages.technologiespage import technologies
from pages.E_comm import E_comm
from pages.Mobile_app import Mobile_app
from pages.AI import AI

@pytest.mark.smoke
def test_technologies(page):
    tech=technologies(page)

    Ec=E_comm(page)
    Ec.E_comm_clicking()

    Mob_app=Mobile_app(page)
    Mob_app.Mobile_app_list_click()

    ai=AI(page)
    ai.AI_click()



