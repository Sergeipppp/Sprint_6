from pages.main_page import MainPage
from data import TestData
from data import FixData
from locators.main_page_locators import MainPageLocators
import allure

@allure.title("Тестирование функционала - присутствие ответов на самые важные вопросы")
class TestQuestion:    
    @allure.title('Проверяем наличие ответа на 1 вопрос')
    def test_question_0(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(FixData.url)
        main_page.wait_when_question_to_be_clickable(MainPageLocators.question0)
        main_page.click_sign_in_question_button(MainPageLocators.question0, MainPageLocators.answer0)
        assert main_page.get_response_afer_click(MainPageLocators.answer0) == TestData.answer0
    
    @allure.title('Проверяем наличие ответа на 2 вопрос')
    def test_question_1(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(FixData.url)
        main_page.wait_when_question_to_be_clickable(MainPageLocators.question1)
        main_page.click_sign_in_question_button(MainPageLocators.question1, MainPageLocators.answer1)
        assert main_page.get_response_afer_click(MainPageLocators.answer1) == TestData.answer1

    @allure.title('Проверяем наличие ответа на 3 вопрос')
    def test_question_2(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(FixData.url)
        main_page.wait_when_question_to_be_clickable(MainPageLocators.question2)
        main_page.click_sign_in_question_button(MainPageLocators.question2, MainPageLocators.answer2)
        assert main_page.get_response_afer_click(MainPageLocators.answer2) == TestData.answer2

    @allure.title('Проверяем наличие ответа на 4 вопрос')
    def test_question_3(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(FixData.url)
        main_page.wait_when_question_to_be_clickable(MainPageLocators.question3)
        main_page.click_sign_in_question_button(MainPageLocators.question3, MainPageLocators.answer3)
        assert main_page.get_response_afer_click(MainPageLocators.answer3) == TestData.answer3

    @allure.title('Проверяем наличие ответа на 5 вопрос')
    def test_question_4(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(FixData.url)
        main_page.wait_when_question_to_be_clickable(MainPageLocators.question4)
        main_page.click_sign_in_question_button(MainPageLocators.question4, MainPageLocators.answer4)
        assert main_page.get_response_afer_click(MainPageLocators.answer4) == TestData.answer4

    @allure.title('Проверяем наличие ответа на 6 вопрос')
    def test_question_5(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(FixData.url)
        main_page.wait_when_question_to_be_clickable(MainPageLocators.question5)
        main_page.click_sign_in_question_button(MainPageLocators.question5, MainPageLocators.answer5)
        assert main_page.get_response_afer_click(MainPageLocators.answer5) == TestData.answer5

    @allure.title('Проверяем наличие ответа на 7 вопрос')
    def test_question_6(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(FixData.url)
        main_page.wait_when_question_to_be_clickable(MainPageLocators.question6)
        main_page.click_sign_in_question_button(MainPageLocators.question6, MainPageLocators.answer6)
        assert main_page.get_response_afer_click(MainPageLocators.answer6) == TestData.answer6

    @allure.title('Проверяем наличие ответа на 8 вопрос')
    def test_question_7(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(FixData.url)
        main_page.wait_when_question_to_be_clickable(MainPageLocators.question7)
        main_page.click_sign_in_question_button(MainPageLocators.question7, MainPageLocators.answer7)
        assert main_page.get_response_afer_click(MainPageLocators.answer7) == TestData.answer7
