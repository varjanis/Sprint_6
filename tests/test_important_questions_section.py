import pytest

from pages.info_page import InfoPage
import allure


class TestInfoPage:

    answer_texts = [
                    "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
                    "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
                    "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
                    "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
                    "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
                    "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
                    "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
                    "Да, обязательно. Всем самокатов! И Москве, и Московской области."
                    ]

    @allure.title('Проверка того, что корректно открываются ответы на вопросы в разделе Вопросы о важном')
    @allure.step('Проверить, корректно ли открылся ответ на данный вопрос')
    @pytest.mark.parametrize('question, answer, answer_text',
                             [
                             [InfoPage.locator_question_how_much, InfoPage.locator_answer_how_much, answer_texts[0]],
                             [InfoPage.locator_question_i_want_several, InfoPage.locator_answer_i_want_several, answer_texts[1]],
                             [InfoPage.locator_question_count_time, InfoPage.locator_answer_count_time, answer_texts[2]],
                             [InfoPage.locator_question_order_for_today, InfoPage.locator_answer_order_for_today, answer_texts[3]],
                             [InfoPage.locator_question_prolong_order, InfoPage.locator_answer_prolong_order, answer_texts[4]],
                             [InfoPage.locator_question_how_about_charger, InfoPage.locator_answer_how_about_charger, answer_texts[5]],
                             [InfoPage.locator_question_cancel_order, InfoPage.locator_answer_cancel_order, answer_texts[6]],
                             [InfoPage.locator_question_beyond_mkad_delivery, InfoPage.locator_answer_beyond_mkad_delivery, answer_texts[7]],
                             ]
                             )
    def test_check_if_the_answer_is_correct(self, driver, question, answer, answer_text):
        info_page = InfoPage(driver)
        info_page.open_base_url()
        info_page.open_important_info_block()
        info_page.click_cookie_consent()
        info_page.click_dropdown_menu_button(question)
        info_page.wait_until_element_is_visible(answer)

        assert info_page.find_page(answer).text == answer_text


