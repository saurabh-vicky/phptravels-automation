from src.page_object.pages.search_tours import SearchToursForm
import logging

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s -  %(message)s')


def test_search_tour(web_driver):
    logging.info('Start of test case: test_search_tours')
    search_tour = SearchToursForm(web_driver)
    search_tour.open_page()
    search_tour.open_tours_tab()
    search_tour.set_tour_destination("Sheraton Trip")
    search_tour.set_tour_type("Private")
    search_tour.set_date("2022", "July", "5")
    search_tour.set_adults_number(10)
    search_tour.search_perform()
    logging.info('End of test case: test_login')