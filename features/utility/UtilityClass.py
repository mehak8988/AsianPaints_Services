from selenium import webdriver
from features.utility.ConfigClass import ConfigClass
from selenium.webdriver.chrome.options import Options

class UtilityClass:

    def _init_(self, driver):
        self.driver = driver

    def launch_browser(self):
        self.driver = webdriver.Chrome(ConfigClass.filePath)

    def launch_browser_notification(self):
        chromeOptions = Options()

        chromeOptions.add_argument("--disable-notifications")

        self.driver = webdriver.Chrome(ConfigClass.filePath, chrome_options=chromeOptions)

    def browser_maximise(self):
            self.driver.maximize_window()

    def launch_app(self):
        self.driver.get(ConfigClass.url)

    def close_browser(self):
        self.driver.quit()


