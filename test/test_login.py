from src.page_object.pages.login import LogInPage
from src.page_object.locators import UserAccountLocators


def test_login(web_driver):
    def test_login_passed(self):
        log_in_page = LogInPage(self.driver)
        log_in_page.open()
        log_in_page.expand_account_menu()
        log_in_page.open_login_page()
        log_in_page.set_user_inputs("user@phptravels.com", "demouser")
        welcome_msg = "Hi, Demo User"
        assert welcome_msg in self.driver.find_element(
            *UserAccountLocators.welcome_msg).text
        log_in_page.expand_account_menu()
        log_in_page.logout()
