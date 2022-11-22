import os

from api.builder import CampaignTeaserData
from api.client import ApiClient


class ApiCampaign(ApiClient):
    url = 'https://target-sandbox.my.com/api/v2/campaigns.json'
    campaign_by_id_url = 'https://target-sandbox.my.com/api/v2/campaigns/{0}.json'

    def post_picture(self, picture_name):
        send_picture_link = 'https://target-sandbox.my.com/api/v2/content/static.json'

        repo_root = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
        file_path = os.path.join(repo_root, 'pictures')
        file_path = os.path.join(file_path, picture_name)

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

    def get_campaign_data_json(self):
        teaser_data = CampaignTeaserData()
        target_url_id = self.post_target_url(teaser_data.target_url)
        picture_id = self.post_picture(teaser_data.picture_name)
        campaign_data = teaser_data.get_campaign_data(target_url_id, picture_id)
        return campaign_data

    def create_campaign_teaser(self):
        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken'],
        }
        campaign_data = self.get_campaign_data_json()

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

    def get_campaign(self, campaign_id, status='active'):
        campaign_by_id_url = self.campaign_by_id_url.format(str(campaign_id))

        params = {
            'fields': 'id, name, status',
        }

        res = self._request(method='GET', location=campaign_by_id_url, params=params, jsonify=True)

        return res['status'] == status

    def delete_campaign(self, campaign_id):
        campaign_by_id_url = self.campaign_by_id_url.format(str(campaign_id))

        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken'],
        }

        res = self._request(method='DELETE', location=campaign_by_id_url, headers=headers)
        assert res.status_code == 204, f'При удалении созданной компании пришел код овтета {res.status_code}.'
