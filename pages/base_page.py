from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import allure


class BasePage:

    locator_base_url = 'https://qa-scooter.praktikum-services.ru/'
    locator_order_page_url = 'https://qa-scooter.praktikum-services.ru/order'
    locator_important_info_block = (By.XPATH, './/div[text() = "Вопросы о важном"]')
    locator_cookie_consent_button = (By.XPATH, './/button[@class="App_CookieButton__3cvqF" and text() = "да все привыкли"]')
    locator_header_order_button = (By.XPATH, './/button[@class="Button_Button__ra12g" and text() = "Заказать"]')
    locator_next_button = (By.XPATH, './/button[text() = "Далее"]')
    locator_page_order_button = (By.XPATH,
                                 './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text() = "Заказать"]')

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть базовый url')
    def open_base_url(self):
        return self.driver.get(self.locator_base_url)

    @allure.step('Показать текущий url')
    def show_current_url(self):
        return self.driver.current_url

    @allure.step('Найти страницу или элемент')
    def find_page(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Кликнуть на страницу или элемент')
    def click_page(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Открыть блок Вопросы о важном')
    def open_important_info_block(self):
        element = self.find_page(self.locator_important_info_block)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Кликнуть по кнопке Заказать в шапке страницы')
    def click_header_order_button(self):
        return self.driver.find_element(*self.locator_header_order_button).click()

    @allure.step('Дождаться загрузки элемента')
    def wait_until_element_is_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))

    @allure.step('Дождаться, чтобы на элемент можно было кликнуть')
    def wait_until_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Принять cookie')
    def click_cookie_consent(self):
        return self.driver.find_element(*self.locator_cookie_consent_button).click()

    @allure.step('Установить новое окно')
    def assert_window(self):
        assert len(self.driver.window_handles) == 1

    @allure.step('Открыть и проверить новое окно')
    def check_window(self):
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break




