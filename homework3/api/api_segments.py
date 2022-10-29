from api.client import ApiClient


class ApiSegments(ApiClient):
    url = 'https://target-sandbox.my.com/api/v2/remarketing/segments.json'

    def create_segment(self, segment_name, vk_group_id, object_type='remarketing_player'):
        object_types_params = {'remarketing_player': {'type': 'positive',
                                                      'left': '365',
                                                      'right': '0'},
                               'remarketing_vk_group': {'type': 'positive',
                                                        'source_id': vk_group_id}}
        data = {
            'name': segment_name,
            'pass_condition': 1,
            'relations': [
                {'object_type': object_type,
                 'params': object_types_params[object_type]
                 },
            ]
        }
        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken'],
        }
        res = self._request(method='POST', location=self.url, headers=headers, json=data, jsonify=True)
        return res['id']

    def get_created_segments(self):
        params = {
            'fields': 'id, name, created'
        }
        return self._request(method='GET', location=self.url, params=params, jsonify=True)

    @staticmethod
    def is_created_object_in_objects_list(created_object_id, object_list):
        for el in object_list['items']:
            if el['id'] == created_object_id:
                return True
        return False

    def delete_segment(self, segment_id):
        delete_segment_link = 'https://target-sandbox.my.com/api/v1/remarketing/mass_action/delete.json'

        data = [
            {'source_id': segment_id, 'source_type': 'segment'}
        ]
        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken']
        }
        self._request(method='POST', location=delete_segment_link, json=data, headers=headers)

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

    def create_segment_with_type(self, segment_name, object_type='remarketing_player', group_id=None):
        segment_id = self.create_segment(segment_name, vk_group_id=group_id, object_type=object_type)
        created_segments = self.get_created_segments()
        assert self.is_created_object_in_objects_list(segment_id, created_segments), \
            f'Сегмента с ID {segment_id} нет в списке созданных сегментов.'

        self.delete_segment(segment_id)
        created_segments = self.get_created_segments()
        assert not self.is_created_object_in_objects_list(segment_id, created_segments), \
            f'Сегмент с ID {segment_id} есть в списке созданных сегментов после удаления.'

    def delete_group(self, group_id):
        delete_group_link = f'https://target-sandbox.my.com/api/v2/remarketing/vk_groups/{group_id}.json'

        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken']
        }
        self._request(method='DELETE', headers=headers, location=delete_group_link)
