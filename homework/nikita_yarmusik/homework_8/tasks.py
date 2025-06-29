from random import randint


def calculate_salary():
    salary = int(input('Введите ЗП: '))
    bonus = bool(randint(0, 1))
    money = randint(0, 1000)

    total = salary + money if bonus else salary
    print(f"{salary}, {bonus} - '${total}'")


calculate_salary()


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = fibonacci_generator()
positions = [5, 200, 1000, 10000]
i = 1

for num in gen:
    if i in positions:
        print(num)

    if i >= max(positions):
        break
    i += 1
