from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class MainPage(BasePage):
    
    @allure.step('Ждем пока кнопка с вопросом станет кликабельна')
    def wait_when_question_to_be_clickable(self, question):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(question))

    @allure.step('Нажимаем на кнопку с вопросом')
    def click_sign_in_question_button(self, question, response):
        self.find_and_click_elements(question, response)

    @allure.step('Получаем ответ на вопрос')
    def get_response_afer_click(self, response):
        return self.driver.find_element(*response).text

    @allure.step('Нажимаем кнопку заказать наверху сайта')
    def click_order_button_small(self):
        self.driver.find_element(*MainPageLocators.order_button_small).click()

    @allure.step('Нажимаем кнопку заказать внизу сайта')
    def click_order_button_big(self):
        self.driver.find_element(*MainPageLocators.order_button_big).click()
