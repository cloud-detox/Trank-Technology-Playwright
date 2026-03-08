import datetime
from conftest import page

class takeScrnsht():
    def __init__(self, page, modName):
        page.wait_for_load_state()
        timeStamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        page.screenshot(path=f"testResults//{modName}_{timeStamp}.png")