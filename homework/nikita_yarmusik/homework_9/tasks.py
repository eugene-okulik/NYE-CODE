# Задание 1
import datetime

user_date = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(user_date, "%b %d, %Y - %H:%M:%S")

full_month = python_date.strftime("%B")
standard_date = python_date.strftime("%d.%m.%Y, %H:%M")

print(full_month, standard_date, sep="\n")

# Задание 2
temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
result = list(filter(lambda x: x > 28, temperatures))
max_temperature = max(temperatures)
min_temperature = min(temperatures)
mid_temperature = sum(temperatures) / len(temperatures)
print(max_temperature, min_temperature, mid_temperature, sep="\n")
