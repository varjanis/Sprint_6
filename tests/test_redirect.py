import allure
from pages.redirect_page import RedirectPage


class TestRedirectPage:

    @allure.title('Открыть страницу заказа из хедера')
    @allure.description('Проверка того, что страница заказа открывается по клику на кнопку Заказать в хедере')
    def test_redirect_to_order_from_header(self, driver):
        redirect_page = RedirectPage(driver)
        redirect_page.open_base_url()
        redirect_page.click_header_order_button()
        redirect_page.wait_until_element_is_visible(redirect_page.locator_next_button)

        assert redirect_page.show_current_url() == redirect_page.locator_order_page_url

    @allure.title('Открыть страницу заказа из середины страницы')
    @allure.description(
        'Проверка того, что страница заказа открывается по клику на кнопку Заказать в середине страницы')
    def test_redirect_to_order_from_middle_page(self, driver):
        redirect_page = RedirectPage(driver)
        redirect_page.open_base_url()
        redirect_page.click_header_order_button()
        redirect_page.wait_until_element_is_visible(redirect_page.locator_next_button)

        assert redirect_page.show_current_url() == redirect_page.locator_order_page_url

    @allure.title('Редирект по клику на логотип Самоката')
    @allure.description(
        'Проверка того, что по клику на логотип Самоката открывается главная страница с лендингом Самоката')
    def test_redirect_from_scooter_logo(self, driver):
        redirect_page = RedirectPage(driver)
        redirect_page.open_base_url()
        redirect_page.click_header_order_button()
        redirect_page.click_scooter_logo()
        redirect_page.wait_until_element_is_visible(redirect_page.locator_page_order_button)

        assert redirect_page.show_current_url() == redirect_page.locator_base_url

    @allure.title('Открыть главную страницу Дзена кликом на логотип Яндекса')
    @allure.description('Проверка того, что при нажатии на логотип Яндекса идёт редирект на главную страницу Дзена')
    def test_redirect_from_yandex_logo(self, driver):
        redirect_page = RedirectPage(driver)
        redirect_page.open_base_url()
        redirect_page.click_header_order_button()
        redirect_page.assert_window()
        redirect_page.click_yandex_logo()
        redirect_page.check_window()
        redirect_page.wait_until_element_is_clickable(redirect_page.locator_dzen_find_button)

        assert redirect_page.show_current_url() == 'https://dzen.ru/?yredirect=true'
