import pytest
import locators
from base import Base

MAIN_PAGE = "https://target-sandbox.my.com/"
LOGIN = 'jo.ry@mail.ru'
PASSWORD = '12345A'
NAME = 'Евгений'


@pytest.mark.UI
@pytest.mark.parametrize('login, password',
                         [(LOGIN, PASSWORD),
                          pytest.param('1' + LOGIN, PASSWORD,
                                       marks=pytest.mark.xfail(reason='Invalid login, valid password')),
                          pytest.param(LOGIN, PASSWORD + '1',
                                       marks=pytest.mark.xfail(reason='Valid login, invalid password')),
                          ])
def test_login(driver, login, password):
    page = Base(driver, MAIN_PAGE)
    page.open()
    page.login_func(login, password)
    assert page.is_element_present(*locators.USER_NAME_BUTTON), 'Авторизация не произведена.'


@pytest.mark.UI
def test_logout(driver):
    page = Base(driver, MAIN_PAGE)
    page.open()
    page.login_func(LOGIN, PASSWORD)
    username_button = page.get_present_element(*locators.USER_NAME_BUTTON)
    username_button.click()
    page.move_to_present_element(*locators.SHOWN_RIGHT_MENU)
    logout_button = page.get_present_element(*locators.LOGOUT_BUTTON)
    logout_button.click()
    assert page.is_element_present(*locators.LOGIN_BUTTON_IN_HEADER), 'Выход из системы не произведен.'


@pytest.mark.UI
def test_change_profile_information(driver):
    page = Base(driver, MAIN_PAGE)
    page.open()
    page.login_func(LOGIN, PASSWORD)
    profile_button = page.get_clickable_element(*locators.PROFILE_BUTTON)
    profile_button.click()
    name_field = page.get_clickable_element(*locators.NAME_FIELD)
    name_field.clear()
    name_field.send_keys(NAME)
    save_button = page.get_present_element(*locators.SAVE_BUTTON)
    save_button.click()
    assert page.is_element_visible(
        *locators.SUCCESS_NOTIFICATION), 'Оповещение об успешном сохранении данных профиля не появилось ' \
                                         'после нажатия кнопки "Сохранить".'


@pytest.mark.UI
@pytest.mark.parametrize('locator, label',
                         [(locators.PROFILE_BUTTON, locators.PROFILE_CATEGORY_LABEL),
                          (locators.BILL_BUTTON, locators.BILL_CATEGORY_LABEL)])
def test_go_to_center_module_categories(driver, locator, label):
    page = Base(driver, MAIN_PAGE)
    page.open()
    page.login_func(LOGIN, PASSWORD)
    categories_button = page.get_clickable_element(*locator)
    categories_button.click()
    assert page.is_element_present(*label), f'Переход в категорию с локатором {locator} не произведен.'
