from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, then, when
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep




@given('Open main page https://soft.reelly.io/sign-in')
def open_main_page(context):
    context.app.MainPage.open_main_page()
    sleep(2)

@when('Log in to the page')
def log_in_to_the_page(context):
         context.app.LoginPage.log_in()
         sleep(2)

@when('Click on settings option')
def click_on_settings(context):
    context.app.SettingsPage.verify_settings_page()
    sleep(2)


@when('Verify the right page opens')
def verify_right_page(context):
    context.app.SettingsPage.verify_settings_pge_open()
    sleep(2)

@then('Verify there are 13 options for the settings')
def verify_options_settings_pge(context):
    context.app.SettingsPage.verify_settings_page()

@then('Verify “connect the company” button is available')
def verify_connect_the_company_button(context):
    context.app.SettingsPage.verify_connect_to_company_btn()