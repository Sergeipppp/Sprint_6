from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

class OrderPage:
    input_name = [By.CSS_SELECTOR, "input[placeholder='* Имя']"]
    input_surname = [By.CSS_SELECTOR, "input[placeholder='* Фамилия']"]
    input_address = [By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']"]
    input_phone = [By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"]
    input_order_data = [By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']"]
    choose_date = [By.CLASS_NAME, "react-datepicker__day--029"]
    metro = [By.CLASS_NAME, "select-search"]
    order_metro = [By.CLASS_NAME, "select-search__select"]
    order_header = [By.CLASS_NAME, "Order_Header__BZXOb"]
    next_button = [By.XPATH, "//button[text()='Далее']"]
    order_period = [By.CLASS_NAME, "Dropdown-placeholder"]
    one_day = [By.XPATH, "//div[text()='сутки']"]
    confirm_order = [By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']"]
    order_modal_header = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"]
    yes_button = [By.XPATH, "//button[text()='Да']"]
    check_status_button = [By.XPATH, "//button[text()='Посмотреть статус']"]

    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Вводим значение в поле')
    def input_name_in_field(self, field, name):
        self.driver.find_element(*field).send_keys(name)

    def wait_for_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.order_header))

    def wait_order_modal_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.order_modal_header))

    @allure.step('Выбираем станцию Метро')
    def click_to_choose_station(self):
        self.driver.find_element(*self.metro).click()
        self.driver.find_element(*self.order_metro).click()

    @allure.step('Нажимаем на кнопку Далее')
    def click_to_next_button(self):
        self.driver.find_element(*self.next_button).click()

    @allure.step('Выбираем дату заказа')
    def choose_order_data(self):
        self.driver.find_element(*self.input_order_data).click()
        self.driver.find_element(*self.choose_date).click()

    @allure.step('Выбираем период бронирования')
    def choose_one_day_order_period(self):
        self.driver.find_element(*self.order_period).click()
        self.driver.find_element(*self.one_day).click()
    
    @allure.step('Нажимаем на кнопку Заказать')
    def click_confirm_order_button(self):
        self.driver.find_element(*self.confirm_order).click()

    @allure.step('Нажимаем на кнопку подтверждения заказа')
    def click_yes_order_button(self):
        self.driver.find_element(*self.yes_button).click()

    @allure.step('Получаем модальное окно с успешным заказом')
    def find_text_in_success_order(self):
        return self.driver.find_element(*self.order_modal_header).text
    
    @allure.step('Нажимаем на кнопку проверить статус заказа')
    def click_check_status_button(self):
        self.driver.find_element(*self.check_status_button).click()
