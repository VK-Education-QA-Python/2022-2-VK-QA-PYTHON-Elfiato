import allure

from ui.locators.basic_locators import GroupListPageLocators
from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class GroupListPage(BasePage):
    locators = GroupListPageLocators
    url = 'https://target-sandbox.my.com/segments/groups_list'

    @allure.step("Ввод ссылки на группу.")
    def input_group_url(self, url):
        input_field = self.get_visible_element(*self.locators.GROUP_URL_INPUT_FIELD)
        input_field.clear()
        input_field.send_keys(url)

    @allure.step("Выбор всех групп в списке преложенных.")
    def select_all_group(self):
        self.get_clickable_element(*self.locators.SELECT_ALL).click()

    @allure.step("Нажатие на кнопку 'Добавить выбранные.'")
    def click_add_selected_button(self):
        self.get_clickable_element(*self.locators.ADD_SELECTED_ITEMS_BUTTON).click()

    @allure.step("Получение id созданной группы.")
    def get_added_group_id(self, name):
        required_group_cid = None
        self.open_page()
        self.is_element_present(*self.locators.ALL_ADDED_GROUPS)
        added_groups = self.driver.find_elements(*self.locators.ALL_ADDED_GROUPS)
        for group in added_groups:
            cid = group.get_attribute("cid")
            current_name_locator = f"[cid='{cid}'] .js-cell-name span"
            current_name = self.get_present_element(By.CSS_SELECTOR, current_name_locator).get_attribute("title")
            if name == current_name:
                required_group_cid = cid
        return required_group_cid

    @allure.step("Удаление группы.")
    def remove_group(self, cid):
        remove_button_selector = f"[cid='{cid}'] .icon-cross"
        self.get_visible_element(By.CSS_SELECTOR, remove_button_selector).click()
        self.get_visible_element(*self.locators.SUBMIT_REMOVE_BUTTON).click()
