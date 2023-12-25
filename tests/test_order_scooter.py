import allure
import pytest
from pages.order_page import OrderPage


class TestOrderPage:

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
        order_page = OrderPage(driver)
        order_page.open_base_url()
        order_page.click_header_order_button()
        order_page.click_cookie_consent()
        order_page.fill_in_name_field(name)
        order_page.fill_in_surname_field(surname)
        order_page.fill_in_adress_field(adress)
        order_page.click_metro_station_field()
        order_page.fill_in_metro_station(metrostation)
        order_page.wait_until_element_is_visible(order_page.locator_metro_station_choice)
        order_page.choose_metro_station()
        order_page.fill_in_phone_field(phonenumber)
        order_page.click_next_button()
        order_page.click_delivery_date_field()
        order_page.choose_delivery_date()
        order_page.click_time_of_lease_field()
        order_page.choose_time_of_lease_one_day()
        order_page.choose_scooter_color(*order_page.locator_color_gray_field)
        order_page.fill_in_comment_field(comment)
        order_page.click_final_order_button()
        order_page.wait_until_element_is_clickable(order_page.locator_are_you_sure_yes_button)
        order_page.click_are_you_sure_yes_button()

        assert order_page.find_show_status_button().text == "Посмотреть статус"








