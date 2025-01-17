

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element_by_id('username').send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('password').send_keys(password)

    def click_login_button(self):
        self.driver.find_element('login').click()

    def find_element(self, locator):
         self.driver.find_element(*locator)

    def find_elements(self,* locator):
         self.driver.find_elements(*locator)

    def click(self, locator):
        self.driver.find_element(*locator).click()