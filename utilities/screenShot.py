import datetime

class takeScrnsht():
    def __init__(self, page, modName):
        self.page = page
        self.modName = modName
        page.wait_for_load_state()
        timeStamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        page.screenshot(path=f"testResults//{timeStamp}_{modName}.png")
        