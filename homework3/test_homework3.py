import pytest

from api.api_campaign import ApiCampaign
from api.api_segments import ApiSegments

from base import ApiBase


@pytest.mark.API
class TestApi(ApiBase):
    authorize = False

    def test_create_campaign(self):
        api_campaign = ApiCampaign(session=self.api_client.session)
        campaign_id = api_campaign.create_campaign_teaser()
        assert api_campaign.get_campaign(campaign_id=campaign_id, status='active'), \
            f'Кампании с ID - {campaign_id} нет в списке активных кампаний.'

        api_campaign.delete_campaign(campaign_id)
        assert api_campaign.get_campaign(campaign_id=campaign_id, status='deleted'), \
            f'После удаления кампания с ID - {campaign_id} не появилась в списке удаленных.'

    def test_create_segment(self):
        api_segment = ApiSegments(session=self.api_client.session)
        segment_id = api_segment.create_segment_with_type(object_type='remarketing_player')
        assert api_segment.is_segment(segment_id), f'Сегмента с ID {segment_id} нет в списке созданных сегментов.'
        api_segment.delete_segment(segment_id)
        assert not api_segment.is_segment(segment_id), \
            f'Сегмент с ID {segment_id} есть в списке созданных сегментов после удаления.'

    def test_create_segment_with_vk_group(self):
        group_link = 'https://vk.com/vkedu'

        api_segment = ApiSegments(session=self.api_client.session)
        group_id, group_object_id = api_segment.add_group(group_link)
        added_groups = api_segment.get_added_groups()
        assert api_segment.is_created_object_in_objects_list(group_id, added_groups), \
            f'Группы с ID - {group_id} нет в списке созданных групп.'

        segment_id = api_segment.create_segment_with_type(object_type='remarketing_vk_group', group_id=group_object_id)
        assert api_segment.is_segment(segment_id), f'Сегмента с ID {segment_id} нет в списке созданных сегментов.'
        api_segment.delete_segment(segment_id)
        assert not api_segment.is_segment(segment_id), \
            f'Сегмент с ID {segment_id} есть в списке созданных сегментов после удаления.'

        api_segment.delete_group(group_id)
        added_groups = api_segment.get_added_groups()
        assert not api_segment.is_created_object_in_objects_list(group_id, added_groups), \
            f'Группа с ID - {group_id} есть в списке созданных групп после удаления.'
