import allure

from ui.locators.basic_locators import SegmentsPageLocators
from ui.pages.base_page import BasePage
from ui.pages.creating_segment_page import CreatingSegmentPage
from selenium.webdriver.common.by import By


class SegmentsPage(BasePage):
    locators = SegmentsPageLocators
    url = 'https://target-sandbox.my.com/segments/segments_list'

    @allure.step("Переход на страницу создания нового сегмента.")
    def go_to_creating_segment_page(self):
        self.get_visible_element(*self.locators.CREATE_SEGMENT_BUTTON).click()
        return CreatingSegmentPage(driver=self.driver)

    @allure.step("Проверка на то, что сегмент создан.")
    def is_segment_create(self, segment_name):
        required_segment_id = None
        self.open_page()
        self.is_element_present(*self.locators.CREATED_SEGMENTS)
        created_segments = self.driver.find_elements(*self.locators.CREATED_SEGMENTS)
        for segment in created_segments:
            segment_id = segment.get_attribute("data-test").split()[0].split('-')[-1]
            current_segment_name_locator_data_test = f'name-{segment_id}'
            current_segment_name_locator = f"[data-test^='{current_segment_name_locator_data_test}'] a"
            current_segment_name = self.get_clickable_element(By.CSS_SELECTOR,
                                                              current_segment_name_locator).get_attribute('title')
            if current_segment_name == segment_name:
                required_segment_id = segment_id
        return required_segment_id

    @allure.step("Удаление сегмента.")
    def remove_segment(self, segment_id):
        remove_segment_locator_data_test = f'remove-{segment_id}'
        remove_segment_locator = f"[data-test^='{remove_segment_locator_data_test}'] span"
        self.get_clickable_element(By.CSS_SELECTOR, remove_segment_locator).click()
        self.get_visible_element(*self.locators.SUBMIT_REMOVE_BUTTON).click()
