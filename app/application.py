from Pages.base_page import BasePage
from Pages.main_page import MainPage
from Pages.log_in_page import LoginPage
from Pages.settings_page import SettingsPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.MainPage = MainPage(driver)
        self.LoginPage = LoginPage(driver)
        self.SettingsPage = SettingsPage(driver)




