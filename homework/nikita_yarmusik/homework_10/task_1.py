def finish_me(funct):
    def wrapper(*args, **kwargs):
        funct(*args, **kwargs)
        print('finished')

    return wrapper


@finish_me
def do_something():
    print('do something')


do_something()
