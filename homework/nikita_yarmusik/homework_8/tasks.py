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


fibonacci_generator()
