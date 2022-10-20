import os

import allure
from selenium.common.exceptions import TimeoutException
from ui.locators.basic_locators import CreatingCampaignPageLocators
from ui.pages.base_page import BasePage


class CreatingCampaignPage(BasePage):
    locators = CreatingCampaignPageLocators
    url = 'https://target-sandbox.my.com/campaign/new'

    @allure.step("Выбор категории - 'трафик'.")
    def select_category_traffic(self):
        category_traffic = self.get_clickable_element(*self.locators.TRAFFIC)
        category_traffic.click()

    @allure.step("Ввод url.")
    def input_url(self, target_url):
        url_field = self.get_present_element(*self.locators.URL_FIELD)
        url_field.clear()
        url_field.send_keys(target_url)

    @allure.step("Ввод имени компании.")
    def input_campaign_name(self, campaign_name):
        campaign_name_field = self.get_clickable_element(*self.locators.CAMPAIGN_NAME)
        campaign_name_field.clear()
        campaign_name_field.send_keys(f'{campaign_name}')

    @allure.step("Выбор социальной характеристики высшее образование.")
    def select_social_characteristics(self):
        self.scroll_to_clickable_element(*self.locators.SOCIAL_CHARACTERISTICS)
        self.get_visible_element(*self.locators.SOCIAL_CHARACTERISTICS).click()
        self.get_visible_element(*self.locators.EDUCATION_LIST).click()
        self.get_visible_element(*self.locators.HIGHER_EDUCATION).click()

    @allure.step("Выбор музыкального предпочтения - 'рок'.")
    def select_interests(self):
        self.scroll_to_clickable_element(*self.locators.INTERESTS)
        self.get_clickable_element(*self.locators.INTERESTS).click()
        self.get_visible_element(*self.locators.MUSIC).click()
        self.get_visible_element(*self.locators.ROCK).click()

    @allure.step("Выбор формата рекламы - тизер.")
    def select_ad_format(self):
        self.scroll_to_clickable_element(*self.locators.AD_FORMAT_TEASER)
        self.get_clickable_element(*self.locators.AD_FORMAT_TEASER).click()

    @allure.step("Добавление изображения в объявление.")
    def add_picture(self):
        project_dir = '\\'.join(
            os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
        file_path = os.path.join(project_dir, 'pictures')
        file_path = os.path.join(file_path, 'teaser.png')
        try:
            self.scroll_to_clickable_element(*self.locators.SHOW_MEDIA_LIB_BUTTON)
            self.get_clickable_element(*self.locators.SHOW_MEDIA_LIB_BUTTON).click()
        except TimeoutException:
            pass
        self.scroll_to_clickable_element(*self.locators.UPLOAD_IMAGE_BUTTON)
        add_picture_button = self.get_present_element(*self.locators.IMAGE_INPUT)
        add_picture_button.send_keys(file_path)

    @allure.step("Заполнение текстовых характеристик объявления.")
    def fill_teaser_fields(self, target_url, title, text):
        with allure.step("Ввод ссылки."):
            self.scroll_to_clickable_element(*self.locators.TEASER_LINK)
            teaser_link = self.get_present_element(*self.locators.TEASER_LINK)
            teaser_link.clear()
            teaser_link.send_keys(target_url)
        with allure.step("Ввод названия."):
            teaser_title = self.get_present_element(*self.locators.TEASER_TITLE)
            teaser_title.clear()
            teaser_title.send_keys(title)
        with allure.step("Ввод текста."):
            teaser_text = self.get_present_element(*self.locators.TEASER_TEXT)
            teaser_text.clear()
            teaser_text.send_keys(text)

    @allure.step("Нажатие на кнопку создания кампании.")
    def save_campaign(self):
        self.scroll_to_clickable_element(*self.locators.SUBMIT_BUTTON)
        self.get_clickable_element(*self.locators.SUBMIT_BUTTON).click()
