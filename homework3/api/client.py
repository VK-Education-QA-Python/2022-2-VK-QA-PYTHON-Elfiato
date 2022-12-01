import requests


class RespondErrorException(Exception):
    pass


class ApiClient:
    url = 'https://target-sandbox.my.com'

    def __init__(self, base_url=None, session=None):
        if base_url is None:
            base_url = self.url
        self.url = base_url

        if session is None:
            session = requests.Session()
        self.session = session

    def login(self):
        location = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
        email = 'jo.ry@mail.ru'
        password = '12345A'

        continue_url = 'https://target-sandbox.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email'
        refer = 'https://target-sandbox.my.com'

        data = {'email': email, 'password': password, 'continue': continue_url}
        headers = {'Referer': refer}
        res = self._request(method='POST', location=location, data=data, allow_redirects=False, headers=headers)
        while res.status_code != 200:
            location = res.headers['Location']
            res = self._request(method='GET', location=location, allow_redirects=False)

        self._request(method='GET', location='https://target-sandbox.my.com/csrf')

    def _request(self, method, location, headers=None, data=None, params=None, allow_redirects=False, files=None,
                 jsonify=None, json=None):
        response = self.session.request(method=method, url=location, headers=headers, data=data, params=params,
                                        allow_redirects=allow_redirects, files=files, json=json)
        if jsonify:
            return response.json()
        return response
