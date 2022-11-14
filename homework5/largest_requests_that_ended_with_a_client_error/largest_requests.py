import os
from sys import argv
from json import dumps

base_dir_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
file_path = os.path.join(base_dir_path, "access.log")
base_url = 'http://almhuette-raith.at/'
all_requests = []
with open(file_path, 'r') as f:
    for line in f:
        arr = line.split()
        url = arr[6]
        if url.startswith(base_url):
            url = url[len(base_url) - 1:]
        status = arr[8]
        ip_address = arr[0]
        request_size = arr[9]
        if status.startswith('4'):
            all_requests.append((url, status, int(request_size), ip_address))

all_requests.sort(key=lambda item: (item[2], item[0]), reverse=True)

with open('largest_requests_that_ended_with_a_client_error_python.txt', 'w') as f:
    if '--json' in argv:
        json_list = []
        for i in range(5):
            json_list.append(dict(zip(("url", "status", "request_size", "ip_address"), all_requests[i])))
        print(f'{dumps(json_list)}', file=f)
    else:
        f.write('Largest requests that ended with a client error\n')
        for i in range(5):
            print(*all_requests[i], sep='\n', file=f)
