import os
from sys import argv
from json import dumps

base_dir_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
file_path = os.path.join(base_dir_path, "access.log")
type_dict = {}
with open(file_path, 'r') as f:
    for line in f:
        arr = line.split()
        type_name = arr[5].strip('"')
        if len(type_name) > 10:
            continue
        if type_name in type_dict:
            type_dict[type_name] += 1
        else:
            type_dict[type_name] = 1

types_list = sorted(type_dict.items(), key=lambda item: item[1], reverse=True)

with open('total_requests_by_type_python.txt', 'w') as f:
    if '--json' in argv:
        json_list = []
        for el in types_list:
            json_list.append(dict(zip(("method", "count"), el)))
        print(f'{dumps(json_list)}', file=f)
    else:
        f.write('Total requests by type\n')
        for el in types_list:
            print(*el, sep=' - ', file=f, end='\n')
