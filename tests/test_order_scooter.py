import allure
import pytest
from pages.order_page import OrderPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestOrderPage:

    @allure.title('Открыть страницу заказа из хедера')
    @allure.description('Проверка того, что страница заказа открывается по клику на кнопку Заказать в хедере')
    def test_order_from_header(self, driver):
        order_page = OrderPage()
        order_page.open_base_url(driver)
        order_page.click_header_order_button(driver)
        order_page.wait_until_element_is_visible(driver, order_page.locator_next_button)

        assert driver.current_url == order_page.locator_order_page_url

    @allure.title('Открыть страницу заказа из середины страницы')
    @allure.description('Проверка того, что страница заказа открывается по клику на кнопку Заказать в середине страницы')
    def test_order_from_middle_page(self, driver):
        order_page = OrderPage()
        order_page.open_base_url(driver)
        order_page.click_header_order_button(driver)
        order_page.wait_until_element_is_visible(driver, order_page.locator_next_button)

        assert driver.current_url == order_page.locator_order_page_url

    @allure.title('Редирект по клику на логотип Самоката')
    @allure.description('Проверка того, что по клику на логотип Самоката открывается главная страница с лендингом Самоката')
    def test_redirect_from_scooter_logo(self, driver):
        order_page = OrderPage()
        order_page.open_base_url(driver)
        order_page.click_header_order_button(driver)
        order_page.click_scooter_logo(driver)
        order_page.wait_until_element_is_visible(driver, order_page.locator_page_order_button)

        assert driver.current_url == order_page.locator_base_url

    @allure.title('Открыть главную страницу Дзена кликом на логотип Яндекса')
    @allure.description('Проверка того, что при нажатии на логотип Яндекса идёт редирект на главную страницу Дзена')
    def test_redirect_from_yandex_logo(self, driver):
        order_page = OrderPage()
        order_page.open_base_url(driver)
        order_page.click_header_order_button(driver)
        wait = WebDriverWait(driver, 10)
        original_window = driver.current_window_handle
        assert len(driver.window_handles) == 1
        order_page.click_yandex_logo(driver)
        wait.until(expected_conditions.number_of_windows_to_be(2))

        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        order_page.wait_until_element_is_clickable(driver, order_page.locator_dzen_find_button)

        assert driver.current_url == 'https://dzen.ru/?yredirect=true'

    @allure.title('Проверка позитивного сценария заказа самоката с двумя наборами данных')
    @allure.description('Проверка того, что при корректных данных можно успешно сделать заказ на самокат')
    @pytest.mark.parametrize(
     'name, surname, adress, metrostation, phonenumber, comment',
     [
     ['Олег', 'Озерков', 'Потешная 13', 'Бульвар Рокоссовского', '+79269876543', 'коммент 1'],
     ['Илья', 'Лесов', 'Озорная 42', 'Славянский бульвар', '+79269878965', 'коммент 2'],
     ]
     )
    def test_order_successfully(self, driver, name, surname, adress, metrostation, phonenumber, comment):
        order_page = OrderPage()
        driver.get(order_page.locator_base_url)
        order_page.click_header_order_button(driver)
        order_page.click_cookie_consent(driver)
        order_page.fill_in_name_field(driver, name)
        order_page.fill_in_surname_field(driver, surname)
        order_page.fill_in_adress_field(driver, adress)
        order_page.click_metro_station_field(driver)
        order_page.fill_in_metro_station(driver, metrostation)
        WebDriverWait(driver, 5)
        order_page.choose_metro_station(driver)
        order_page.fill_in_phone_field(driver, phonenumber)
        order_page.click_next_button(driver)
        order_page.click_delivery_date_field(driver)
        order_page.choose_delivery_date(driver)
        order_page.click_time_of_lease_field(driver)
        order_page.choose_time_of_lease_one_day(driver)
        order_page.choose_scooter_color(driver, *order_page.locator_color_gray_field)
        order_page.fill_in_comment_field(driver, comment)
        order_page.click_final_order_button(driver)
        order_page.wait_until_element_is_clickable(driver, order_page.locator_are_you_sure_yes_button)
        order_page.click_are_you_sure_yes_button(driver)

        assert driver.find_element(*order_page.locator_show_status_button).text == "Посмотреть статус"








