import functools

def double(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func()
        print("Let's try that again!")
        func()
    return wrapper
