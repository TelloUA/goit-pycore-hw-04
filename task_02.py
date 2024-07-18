import pprint
from os import path

def get_cats_info(file_path: str):
    if not path.exists(file_path):
        return False
    
    keys_list = ['id', 'name', 'age']
    result = []
    with open(file=file_path, mode='r', encoding='utf-8') as fh:
        while True:
            line = fh.readline().strip()
            if not line:
                break
            cat_list = line.split(',')
            cat_dict = dict(zip(keys_list, cat_list))
            result.append(cat_dict)
    
    return result

cats_info = get_cats_info("task_02_file.txt")
pprint.pp(cats_info)
