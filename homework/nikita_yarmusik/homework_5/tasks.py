person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person[0], person[1], person[2], person[3], person[4]


text = 'результат операции: 42'
number = int(text[text.index(':') + 1:]) + 10
print(number)


students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print(f'Students {", ".join(students)} study these subjects {", ".join(subjects)}')