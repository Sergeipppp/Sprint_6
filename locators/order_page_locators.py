from selenium.webdriver.common.by import By

class OrderPageLocators:
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
    