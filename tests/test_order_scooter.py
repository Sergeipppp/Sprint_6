from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from locators.base_page_locators import BasePageLocastors
from data import FixData
import pytest
import allure

@allure.title("Тестирование функционала - заказ Самоката")
class TestOrderScooter:  
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
    def test_order_scooter_with_button_in_top(self, driver, user_data):
        driver.get(FixData.url)
        main_page = MainPage(driver)
        main_page.click_order_button_small()
        order_page = OrderPage(driver)
        order_page.wait_for_header()
        order_page.input_name_in_field(OrderPageLocators.input_name, user_data["name"])
        order_page.input_name_in_field(OrderPageLocators.input_surname, user_data["surname"])
        order_page.input_name_in_field(OrderPageLocators.input_address, user_data["address"])
        order_page.input_name_in_field(OrderPageLocators.input_phone, user_data["phone"])
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
        main_page.click_logo(BasePageLocastors.scooter_logo)
        assert driver.current_url == FixData.url

    @allure.title('Делаем заказ на самокат, через кнопку заказать внизу сайта')
    def test_order_scooter_with_button_in_down(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(FixData.url)
        main_page.click_order_button_big()
        order_page = OrderPage(driver)
        order_page.wait_for_header()
        order_page.input_name_in_field(OrderPageLocators.input_name,'Сергей')
        order_page.input_name_in_field(OrderPageLocators.input_surname,'Иванов')
        order_page.input_name_in_field(OrderPageLocators.input_address,'Москва')
        order_page.input_name_in_field(OrderPageLocators.input_phone,'+7911123123')
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
        main_page.click_logo(BasePageLocastors.scooter_logo)
        assert driver.current_url == FixData.url

    @allure.title('Проверяем, что при нажатии на логотип Яндекса, откроется страница Дзена')
    def test_click_yandex_logo(self, driver):
        driver.get(FixData.url)
        main_page = MainPage(driver)
        main_window = driver.current_window_handle
        main_page.click_logo(BasePageLocastors.yandex_logo)
        all_windows = driver.window_handles
        new_window = [window for window in all_windows if window != main_window][0]
        driver.switch_to.window(new_window)
        main_page.wait_new_page(FixData.ya_url)
        assert driver.current_url == FixData.ya_url
