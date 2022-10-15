from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException, \
    InvalidElementStateException
from selenium.webdriver.common.action_chains import ActionChains
import locators

WAITING_TIME = 10


class Base:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, how, what, timeout=WAITING_TIME):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((how, what)))
        except (NoSuchElementException, TimeoutException):
            return False
        return True

    def get_present_element(self, how, what):
        if self.is_element_present(how, what):
            return self.driver.find_element(how, what)
        else:
            assert self.is_element_present(how, what), f'Элемент с локатором {how} :: {what} не найден'

    def move_to_present_element(self, how, what):
        action = ActionChains(self.driver)
        element = self.get_present_element(how, what)
        action.move_to_element(element).perform()

    def is_element_clickable(self, how, what, timeout=WAITING_TIME):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((how, what)))
        except (ElementNotInteractableException, InvalidElementStateException, TimeoutException):
            return False
        return True

    def get_clickable_element(self, how, what):
        if self.is_element_clickable(how, what):
            return self.driver.find_element(how, what)
        else:
            assert self.is_element_present(how, what), f'На элемент с локатором {how} :: {what} невозможно нажать.'

    def is_element_visible(self, how, what, timeout=WAITING_TIME):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))
        except (NoSuchElementException, TimeoutException):
            return False
        return True

    def login_func(self, login, password):
        login_button_in_header = self.get_present_element(*locators.LOGIN_BUTTON_IN_HEADER)
        login_button_in_header.click()
        email_field = self.get_present_element(*locators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(login)
        password_field = self.get_present_element(*locators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)
        self.get_present_element(*locators.LOGIN_BUTTON_IN_AUTHORIZATION_FORM).click()
