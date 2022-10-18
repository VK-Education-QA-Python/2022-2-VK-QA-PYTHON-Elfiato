from ui.locators.basic_locators import MainPageLocators
from ui.pages.login_page import LoginPage
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def go_to_login_page(self):
        login_button = self.get_clickable_element(*self.locators.LOGIN_BUTTON_IN_HEADER)
        login_button.click()
        return LoginPage(driver=self.driver)
