from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SettingsPage(BasePage):

    SETTING_PGE = (By.XPATH,"//div[@class='settings-code w-embed']")
    SETTING_PGE_OPEN = (By.CSS_SELECTOR,'.image-profile-settings')
    SETTING_OPT = (By.XPATH, "//div[@class='settings-block-menu']")
    CONNECT_TO_COMPANY =(By.XPATH,'//a[@href="/payment/personal"]')

    def verify_settings_page(self,*locator):
         self.driver.find_element(*self.SETTING_PGE).click()


    def verify_settings_pge_open(self,*locator):
        self.driver.find_element(*self.SETTING_PGE_OPEN)

    def verify_options_settings_pge(self,*locator):
       elements = self.driver.find_elements(*self.SETTING_OPT)
       assert len(elements) == 1, f"Expected 1 elements, but found {len(elements)}"
       print(f"Verified: {len(elements)} options are available in the settings.")

    def verify_connect_to_company_btn(self,*locator):
        self.driver.find_element(*self.CONNECT_TO_COMPANY)

