from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):

    locator_header_order_button = (By.XPATH, './/button[@class="Button_Button__ra12g" and text() = "Заказать"]')
    locator_name_field = (By.XPATH, './/input[@placeholder="* Имя"]')
    locator_surname_field = (By.XPATH, './/input[@placeholder="* Фамилия"]')
    locator_adress_field = (By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]')
    locator_metrostation_field = (By.XPATH, './/input[@placeholder="* Станция метро"]')
    locator_phone_field = (By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]')
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
    locator_metro_station_choice = (By.XPATH, './/div[@class="select-search__select"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Заполнить поле Имя')
    def fill_in_name_field(self, text):
        return self.find_page(self.locator_name_field).send_keys(text)

    @allure.step('Заполнить поле Фамилия')
    def fill_in_surname_field(self, text):
        return self.find_page(self.locator_surname_field).send_keys(text)

    @allure.step('Заполнить поле Адрес')
    def fill_in_adress_field(self, text):
        return self.find_page(self.locator_adress_field).send_keys(text)

    @allure.step('Заполнить поле Телефон')
    def fill_in_phone_field(self, text):
        return self.find_page(self.locator_phone_field).send_keys(text)

    @allure.step('Заполнить поле Комментарий')
    def fill_in_comment_field(self, text):
        return self.find_page(self.locator_comment_field).send_keys(text)

    @allure.step('Кликнуть по полю Станция метро')
    def click_metro_station_field(self):
        return self.click_page(self.locator_metrostation_field)

    @allure.step('Выбрать станцию метро')
    def choose_metro_station(self):
        return self.click_page(self.locator_metro_station_choice)

    @allure.step('Заполнить поле Станция метро')
    def fill_in_metro_station(self, text):
        return self.find_page(self.locator_metrostation_field).send_keys(text)

    @allure.step('Кликнуть на кнопку Далее')
    def click_next_button(self):
        return self.click_page(self.locator_next_button)

    @allure.step('Кликнуть на поле Когда привезти самокат')
    def click_delivery_date_field(self):
        return self.click_page(self.locator_when_to_deliver_field)

    @allure.step('Выбрать дату')
    def choose_delivery_date(self):
        return self.click_page(self.locator_day_choice)

    @allure.step('Кликнуть на поле Срок аренды')
    def click_time_of_lease_field(self):
        return self.click_page(self.locator_time_of_lease_field)

    @allure.step('Ввбрать срок аренды: сутки')
    def choose_time_of_lease_one_day(self):
        return self.click_page(self.locator_time_of_lease_choice_one_day)

    @allure.step('Выбрать цвет самоката')
    def choose_scooter_color(self, *locator):
        return self.click_page(locator)

    @allure.step('Кликнуть на кнопку Заказать')
    def click_final_order_button(self):
        return self.click_page(self.locator_order_button)

    @allure.step('Кликнуть на кнопку "Вы уверены? - Да"')
    def click_are_you_sure_yes_button(self):
        return self.click_page(self.locator_are_you_sure_yes_button)

    @allure.step('Найти кнопку Посмотреть статус')
    def find_show_status_button(self):
        return self.find_page(self.locator_show_status_button)







