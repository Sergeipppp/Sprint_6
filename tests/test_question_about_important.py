from pages.main_page import MainPage
from data import TestData
from selenium import webdriver
import allure

@allure.title("Тестирование функционала - присутствие ответов на самые важные вопросы")
class TestQuestion:
    driver = None
    
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
    
    @allure.title('Проверяем наличие ответа на 1 вопрос')
    def test_question_0(self):
        main_page = MainPage(self.driver)
        main_page.open_page(TestData.url)
        main_page.wait_when_question_to_be_clickable(main_page.question0)
        main_page.click_sign_in_question_button(main_page.question0)
        main_page.wait_for_load_response(main_page.answer0)
        assert main_page.get_response_afer_click(main_page.answer0) == TestData.answer0
    
    @allure.title('Проверяем наличие ответа на 2 вопрос')
    def test_question_1(self):
        main_page = MainPage(self.driver)
        main_page.open_page(TestData.url)
        main_page.wait_when_question_to_be_clickable(main_page.question1)
        main_page.click_sign_in_question_button(main_page.question1)
        main_page.wait_for_load_response(main_page.answer1)
        assert main_page.get_response_afer_click(main_page.answer1) == TestData.answer1

    @allure.title('Проверяем наличие ответа на 3 вопрос')
    def test_question_2(self):
        main_page = MainPage(self.driver)
        main_page.open_page(TestData.url)
        main_page.wait_when_question_to_be_clickable(main_page.question2)
        main_page.click_sign_in_question_button(main_page.question2)
        main_page.wait_for_load_response(main_page.answer2)
        assert main_page.get_response_afer_click(main_page.answer2) == TestData.answer2

    @allure.title('Проверяем наличие ответа на 4 вопрос')
    def test_question_3(self):
        main_page = MainPage(self.driver)
        main_page.open_page(TestData.url)
        main_page.wait_when_question_to_be_clickable(main_page.question3)
        main_page.click_sign_in_question_button(main_page.question3)
        main_page.wait_for_load_response(main_page.answer3)
        assert main_page.get_response_afer_click(main_page.answer3) == TestData.answer3

    @allure.title('Проверяем наличие ответа на 5 вопрос')
    def test_question_4(self):
        main_page = MainPage(self.driver)
        main_page.open_page(TestData.url)
        main_page.wait_when_question_to_be_clickable(main_page.question4)
        main_page.click_sign_in_question_button(main_page.question4)
        main_page.wait_for_load_response(main_page.answer4)
        assert main_page.get_response_afer_click(main_page.answer4) == TestData.answer4

    @allure.title('Проверяем наличие ответа на 6 вопрос')
    def test_question_5(self):
        main_page = MainPage(self.driver)
        main_page.open_page(TestData.url)
        main_page.wait_when_question_to_be_clickable(main_page.question5)
        main_page.click_sign_in_question_button(main_page.question5)
        main_page.wait_for_load_response(main_page.answer5)
        assert main_page.get_response_afer_click(main_page.answer5) == TestData.answer5

    @allure.title('Проверяем наличие ответа на 7 вопрос')
    def test_question_6(self):
        main_page = MainPage(self.driver)
        main_page.open_page(TestData.url)
        main_page.wait_when_question_to_be_clickable(main_page.question6)
        main_page.click_sign_in_question_button(main_page.question6)
        main_page.wait_for_load_response(main_page.answer6)
        assert main_page.get_response_afer_click(main_page.answer6) == TestData.answer6

    @allure.title('Проверяем наличие ответа на 8 вопрос')
    def test_question_7(self):
        main_page = MainPage(self.driver)
        main_page.open_page(TestData.url)
        main_page.wait_when_question_to_be_clickable(main_page.question7)
        main_page.click_sign_in_question_button(main_page.question7)
        main_page.wait_for_load_response(main_page.answer7)
        assert main_page.get_response_afer_click(main_page.answer7) == TestData.answer7

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
