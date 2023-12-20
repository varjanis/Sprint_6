from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):
    locator_header_order_button = (By.XPATH, './/button[@class="Button_Button__ra12g" and text() = "Заказать"]')
    locator_page_order_button = (By.XPATH,
                                 './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text() = "Заказать"]')
    locator_name_field = (By.XPATH, './/input[@placeholder="* Имя"]')
    locator_surname_field = (By.XPATH, './/input[@placeholder="* Фамилия"]')
    locator_adress_field = (By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]')
    locator_metrostation_field = (By.XPATH, './/input[@placeholder="* Станция метро"]')
    locator_phone_field = (By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]')
    locator_next_button = (By.XPATH, './/button[text() = "Далее"]')
    locator_when_to_deliver_field = (By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')
    locator_day_choice = (By.XPATH, './/div[@class="react-datepicker__day react-datepicker__day--028"]')
    locator_time_of_lease_field = (By.XPATH, './/div[@class="Dropdown-placeholder" and text() = "* Срок аренды"]')
    locator_time_of_lease_choice_one_day = (By.XPATH, './/div[text() = "сутки"]')
    locator_time_of_lease_choice_two_days = (By.XPATH, './/div[text() = "сутки"]')
    locator_color_choice_field = (By.XPATH, './/div[@class="Order_Title__3EKne" and text() = "Цвет самоката"]')
    locator_color_black_field = (By.XPATH, './/label[text() = "чёрный жемчуг"]')
    locator_color_gray_field = (By.XPATH, './/label[text() = "серая безысходность"]')
    locator_comment_field = (By.XPATH, './/input[@placeholder="Комментарий для курьера"]')
    locator_order_button = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text() = "Заказать"]')
    locator_are_you_sure_yes_button = (By.XPATH, './/button[text() = "Да"]')
    locator_show_status_button = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text() = "Посмотреть статус"]')
    locator_scooter_logo = (By.XPATH, './/img[@alt="Scooter"]')
    locator_yandex_logo = (By.XPATH, './/img[@alt="Yandex"]')
    locator_metro_station_choice = (By.XPATH, './/div[@class="select-search__select"]')
    locator_logo_dzen = (By.XPATH, './/svg[@class="desktop-base-header__logoBrand-3W desktop-base-header__isMorda-mX"]')
    locator_dzen_find_button = (By.XPATH, './/button[@type="submit" and text() = "Найти"]')

    def click_header_order_button(self, driver):
        return driver.find_element(*self.locator_header_order_button).click()

    def fill_in_name_field(self, driver, text):
        return driver.find_element(*self.locator_name_field).send_keys(text)

    def fill_in_surname_field(self, driver, text):
        return driver.find_element(*self.locator_surname_field).send_keys(text)

    def fill_in_adress_field(self, driver, text):
        return driver.find_element(*self.locator_adress_field).send_keys(text)

    def fill_in_phone_field(self, driver, text):
        return driver.find_element(*self.locator_phone_field).send_keys(text)

    def fill_in_comment_field(self, driver, text):
        return driver.find_element(*self.locator_comment_field).send_keys(text)

    def click_metro_station_field(self, driver):
        return driver.find_element(*self.locator_metrostation_field).click()

    def choose_metro_station(self, driver):
        return driver.find_element(*self.locator_metro_station_choice).click()

    def fill_in_metro_station(self, driver, text):
        return driver.find_element(*self.locator_metrostation_field).send_keys(text)

    def click_next_button(self, driver):
        return driver.find_element(*self.locator_next_button).click()

    def click_delivery_date_field(self, driver):
        return driver.find_element(*self.locator_when_to_deliver_field).click()

    def choose_delivery_date(self, driver):
        return driver.find_element(*self.locator_day_choice).click()

    def click_time_of_lease_field(self, driver):
        return driver.find_element(*self.locator_time_of_lease_field).click()

    def choose_time_of_lease_one_day(self, driver):
        return driver.find_element(*self.locator_time_of_lease_choice_one_day).click()

    def choose_scooter_color(self, driver, *locator):
        return driver.find_element(*locator).click()

    def click_final_order_button(self, driver):
        return driver.find_element(*self.locator_order_button).click()

    def click_are_you_sure_yes_button(self, driver):
        return driver.find_element(*self.locator_are_you_sure_yes_button).click()

    def click_yandex_logo(self, driver):
        return driver.find_element(*self.locator_yandex_logo).click()

    def click_scooter_logo(self, driver):
        return driver.find_element(*self.locator_scooter_logo).click()







