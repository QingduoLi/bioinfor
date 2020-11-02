def func1(msg, count):
    def inner():
        print(msg * count)
    return inner()

new_func = func1("ok",3)
