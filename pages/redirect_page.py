from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class RedirectPage(BasePage):

    locator_scooter_logo = (By.XPATH, './/img[@alt="Scooter"]')
    locator_yandex_logo = (By.XPATH, './/img[@alt="Yandex"]')
    locator_logo_dzen = (By.XPATH, './/svg[@class="desktop-base-header__logoBrand-3W desktop-base-header__isMorda-mX"]')
    locator_dzen_find_button = (By.XPATH, './/button[@type="submit" and text() = "Найти"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Кликнуть на логотип Яндекса')
    def click_yandex_logo(self):
        return self.click_page(self.locator_yandex_logo)

    @allure.step('Кликнуть на логотип Самоката')
    def click_scooter_logo(self):
        return self.click_page(self.locator_scooter_logo)



