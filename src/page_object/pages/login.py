from src.page_object.locators import LogInLocators
from selenium.webdriver.common.keys import Keys


class LogInPage:
    def __init__(self, driver):
        self.driver = driver

    def expand_account_menu(self):
        self.driver.find_element(*LogInLocators.user_account_menu).click()

    def open_login_page(self):
        self.driver.find_element(*LogInLocators.login_link).click()

    def set_user_inputs(self, email, password):
        self.driver.find_element(*LogInLocators.email_input).click()
        self.driver.find_element(*LogInLocators.email_input).send_keys(email)
        self.driver.find_element(*LogInLocators.password_input).click()
        self.driver.find_element(
            *LogInLocators.password_input).send_keys(password, Keys.ENTER)

    def logout(self):
        self.driver.find_element(*LogInLocators.logout_link).click()