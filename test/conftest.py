from src.test_base.utils import driver_setup
import pytest


@pytest.fixture()
def web_driver(request):
    driver = driver_setup()
    yield driver
    driver.close()
    driver.quit()
