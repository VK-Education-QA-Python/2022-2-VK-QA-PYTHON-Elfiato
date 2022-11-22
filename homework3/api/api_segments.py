from api.client import ApiClient
from api.builder import SegmentData


class ApiSegments(ApiClient):
    segment_url = 'https://target-sandbox.my.com/api/v2/remarketing/segments.json'
    segment_by_id_url = 'https://target-sandbox.my.com/api/v2/remarketing/segments/{0}.json'

    def create_segment(self, vk_group_id, object_type='remarketing_player'):
        data = SegmentData.get_segment_data(vk_group_id=vk_group_id, object_type=object_type)
        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken'],
        }
        res = self._request(method='POST', location=self.segment_url, headers=headers, json=data, jsonify=True)
        return res['id']

    def get_created_segments(self):
        params = {
            'fields': 'id, name, created'
        }
        return self._request(method='GET', location=self.segment_url, params=params, jsonify=True)

    def is_segment(self, segment_id):
        segment_link = self.segment_by_id_url.format(str(segment_id))
        res = self._request(method='GET', location=segment_link)
        return res.status_code == 200

    @staticmethod
    def is_created_object_in_objects_list(created_object_id, object_list):
        for el in object_list['items']:
            if el['id'] == created_object_id:
                return True
        return False

    def delete_segment(self, segment_id):
        delete_segment_link = self.segment_by_id_url.format(str(segment_id))

        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken']
        }
        self._request(method='DELETE', location=delete_segment_link, headers=headers)

    def get_group_id(self, group_link):
        get_group_id_link = 'https://target-sandbox.my.com/api/v2/vk_groups.json'

        params = {'_q': group_link}
        res = self._request(method='GET', location=get_group_id_link, params=params, jsonify=True)
        return res['items'][0]['id']

    def add_group(self, group_link):
        add_group_link = 'https://target-sandbox.my.com/api/v2/remarketing/vk_groups/bulk.json'

        group_object_id = self.get_group_id(group_link)
        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken']
        }
        data = {
            'items': [{'object_id': group_object_id}]
        }
        res = self._request(method='POST', headers=headers, json=data, jsonify=True, location=add_group_link)
        return res['items'][0]['id'], group_object_id

    def get_added_groups(self):
        vk_groups_link = 'https://target-sandbox.my.com/api/v2/remarketing/vk_groups.json'

        params = {
            'fields': 'id,name,url'
        }
        return self._request(method='GET', location=vk_groups_link, params=params, jsonify=True)

    def create_segment_with_type(self, object_type='remarketing_player', group_id=None):
        return self.create_segment(vk_group_id=group_id, object_type=object_type)

    def delete_group(self, group_id):
        delete_group_link = f'https://target-sandbox.my.com/api/v2/remarketing/vk_groups/{group_id}.json'

        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken']
        }
        self._request(method='DELETE', headers=headers, location=delete_group_link)
