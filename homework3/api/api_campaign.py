import os

from api.client import ApiClient


class ApiCampaign(ApiClient):
    url = 'https://target-sandbox.my.com/api/v2/campaigns.json'

    def post_picture(self, picture_name):
        send_picture_link = 'https://target-sandbox.my.com/api/v2/content/static.json'

        base_dir = '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
        file_path = os.path.join(base_dir, f'pictures\\{picture_name}')

        data = {"width": 0, "height": 0}
        file = {'file': open(file_path, 'rb')}
        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken'],
        }
        res = self._request(method='POST', location=send_picture_link, headers=headers,
                            files=file, data=data, jsonify=True)
        return res['id']

    def post_target_url(self, target_url):
        send_target_link_url = 'https://target-sandbox.my.com/api/v1/urls/'

        params = {'url': target_url}
        res = self._request(method='GET', location=send_target_link_url, params=params, jsonify=True)
        return res['id']

    def get_campaign_data_json(self, campaign_name, target_url, teaser_title, teaser_text, picture):
        target_url_id = self.post_target_url(target_url)
        picture_id = self.post_picture(picture)
        campaign_data = {"name": campaign_name,
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
                                         "text": teaser_title},
                                     "text_90": {
                                         "text": teaser_text},
                                 },
                                 "content": {
                                     "image_90x75": {
                                         "id": picture_id
                                     }
                                 },
                             }
                         ]}
        return campaign_data

    def create_campaign_teaser(self, campaign_name):
        target_url = 'https://education.vk.campaign/'
        teaser_title = 'Qwadsfa'
        teaser_text = '1234153425234'
        picture_name = 'teaser.png'

        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken'],
            'X-Campaign-Create-Action': 'new',
        }
        campaign_data = self.get_campaign_data_json(campaign_name, target_url, teaser_title, teaser_text, picture_name)

        res = self._request(method='POST', location=self.url, headers=headers, json=campaign_data, jsonify=True)
        return res['id']

    def get_campaigns(self, status='active'):
        params = {
            'fields': 'id, name, status',
            'sorting': '-id',
            '_status__in': status,
        }
        res = self._request(method='GET', location=self.url, params=params, jsonify=True)
        return res

    def delete_campaign(self, campaign_id):
        mass_action_url = 'https://target-sandbox.my.com/api/v2/campaigns/mass_action.json'

        data = [
            {'id': campaign_id, 'status': 'deleted'},
        ]
        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken'],
        }
        res = self._request(method='POST', location=mass_action_url, json=data, headers=headers)
        assert res.status_code == 204, f'При удалении созданной компании пришел код овтета {res.status_code}.'

    @staticmethod
    def is_created_campaign_in_campaigns_list(created_campaign_id, campaigns):
        for campaign in campaigns['items']:
            if campaign['id'] == created_campaign_id:
                return True
        return False
