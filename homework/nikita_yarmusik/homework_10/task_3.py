number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))


def select_operator(funct):
    def wrapper(first, second):
        if first < 0 or second < 0:
            return funct(first, second, '*')
        elif first == second:
            return funct(first, second, '+')
        elif first > second:
            return funct(first, second, '-')
        elif first < second:
            return funct(first, second, '/')
        return None

    return wrapper


@select_operator
def calc(first, second, operation=None):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    else:
        raise ValueError('Invalid operation')


print(calc(number_1, number_2))
