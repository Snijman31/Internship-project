from Pages.base_page import BasePage


class MainPage(BasePage):

    def open_main_page(self):
        self.open_url('https://soft.reelly.io/sign-in')
