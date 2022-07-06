from src.page_object.pages.login import LogInPage
from data.locators import UserAccountLocators
import logging

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s -  %(message)s')


def test_login(web_driver):
    logging.info('Start of test case: test_login')
    log_in_page = LogInPage(web_driver)
    log_in_page.open_login_page()
    log_in_page.expand_account_menu()
    log_in_page.open_login_page()
    log_in_page.set_user_inputs("user@phptravels.com", "demouser")
    welcome_msg = "Hi, Demo User"
    assert welcome_msg in web_driver.find_element(*UserAccountLocators.welcome_msg).text
    log_in_page.expand_account_menu()
    log_in_page.logout()
    logging.info('End of test case: test_login')
