from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (By.XPATH,'//*[@id="email-2"]')
    PASSWORD = (By.XPATH, '//*[@id="field"]')
    CLICK_LOG_BTN = (By.CSS_SELECTOR, '.login-button.w-button')
    def log_in(self,):
        self.driver.find_element(*self.USERNAME).send_keys('nijmansarahann+test+@icloud.com')
        self.driver.find_element(*self.PASSWORD).send_keys('Silas22!')
        self.driver.find_element(*self.CLICK_LOG_BTN).click()