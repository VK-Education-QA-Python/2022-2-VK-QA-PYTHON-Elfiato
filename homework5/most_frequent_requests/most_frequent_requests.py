import os
from sys import argv
from json import dumps

base_dir_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
file_path = os.path.join(base_dir_path, "access.log")
base_url = 'http://almhuette-raith.at/'
url_dict = {}
with open(file_path, 'r') as f:
    for l in f:
        arr = l.split()
        url = arr[6]
        if url.startswith(base_url):
            url = url[len(base_url) - 1:]
        if url in url_dict:
            url_dict[url] += 1
        else:
            url_dict[url] = 1

url_list = sorted(url_dict.items(), key=lambda item: item[1], reverse=True)

with open('most_frequent_requests_python.txt', 'w') as f:
    if '--json' in argv:
        json_list = []
        for i in range(10):
            json_list.append(dict(zip(("url", "count"), url_list[i])))
        print(f'{dumps(json_list)}', file=f)
    else:
        f.write('Most frequent requests\n')
        for i in range(10):
            print(*url_list[i], sep='\n', file=f)
