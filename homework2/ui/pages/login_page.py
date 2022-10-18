from ui.pages.base_page import BasePage
from ui.locators.basic_locators import LoginPageLocators
from ui.pages.dashboard_page import DashBoardPage


class LoginPage(BasePage):
    locators = LoginPageLocators()
    __login = 'jo.ry@mail.ru'
    __password = '12345A'

    def login(self):
        email_field = self.get_present_element(*self.locators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(self.__login)
        password_field = self.get_present_element(*self.locators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(self.__password)
        self.get_present_element(*self.locators.LOGIN_BUTTON_IN_AUTHORIZATION_FORM).click()
        return DashBoardPage(driver=self.driver)
