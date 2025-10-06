from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем на логотип')
    def click_logo(self, logo):
        self.driver.find_element(*logo).click()
    
    @allure.step('Ждем загрузки страницы {page}')
    def wait_new_page(self, page):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(page))

    @allure.step('Открываем страницу {page} и пролистываем вниз')
    def open_page(self, page):
        self.driver.get(page)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def find_and_click_elements(self, element, response):
        self.driver.find_element(*element).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(response))
