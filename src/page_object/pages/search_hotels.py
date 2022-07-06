from data.locators import SearchHotelsFormLocators
from lib.pages_utilities import set_travellers_number


class SearchHotelForm:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("http://www.phptravels.net/")

    def set_destination(self, destination):
        self.driver.find_element(*SearchHotelsFormLocators.destination_inactive).click()
        self.driver.find_element(*SearchHotelsFormLocators.destination_input).send_keys(destination)
        self.driver.find_element(*SearchHotelsFormLocators.search_match).click()

    def set_date_range(self, check_in, check_out):
        self.driver.find_element(*SearchHotelsFormLocators.checkin_input).click()
        self.driver.find_element(*SearchHotelsFormLocators.checkin_input).send_keys(check_in)
        self.driver.find_element(*SearchHotelsFormLocators.checkout_input).click()
        self.driver.find_element(*SearchHotelsFormLocators.checkout_input).send_keys(check_out)

    def set_adults_number(self, adults_num):
        set_travellers_number(self.driver, adults_num, SearchHotelsFormLocators,
                              ["adults_input_value", "adults_add", "adults_sub"])


    def set_kids_number(self, kids_num):
        set_travellers_number(self.driver, kids_num, SearchHotelsFormLocators,
                              ["kids_input_value", "kids_add", "kids_sub"])

    def search_perform(self):
        self.driver.find_element(*SearchHotelsFormLocators.search_btn).click()