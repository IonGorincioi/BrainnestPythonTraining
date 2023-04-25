# A decorator that repeats a function call a specified number of times

def wrapper(function):
    def inner(*args, **kwargs):
        print("Hello world!")
        function(*args, **kwargs)
        print("Hello world!")
    return inner

@wrapper
def my_function():
    print("Hello world!")

my_function()