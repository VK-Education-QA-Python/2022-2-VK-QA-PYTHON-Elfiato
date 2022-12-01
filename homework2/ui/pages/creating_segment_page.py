import time

import allure

from ui.locators.basic_locators import CreatingSegmentLocators
from ui.pages.base_page import BasePage


class CreatingSegmentPage(BasePage):
    locators = CreatingSegmentLocators
    url = 'https://target-sandbox.my.com/segments/segments_list/new'

    @allure.step("Выбор категории -  Приложения и игры.")
    def select_category_apps(self):
        self.get_clickable_element(*self.locators.APPS_CATEGORY).click()

    @allure.step("Установка галочки 'Игравшие и платившие на платформе.'")
    def set_new_segment_checkbox_true(self):
        self.get_clickable_element(*self.locators.SEGMENT_CHECKBOX).click()

    @allure.step("Нажатие кнопки добавления сегмента.")
    def click_submit_button(self):
        self.get_clickable_element(*self.locators.SUBMIT_SEGMENT_BUTTON).click()

    @allure.step("Нажатие кнопки создания сегмента.")
    def create_new_segment(self):
        self.get_clickable_element(*self.locators.CREATE_NEW_SEGMENT_BUTTON).click()

    @allure.step("Выбор категории -  Группы ОК и ВК.")
    def select_category_groups(self):
        self.get_clickable_element(*self.locators.GROUPS_CATEGORY).click()

    def create_segment(self, category):
        segment_name = 'Segm' + '_' + str(time.time())
        category()
        self.set_new_segment_checkbox_true()
        self.click_submit_button()
        self.input_text(*self.locators.SEGMENT_NAME_FORM, segment_name)
        self.create_new_segment()
        return segment_name
