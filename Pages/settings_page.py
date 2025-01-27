from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SettingsPage(BasePage):

    SETTING_PGE = (By.XPATH, "//a[@href='/settings']")
    SETTING_PGE_OPEN = (By.CSS_SELECTOR,'.image-profile-settings')
    SETTING_OPT = (By.CSS_SELECTOR,'.settings-block-menu'"Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Option 6", "Option 7", "Option 8",
                       "Option 9", "Option 10", "Option 11", "Option 12", "Option 13")
    CONNECT_TO_COMPANY =(By.XPATH,'//a[@href="/payment/personal"]')

    def verify_settings_page(self,*locator):
        self.driver.find_element(*self.SETTING_PGE).click()

    def verify_settings_pge_open(self,*locator):
        self.driver.find_element(*self.SETTING_PGE_OPEN)

    def verify_options_settings_pge(self,*locator):
        self.driver.find_element(*self.SETTING_OPT)

    def verify_connect_to_company_btn(self,*locator):
        self.driver.find_element(*self.CONNECT_TO_COMPANY)

