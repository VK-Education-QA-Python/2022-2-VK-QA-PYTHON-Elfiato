import allure

from ui.pages.base_page import BasePage
from ui.locators.basic_locators import LoginPageLocators
from ui.pages.dashboard_page import DashBoardPage


class LoginPage(BasePage):
    locators = LoginPageLocators()
    __login = 'jo.ry@mail.ru'
    __password = '12345A'

    @allure.step("Авторизация.")
    def login(self):
        self.input_text(*self.locators.EMAIL_FIELD, self.__login)
        self.input_text(*self.locators.PASSWORD_FIELD, self.__password)

        self.get_present_element(*self.locators.LOGIN_BUTTON_IN_AUTHORIZATION_FORM).click()
        return DashBoardPage(driver=self.driver)
