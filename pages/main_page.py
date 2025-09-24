from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

class MainPage:
    question0 = [By.ID, 'accordion__heading-0']
    question1 = [By.ID, 'accordion__heading-1']
    question2 = [By.ID, 'accordion__heading-2']
    question3 = [By.ID, 'accordion__heading-3']
    question4 = [By.ID, 'accordion__heading-4']
    question5 = [By.ID, 'accordion__heading-5']
    question6 = [By.ID, 'accordion__heading-6']
    question7 = [By.ID, 'accordion__heading-7']
    answer0 = [By.XPATH, ".//div[@id='accordion__panel-0']/p"]
    answer1 = [By.XPATH, ".//div[@id='accordion__panel-1']/p"]
    answer2 = [By.XPATH, ".//div[@id='accordion__panel-2']/p"]
    answer3 = [By.XPATH, ".//div[@id='accordion__panel-3']/p"]
    answer4 = [By.XPATH, ".//div[@id='accordion__panel-4']/p"]
    answer5 = [By.XPATH, ".//div[@id='accordion__panel-5']/p"]
    answer6 = [By.XPATH, ".//div[@id='accordion__panel-6']/p"]
    answer7 = [By.XPATH, ".//div[@id='accordion__panel-7']/p"]
    order_button_small = [By.XPATH, "/html/body/div/div/div/div[1]/div[2]/button[1]"]
    order_button_big = [By.XPATH, "/html/body/div/div/div/div[4]/div[2]/div[5]/button"]
    scooter_logo = [By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']"]
    yandex_logo = [By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']"]
      
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем на кнопку с вопросом')
    def click_sign_in_question_button(self, question):
        self.driver.find_element(*question).click()

    @allure.step('Ждем пока кнопка с вопросом станет кликабельна')
    def wait_when_question_to_be_clickable(self, question):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(question))
    
    @allure.step('Ждем отображения ответа на вопрос')
    def wait_for_load_response(self, response):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(response))

    @allure.step('Получаем ответ на вопрос')
    def get_response_afer_click(self, response):
        return self.driver.find_element(*response).text

    @allure.step('Нажимаем кнопку заказать наверху сайта')
    def click_order_button_small(self):
        self.driver.find_element(*self.order_button_small).click()

    @allure.step('Нажимаем кнопку заказать наверху сайта')
    def click_order_button_big(self):
        self.driver.find_element(*self.order_button_big).click()

    @allure.step('Нажимаем на логотип Самокат')
    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()
    
    @allure.step('Нажимаем на логотип Яндекса')
    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

    @allure.step('Ждем загрузки страницы Дзена')
    def wait_new_page_dzen(self, page):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(page))

    @allure.step('Открываем страницу {page} и пролистываем вниз')
    def open_page(self, page):
        self.driver.get(page)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
