import os
from datetime import datetime, timedelta


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
okulik_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def split_lines(text):
    return text.splitlines()


def select_date(your_text):
    start = your_text.find('. ') + 2
    end = your_text.find(' - ')
    return your_text[start:end]


def parse_date(your_date):
    return datetime.strptime(your_date, '%Y-%m-%d %H:%M:%S.%f')


lines = split_lines(read_file(okulik_path))
line_1, line_2, line_3 = lines[0], lines[1], lines[2]

print(parse_date(select_date(line_1)) + timedelta(weeks=1))
print(parse_date(select_date(line_2)).weekday())

now = datetime.now()
print((now - parse_date(select_date(line_3))).days)
