# Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел


x, y = int(input()), int(input())
print(f'Среднее арифметическое: {(x+y) / 2}')
print(f'Среднее геометрическое: {(x*y) ** 0.5}')