import allure

from ui.locators.basic_locators import DashboardPageLocators
from ui.pages.base_page import BasePage
from ui.pages.creating_campaign_page import CreatingCampaignPage


class DashBoardPage(BasePage):
    locators = DashboardPageLocators
    url = 'https://target-sandbox.my.com/dashboard'

    @allure.step("Проверка на наличие имени пользователя в навбаре после авторизации.")
    def is_user_name_button_present(self):
        self.is_element_present(*self.locators.USER_NAME_BUTTON)

    @allure.step("Переход на страницу создания кампании.")
    def go_to_creating_campaign_page(self):
        self.move_to_present_element(*self.locators.CREATE_CAMPAIGN_BUTTON)
        create_campaign_button = self.get_clickable_element(*self.locators.CREATE_CAMPAIGN_BUTTON)
        create_campaign_button.click()
        return CreatingCampaignPage(driver=self.driver)

    @allure.step("Проверка на то, что кампания создана.")
    def is_campaign_created(self, campaign_name):
        self.is_element_present(*self.locators.CREATED_CAMPAIGNS)
        created_campaigns = self.driver.find_elements(*self.locators.CREATED_CAMPAIGNS)
        for campaign in created_campaigns:
            name = campaign.get_attribute("title")
            if name == campaign_name:
                return True
        return False
