from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class MainMenuPage(BasePage):
    MAIN_MENU = (By.XPATH, '//a[@href="/main-menu"]')

    def click_on_main_menu(self, *locator):
        elements = self.driver.find_elements(*self.MAIN_MENU)
        elements[1].click()
