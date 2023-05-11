import time

def timestamp(func):
    def wrapper():
        print(time.ctime())
        result = func()
        return result
    return wrapper
