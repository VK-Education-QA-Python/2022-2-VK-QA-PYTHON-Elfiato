import time

import pytest

from base import BaseCaseLogIn


@pytest.mark.UI
class Test(BaseCaseLogIn):
    def test_make_campaign(self):
        campaign_name = 'QWERTY' + '_' + str(time.time())
        target_url = 'https://education.vk.campaign/'
        teaser_title = 'Qwadsfa'
        teaser_text = '1234153425234'
        dashboard_page = self.dashboard_page
        dashboard_page.is_opened()
        campaign_page = dashboard_page.go_to_creating_campaign_page()
        campaign_page.select_category_traffic()
        campaign_page.input_url(target_url)
        campaign_page.input_campaign_name(campaign_name)
        campaign_page.select_social_characteristics()
        campaign_page.select_interests()
        campaign_page.select_ad_format()
        campaign_page.add_picture()
        campaign_page.fill_teaser_fields(target_url, teaser_title, teaser_text)
        campaign_page.save_campaign()
        dashboard_page.is_opened()
        assert dashboard_page.is_campaign_created(
            campaign_name), f'Компании с именем "{campaign_name}" нет в списке созданных компаний.'

    def test_create_segment(self):
        segment_page = self.segment_page
        segment_page.open_page()
        creating_segment_page = segment_page.go_to_creating_segment_page()
        segment_name = self.create_segment(creating_segment_page,
                                           creating_segment_page.select_category_apps)
        assert segment_page.is_segment_create(
            segment_name), f'Сегмента с именем "{segment_name}" нет в списке созданных сегментов.'

    def test_create_segment_with_group(self):
        url = 'https://vk.com/vkedu'
        group_name = 'VK Образование'
        group_list_page = self.group_list_page
        group_list_page.open_page()
        group_list_page.input_group_url(url)
        group_list_page.select_all_group()
        group_list_page.click_add_selected_button()
        group_id = group_list_page.get_added_group_id(group_name)

        segment_page = self.segment_page
        segment_page.open_page()
        creating_segment_page = segment_page.go_to_creating_segment_page()
        segment_name = self.create_segment(creating_segment_page,
                                           creating_segment_page.select_category_groups)
        segment_id = segment_page.is_segment_create(segment_name)
        assert segment_id, f'Сегмента с именем "{segment_name}" нет в списке созданных сегментов.'

        segment_page.remove_segment(segment_id)
        assert not segment_page.is_segment_create(
            segment_name), f'После удаления, сегмент с именем "{segment_name}" ' \
                           f'все еще есть в списке созданных сегментов.'

        group_list_page.open_page()
        group_list_page.remove_group(group_id)
        assert not group_list_page.get_added_group_id(
            group_name), f'После удаления, группа с именем {group_name} все еще есть в списке добавленных групп.'
