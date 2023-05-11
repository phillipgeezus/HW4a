from test import test
@test

def double(func):
    def wrapper():
        func()
        print("Let’s try that again!")
        func()
    return wrapper
