from selenium import webdriver
from fixture.session import SessionHelper
from fixture.login import LoginHelper
from fixture.report import ReportHelper
from fixture.ResultAndPrizes import ResultAndPrizeHelper
from fixture.messages import MessageID
from fixture.utiliz import UtilizHelper


class Application:

    def __init__(self, browser, base_url, executor):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
#            chrome_options = webdriver.ChromeOptions()
#            chrome_options.add_argument('start-fullscreen')
#            self.wd = webdriver.Chrome(options=chrome_options)
            self.wd = webdriver.Remote(
                command_executor=f"http://{executor}:4444/wd/hub",
                desired_capabilities={"browserName": browser}
            )
            self.wd.maximize_window()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecoqnized browser %s" % browser)
        self.wd.implicitly_wait(7)
        self.session = SessionHelper(self)
        self.login = LoginHelper(self)
        self.report = ReportHelper(self)
        self.ResultAndPrizes = ResultAndPrizeHelper(self)
        self.messages = MessageID(self)
        self.base_url = base_url
        self.utiliz = UtilizHelper(self)


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)


    def destroy(self):
        self.wd.quit()