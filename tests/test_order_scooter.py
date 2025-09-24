from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import TestData
from selenium import webdriver
import pytest
import allure

@allure.title("Тестирование функционала - заказ Самоката")
class TestOrderScooter:
    driver = None
    
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
    
    @pytest.mark.parametrize("user_data", [
        {
            "name": "Сергей",
            "surname": "Иванов",
            "address": "Москва",
            "phone": "+79123456789"
        },
        {
            "name": "Иван",
            "surname": "Сергеев",
            "address": "Абакан",
            "phone": "+79123456111"
        }
    ])
    @allure.title('Делаем заказ на самокат, через кнопку заказать наверху сайта')
    def test_order_scooter_with_button_in_top(self, user_data):
        self.driver.get(TestData.url)
        main_page = MainPage(self.driver)
        main_page.click_order_button_small()
        order_page = OrderPage(self.driver)
        order_page.wait_for_header()
        order_page.input_name_in_field(OrderPage.input_name, user_data["name"])
        order_page.input_name_in_field(OrderPage.input_surname, user_data["surname"])
        order_page.input_name_in_field(OrderPage.input_address, user_data["address"])
        order_page.input_name_in_field(OrderPage.input_phone, user_data["phone"])
        order_page.click_to_choose_station()
        order_page.click_to_next_button()    
        order_page.wait_for_header()
        order_page.choose_order_data()
        order_page.choose_one_day_order_period()
        order_page.click_confirm_order_button()
        order_page.wait_order_modal_header()
        order_page.click_yes_order_button()
        order_page.wait_order_modal_header()
        assert order_page.find_text_in_success_order()[:14] == 'Заказ оформлен'
        order_page.click_check_status_button()
        main_page.click_scooter_logo()
        assert self.driver.current_url == TestData.url

    @allure.title('Делаем заказ на самокат, через кнопку заказать внизу сайта')
    def test_order_scooter_with_button_in_down(self):
        main_page = MainPage(self.driver)
        main_page.open_page(TestData.url)
        main_page.wait_when_question_to_be_clickable(main_page.question0)
        main_page.click_order_button_big()
        order_page = OrderPage(self.driver)
        order_page.wait_for_header()
        order_page.input_name_in_field(OrderPage.input_name,'Сергей')
        order_page.input_name_in_field(OrderPage.input_surname,'Иванов')
        order_page.input_name_in_field(OrderPage.input_address,'Москва')
        order_page.input_name_in_field(OrderPage.input_phone,'+7911123123')
        order_page.click_to_choose_station()
        order_page.click_to_next_button()    
        order_page.wait_for_header()
        order_page.choose_order_data()
        order_page.choose_one_day_order_period()
        order_page.click_confirm_order_button()
        order_page.wait_order_modal_header()
        order_page.click_yes_order_button()
        order_page.wait_order_modal_header()
        assert order_page.find_text_in_success_order()[:14] == 'Заказ оформлен'
        order_page.click_check_status_button()
        main_page.click_scooter_logo()
        assert self.driver.current_url == TestData.url

    @allure.title('Проверяем, что при нажатии на логотип Яндекса, откроется страница Дзена')
    def test_click_yandex_logo(self):
        self.driver.get(TestData.url)
        main_page = MainPage(self.driver)
        main_window = self.driver.current_window_handle
        main_page.click_yandex_logo()
        all_windows = self.driver.window_handles
        new_window = [window for window in all_windows if window != main_window][0]
        self.driver.switch_to.window(new_window)
        main_page.wait_new_page_dzen(TestData.ya_url)
        assert self.driver.current_url == TestData.ya_url
        
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
