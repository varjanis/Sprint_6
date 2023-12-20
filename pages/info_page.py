from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InfoPage(BasePage):

    locator_important_info_block = (By.XPATH, './/div[text() = "Вопросы о важном"]')
    locator_question_how_much = (By.XPATH, './/div[text() = "Сколько это стоит? И как оплатить?"]')
    locator_answer_how_much = (By.XPATH, './/p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]')

    locator_question_i_want_several = (By.XPATH, './/div[@class="accordion__button" and text() = "Хочу сразу несколько самокатов! '
                                                 'Так можно?"]')
    locator_answer_i_want_several = (By.XPATH, './/p[text() = "Пока что у нас так: один заказ — один самокат. '
                                               'Если хотите покататься с друзьями, '
                                               'можете просто сделать несколько заказов — один за другим."]')

    locator_question_count_time = (By.XPATH, './/div[@class="accordion__button" and text() = "Как рассчитывается время аренды?" ]')
    locator_answer_count_time = (By.XPATH, './/p[text() = "Допустим, вы оформляете заказ на 8 мая. '
                                           'Мы привозим самокат 8 мая в течение дня. '
                                           'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                                           'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]')

    locator_question_order_for_today = (By.XPATH, './/div[@class="accordion__button" and text() = "Можно ли заказать самокат прямо на сегодня?"]')
    locator_answer_order_for_today = (By.XPATH, './/p[text() = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."]')

    locator_question_prolong_order = (By.XPATH, './/div[@class="accordion__button" and text() = "Можно ли продлить заказ или вернуть самокат раньше?" ]')
    locator_answer_prolong_order = (By.XPATH, './/p[text() = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."]')

    locator_question_how_about_charger = (By.XPATH, './/div[@class="accordion__button" and text() = "Вы привозите зарядку вместе с самокатом?"]')
    locator_answer_how_about_charger = (By.XPATH, './/p[text() = "Самокат приезжает к вам с полной зарядкой. '
                                                  'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
                                                  'Зарядка не понадобится."]')

    locator_question_cancel_order = (By.XPATH, './/div[@class="accordion__button" and text() = "Можно ли отменить заказ?"]')
    locator_answer_cancel_order = (By.XPATH, './/p[text() = "Да, пока самокат не привезли. '
                                             'Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."]')

    locator_question_beyond_mkad_delivery = (By.XPATH, './/div[@class="accordion__button" and text() = "Я жизу за МКАДом, привезёте?"]')
    locator_answer_beyond_mkad_delivery = (By.XPATH, './/p[text() = "Да, обязательно. Всем самокатов! И Москве, и Московской области."]')

    def open_important_info_block(self, driver):
        element = driver.find_element(*self.locator_important_info_block)
        return driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_dropdown_menu_button(self, driver, *locator):
        return driver.find_element(*locator).click()




