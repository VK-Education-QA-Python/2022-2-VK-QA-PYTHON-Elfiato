import time

import allure
import pytest

from _pytest.fixtures import FixtureRequest

from base import BaseCaseLogIn


@pytest.mark.UI
class Test(BaseCaseLogIn):
    @allure.title("Тест на создание кампании.")
    @allure.description("Создание кампании с типом 'тизер' и проверка на то, что она появилась в списке кампаний.")
    def test_make_campaign(self, request: FixtureRequest):
        campaign_name = 'QWERTY' + '_' + str(time.time())
        with allure.step("Открываем страницу с списком кампаний и проверяем, что она открыта."):
            dashboard_page = request.getfixturevalue('dashboard_page')
            dashboard_page.is_opened()
        campaign_page = dashboard_page.go_to_creating_campaign_page()
        campaign_page.creating_campaign(campaign_name)
        with allure.step("Проверяем, что открылась страница с списком кампаний."):
            dashboard_page.is_opened()
        assert dashboard_page.is_campaign_created(
            campaign_name), f'Кампании с именем "{campaign_name}" нет в списке созданных кампаний.'

    @allure.title("Тест на создание сегмента.")
    @allure.description("Создание сегмента с типом 'Приложения и игры в соцсетях' и проверка на то, что он создан.")
    def test_create_segment(self, request: FixtureRequest):
        with allure.step("Открываем страницу с списком сегментов."):
            segment_page = request.getfixturevalue('segment_page')
            segment_page.open_page()
        creating_segment_page = segment_page.go_to_creating_segment_page()
        segment_name = creating_segment_page.create_segment(creating_segment_page.select_category_apps)
        assert segment_page.is_segment_create(
            segment_name), f'Сегмента с именем "{segment_name}" нет в списке созданных сегментов.'

    @allure.title("Тест на создание сегмента.")
    @allure.description("Создание сегмента с типом 'Группы OK и VK' и проверка на то, что он создан, "
                        "затем удалить созданный сегмент и добавленный источник данных.")
    def test_create_segment_with_group(self, request: FixtureRequest):
        group_name = 'VK Образование'
        with allure.step("Открываем страницу Групп ОК и ВК."):
            group_list_page = request.getfixturevalue('group_list_page')
            group_list_page.open_page()
        group_list_page.add_group()
        group_id = group_list_page.get_added_group_id(group_name)

        with allure.step("Переходим на страницу с списком сегментов."):
            segment_page = request.getfixturevalue('segment_page')
            segment_page.open_page()
        creating_segment_page = segment_page.go_to_creating_segment_page()
        segment_name = creating_segment_page.create_segment(creating_segment_page.select_category_groups)
        segment_id = segment_page.is_segment_create(segment_name)
        assert segment_id, f'Сегмента с именем "{segment_name}" нет в списке созданных сегментов.'
        segment_page.remove_segment(segment_id)
        assert not segment_page.is_segment_create(
            segment_name), f'После удаления, сегмент с именем "{segment_name}" ' \
                           f'все еще есть в списке созданных сегментов.'
        with allure.step("Переходим на страницу источников."):
            group_list_page.open_page()
        group_list_page.remove_group(group_id)
        assert not group_list_page.get_added_group_id(
            group_name), f'После удаления, группа с именем {group_name} все еще есть в списке добавленных групп.'
