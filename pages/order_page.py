from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):

    @allure.step('Вводим значение в поле')
    def input_name_in_field(self, field, name):
        self.driver.find_element(*field).send_keys(name)

    def wait_for_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.order_header))

    def wait_order_modal_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.order_modal_header))

    @allure.step('Выбираем станцию Метро')
    def click_to_choose_station(self):
        self.driver.find_element(*OrderPageLocators.metro).click()
        self.driver.find_element(*OrderPageLocators.order_metro).click()

    @allure.step('Нажимаем на кнопку Далее')
    def click_to_next_button(self):
        self.driver.find_element(*OrderPageLocators.next_button).click()

    @allure.step('Выбираем дату заказа')
    def choose_order_data(self):
        self.driver.find_element(*OrderPageLocators.input_order_data).click()
        self.driver.find_element(*OrderPageLocators.choose_date).click()

    @allure.step('Выбираем период бронирования')
    def choose_one_day_order_period(self):
        self.driver.find_element(*OrderPageLocators.order_period).click()
        self.driver.find_element(*OrderPageLocators.one_day).click()
    
    @allure.step('Нажимаем на кнопку Заказать')
    def click_confirm_order_button(self):
        self.driver.find_element(*OrderPageLocators.confirm_order).click()

    @allure.step('Нажимаем на кнопку подтверждения заказа')
    def click_yes_order_button(self):
        self.driver.find_element(*OrderPageLocators.yes_button).click()

    @allure.step('Получаем модальное окно с успешным заказом')
    def find_text_in_success_order(self):
        return self.driver.find_element(*OrderPageLocators.order_modal_header).text
    
    @allure.step('Нажимаем на кнопку проверить статус заказа')
    def click_check_status_button(self):
        self.driver.find_element(*OrderPageLocators.check_status_button).click()
