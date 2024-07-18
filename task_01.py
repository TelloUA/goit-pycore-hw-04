import re
from os import path

def total_salary(file_path: str):
    # check the file
    if not path.exists(file_path):
        return None, None
    
    # setup variables
    total = 0
    counter = 0

    #read the file
    with open(file=file_path, mode='r', encoding='utf-8') as fh:
        while True:
            line = fh.readline().strip()
            if not line:
                break
            # split line and update data
            data = re.search(r'(\w*),(\d*)', line)
            # check find and valid value
            if data is None or data[2] == '':
                return None, None
            parts = line.split(',')
            total += (int)(parts[1])
            counter += 1
    average = total / counter

    return total, "{:.2f}".format(average)

total, average = total_salary('task_01_file.txt')
if total is None or average is None:
    print('Функція закінчилась з помилкою')
else:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# total_salary('task_01_file.txt')