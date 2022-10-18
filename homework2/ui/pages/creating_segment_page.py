from ui.locators.basic_locators import CreatingSegmentLocators
from ui.pages.base_page import BasePage


class CreatingSegmentPage(BasePage):
    locators = CreatingSegmentLocators
    url = 'https://target-sandbox.my.com/segments/segments_list/new'

    def select_category_apps(self):
        self.get_clickable_element(*self.locators.APPS_CATEGORY).click()

    def set_new_segment_checkbox_true(self):
        self.get_clickable_element(*self.locators.SEGMENT_CHECKBOX).click()

    def click_submit_button(self):
        self.get_clickable_element(*self.locators.SUBMIT_SEGMENT_BUTTON).click()

    def input_name(self, name):
        segment_name_field = self.get_present_element(*self.locators.SEGMENT_NAME_FORM)
        segment_name_field.clear()
        segment_name_field.send_keys(name)

    def create_new_segment(self):
        self.get_clickable_element(*self.locators.CREATE_NEW_SEGMENT_BUTTON).click()

    def select_category_groups(self):
        self.get_clickable_element(*self.locators.GROUPS_CATEGORY).click()
