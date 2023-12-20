import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

DRIVER_PATH = '../geckodriver'

@pytest.fixture(scope='function')
def driver():

    service = Service(executable_path=DRIVER_PATH)
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(service=service, options=options)

    yield driver
    driver.quit()
