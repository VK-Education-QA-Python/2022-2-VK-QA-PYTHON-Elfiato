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
        self.input_text(*self.locators.URL_FIELD, target_url)

    @allure.step("Ввод имени компании.")
    def input_campaign_name(self, campaign_name):
        self.input_text(*self.locators.CAMPAIGN_NAME, campaign_name, self.get_clickable_element)

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
        file_dir = os.path.abspath(os.path.dirname(__file__))
        base_dir = os.path.split(file_dir)[0]
        file_path = os.path.join(base_dir, 'pictures')
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
            self.input_text(*self.locators.TEASER_LINK, target_url)
        with allure.step("Ввод названия."):
            self.input_text(*self.locators.TEASER_TITLE, title)
        with allure.step("Ввод текста."):
            self.input_text(*self.locators.TEASER_TEXT, text)

    @allure.step("Нажатие на кнопку создания кампании.")
    def save_campaign(self):
        self.scroll_to_clickable_element(*self.locators.SUBMIT_BUTTON)
        self.get_clickable_element(*self.locators.SUBMIT_BUTTON).click()

    def creating_campaign(self, campaign_name):
        target_url = 'https://education.vk.campaign/'
        teaser_title = 'Qwadsfa'
        teaser_text = '1234153425234'
        with allure.step(
                f'Создание кампании с названием - {campaign_name}, url - {target_url}, '
                f'названием тизера - {teaser_title}, текстом тизера - {teaser_text}.'):
            self.select_category_traffic()
            self.input_url(target_url)
            self.input_campaign_name(campaign_name)
            self.select_social_characteristics()
            self.select_interests()
            self.select_ad_format()
            self.add_picture()
            self.fill_teaser_fields(target_url, teaser_title, teaser_text)
            self.save_campaign()
