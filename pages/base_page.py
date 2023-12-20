from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class BasePage:

    locator_base_url = 'https://qa-scooter.praktikum-services.ru/'
    locator_order_page_url = 'https://qa-scooter.praktikum-services.ru/order'
    locator_cookie_consent_button = (By.XPATH, './/button[@class="App_CookieButton__3cvqF" and text() = "да все привыкли"]')

    def open_base_url(self, driver):
        return driver.get(self.locator_base_url)

    def wait_until_element_is_visible(self, driver, locator):
        return WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(locator))

    def wait_until_element_is_clickable(self, driver, locator):
        return WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    def click_cookie_consent(self, driver):
        return driver.find_element(*self.locator_cookie_consent_button).click()




