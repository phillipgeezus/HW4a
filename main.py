from double import double

@double
def greet():
    print('Hello World!')

def test():
    greet()

if __name__ == "__test__":
    test()
