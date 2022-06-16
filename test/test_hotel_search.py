from src.page_object.pages.search_hotels import SearchHotelForm
from src.page_object.locators import SearchResultsLocators


def test_hotel_search(web_driver):
    search_hotel = SearchHotelForm(web_driver)
    search_hotel.open_page()
    search_hotel.set_destination("Warsaw")
    search_hotel.set_date_range("29/12/2019", "03/01/2020")
    search_hotel.set_adults_number(3)
    search_hotel.set_kids_number(0)
    search_hotel.search_perform()

    results_title = "Warsaw"
    assert results_title in web_driver.find_element(
        *SearchResultsLocators.search_title).text


