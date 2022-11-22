import uuid


class CampaignTeaserData:

    def __init__(self, teaser_title='Qwadsfa', teaser_text='1234153425234', picture_name='teaser.png',
                 target_url='https://education.vk.campaign/'):
        self.teaser_title = teaser_title
        self.teaser_text = teaser_text
        self.picture_name = picture_name
        self.target_url = target_url

    def __repr__(self):
        return f'teaser_title - "{self.teaser_title}", teaser_text - "{self.teaser_text}", ' \
               f'picture_name - "{self.picture_name}", target_url - "{self.target_url}"'

    def get_campaign_data(self, target_url_id, picture_id):
        campaign_data = {"name": str(uuid.uuid4()),
                         'package_id': '1029',
                         'objective': "traffic",
                         "banners": [
                             {
                                 "urls": {
                                     "primary": {
                                         "id": target_url_id}
                                 },
                                 "textblocks": {
                                     "title_25": {
                                         "text": self.teaser_title},
                                     "text_90": {
                                         "text": self.teaser_text},
                                 },
                                 "content": {
                                     "image_90x75": {
                                         "id": picture_id
                                     }
                                 },
                             }
                         ]}
        return campaign_data


class SegmentData:

    @staticmethod
    def get_segment_data(vk_group_id, object_type):
        object_types_params = {'remarketing_player': {'type': 'positive',
                                                      'left': '365',
                                                      'right': '0'},
                               'remarketing_vk_group': {'type': 'positive',
                                                        'source_id': vk_group_id}}
        data = {
            'name': str(uuid.uuid4()),
            'pass_condition': 1,
            'relations': [
                {'object_type': object_type,
                 'params': object_types_params[object_type]
                 },
            ]
        }
        return data
