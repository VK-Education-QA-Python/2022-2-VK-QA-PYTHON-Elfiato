import time

import pytest

from api.api_campaign import ApiCampaign
from api.api_segments import ApiSegments

from base import ApiBase


@pytest.mark.API
class TestApi(ApiBase):
    authorize = False

    def test_create_campaign(self):
        campaign_name = 'Name' + '_' + str(time.time())

        api_campaign = ApiCampaign(session=self.api_client.session)
        campaign_id = api_campaign.create_campaign_teaser(campaign_name)
        active_campaigns = api_campaign.get_campaigns(status='active')
        assert api_campaign.is_created_campaign_in_campaigns_list(campaign_id, active_campaigns), \
            f'Кампании с ID - {campaign_id} нет в списке активных кампаний.'

        api_campaign.delete_campaign(campaign_id)
        deleted_campaigns = api_campaign.get_campaigns(status='deleted')
        assert api_campaign.is_created_campaign_in_campaigns_list(campaign_id, deleted_campaigns), \
            f'После удаления кампания с ID - {campaign_id} не появилась в списке удаленных.'

    def test_create_segment(self):
        segment_name = 'Segment' + '_' + str(time.time())

        api_segment = ApiSegments(session=self.api_client.session)
        api_segment.create_segment_with_type(segment_name, object_type='remarketing_player')

    def test_create_segment_with_vk_group(self):
        group_link = 'https://vk.com/vkedu'
        segment_name = 'Segment' + '_' + str(time.time())

        api_segment = ApiSegments(session=self.api_client.session)
        group_id, group_object_id = api_segment.add_group(group_link)
        added_groups = api_segment.get_added_groups()
        assert api_segment.is_created_object_in_objects_list(group_id, added_groups), \
            f'Группы с ID - {group_id} нет в списке созданных групп.'

        api_segment.create_segment_with_type(segment_name, object_type='remarketing_vk_group', group_id=group_object_id)

        api_segment.delete_group(group_id)
        added_groups = api_segment.get_added_groups()
        assert not api_segment.is_created_object_in_objects_list(group_id, added_groups), \
            f'Группа с ID - {group_id} есть в списке созданных групп после удаления.'
