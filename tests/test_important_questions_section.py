from pages.info_page import InfoPage
import allure


class TestInfoPage:

    @allure.title('Проверка того, что корректно открываются ответы на вопросы в разделе Вопросы о важном')
    @allure.description('Проверка того, что при нажатии на 1 вопрос открывается корректный ответ')
    def test_choose_question_how_much(self, driver):
        info_page = InfoPage()
        info_page.open_base_url(driver)
        info_page.open_important_info_block(driver)
        info_page.click_cookie_consent(driver)
        info_page.click_dropdown_menu_button(driver, *info_page.locator_question_how_much)
        info_page.wait_until_element_is_visible(driver, info_page.locator_answer_how_much)

        assert driver.find_element(*info_page.locator_answer_how_much).text == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    @allure.title('Проверка того, что корректно открываются ответы на вопросы в разделе Вопросы о важном')
    @allure.description('Проверка того, что при нажатии на 2 вопрос открывается корректный ответ')
    def test_choose_question_i_want_several(self, driver):
        info_page = InfoPage()
        info_page.open_base_url(driver)
        info_page.open_important_info_block(driver)
        info_page.click_cookie_consent(driver)
        info_page.click_dropdown_menu_button(driver, *info_page.locator_question_i_want_several)
        info_page.wait_until_element_is_visible(driver, info_page.locator_answer_i_want_several)

        assert driver.find_element(*info_page.locator_answer_i_want_several).text == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    @allure.title('Проверка того, что корректно открываются ответы на вопросы в разделе Вопросы о важном')
    @allure.description('Проверка того, что при нажатии на 3 вопрос открывается корректный ответ')
    def test_choose_question_count_time(self, driver):
        info_page = InfoPage()
        info_page.open_base_url(driver)
        info_page.open_important_info_block(driver)
        info_page.click_cookie_consent(driver)
        info_page.click_dropdown_menu_button(driver, *info_page.locator_question_count_time)
        info_page.wait_until_element_is_visible(driver, info_page.locator_answer_count_time)

        assert driver.find_element(*info_page.locator_answer_count_time).text == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    @allure.title('Проверка того, что корректно открываются ответы на вопросы в разделе Вопросы о важном')
    @allure.description('Проверка того, что при нажатии на 4 вопрос открывается корректный ответ')
    def test_choose_question_order_for_today(self, driver):
        info_page = InfoPage()
        info_page.open_base_url(driver)
        info_page.open_important_info_block(driver)
        info_page.click_cookie_consent(driver)
        info_page.click_dropdown_menu_button(driver, *info_page.locator_question_order_for_today)
        info_page.wait_until_element_is_visible(driver, info_page.locator_answer_order_for_today)

        assert driver.find_element(*info_page.locator_answer_order_for_today).text == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    @allure.title('Проверка того, что корректно открываются ответы на вопросы в разделе Вопросы о важном')
    @allure.description('Проверка того, что при нажатии на 5 вопрос открывается корректный ответ')
    def test_choose_question_prolong_order(self, driver):
        info_page = InfoPage()
        info_page.open_base_url(driver)
        info_page.open_important_info_block(driver)
        info_page.click_cookie_consent(driver)
        info_page.click_dropdown_menu_button(driver, *info_page.locator_question_prolong_order)
        info_page.wait_until_element_is_visible(driver, info_page.locator_answer_prolong_order)

        assert driver.find_element(*info_page.locator_answer_prolong_order).text == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    @allure.title('Проверка того, что корректно открываются ответы на вопросы в разделе Вопросы о важном')
    @allure.description('Проверка того, что при нажатии на 6 вопрос открывается корректный ответ')
    def test_choose_question_how_about_charger(self, driver):
        info_page = InfoPage()
        info_page.open_base_url(driver)
        info_page.open_important_info_block(driver)
        info_page.click_cookie_consent(driver)
        info_page.click_dropdown_menu_button(driver, *info_page.locator_question_how_about_charger)
        info_page.wait_until_element_is_visible(driver, info_page.locator_answer_how_about_charger)

        assert driver.find_element(*info_page.locator_answer_how_about_charger).text == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    @allure.title('Проверка того, что корректно открываются ответы на вопросы в разделе Вопросы о важном')
    @allure.description('Проверка того, что при нажатии на 7 вопрос открывается корректный ответ')
    def test_choose_question_cancel_order(self, driver):
        info_page = InfoPage()
        info_page.open_base_url(driver)
        info_page.open_important_info_block(driver)
        info_page.click_cookie_consent(driver)
        info_page.click_dropdown_menu_button(driver, *info_page.locator_question_cancel_order)
        info_page.wait_until_element_is_visible(driver, info_page.locator_answer_cancel_order)

        assert driver.find_element(*info_page.locator_answer_cancel_order).text == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    @allure.title('Проверка того, что корректно открываются ответы на вопросы в разделе Вопросы о важном')
    @allure.description('Проверка того, что при нажатии на 8 вопрос открывается корректный ответ')
    def test_choose_question_beyond_mkad_delivery(self, driver):
        info_page = InfoPage()
        info_page.open_base_url(driver)
        info_page.open_important_info_block(driver)
        info_page.click_cookie_consent(driver)
        info_page.click_dropdown_menu_button(driver, *info_page.locator_question_beyond_mkad_delivery)
        info_page.wait_until_element_is_visible(driver, info_page.locator_answer_beyond_mkad_delivery)

        assert driver.find_element(*info_page.locator_answer_beyond_mkad_delivery).text == "Да, обязательно. Всем самокатов! И Москве, и Московской области."

