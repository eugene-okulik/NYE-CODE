def repeat_me(funct):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)
        for _ in range(count):
            funct(*args, **kwargs)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('hello', count=2)
print('-------------')
example('hello')
