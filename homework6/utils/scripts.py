import os


class BaseScripts:
    def __init__(self, filename):
        file_path = self.get_log_file_path(filename)
        with open(file_path, 'r') as f:
            self.file = f.read().split('\n')[:-1]

    @staticmethod
    def get_log_file_path(filename):
        dir_path = os.path.dirname(__file__)
        return os.path.join(dir_path, filename)

    def total_requests(self):
        counter = 0
        for l in self.file:
            arr = l.split()
            if arr[7].startswith('HTTP') and '/' in arr[6]:
                counter += 1
        return [counter]

    def most_frequent_requests(self, amount):
        base_url = 'http://almhuette-raith.at/'
        url_dict = {}
        for l in self.file:
            arr = l.split()
            url = arr[6]
            if url.startswith(base_url):
                url = url[len(base_url) - 1:]
            if url in url_dict:
                url_dict[url] += 1
            else:
                url_dict[url] = 1

        return sorted(url_dict.items(), key=lambda item: item[1], reverse=True)[:amount]

    def total_requests_by_type(self):
        type_dict = {}
        for line in self.file:
            arr = line.split()
            type_name = arr[5].strip('"')
            if len(type_name) > 10:
                continue
            if type_name in type_dict:
                type_dict[type_name] += 1
            else:
                type_dict[type_name] = 1

        return sorted(type_dict.items(), key=lambda item: item[1], reverse=True)

    def largest_requests(self, amount):
        base_url = 'http://almhuette-raith.at/'
        all_requests = []
        for line in self.file:
            arr = line.split()
            url = arr[6]
            if url.startswith(base_url):
                url = url[len(base_url) - 1:]
            status = arr[8]
            ip_address = arr[0]
            request_size = arr[9]
            if status.startswith('4'):
                if '%' in url:
                    url = '%%'.join(url.split('%'))
                all_requests.append((url, int(status), int(request_size), ip_address))

        return sorted(all_requests, key=lambda item: (item[2], item[0]), reverse=True)[:amount]

    def users_with_server_error_requests(self, amount):
        user_dict = {}
        for line in self.file:
            arr = line.split()
            status = arr[8]
            ip_address = arr[0]
            if status.startswith('5'):
                if ip_address not in user_dict:
                    user_dict[ip_address] = 1
                else:
                    user_dict[ip_address] += 1

        return sorted(user_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)[:amount]
