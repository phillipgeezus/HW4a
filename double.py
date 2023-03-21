from double import double
@timestamp

def greet():
    print('Hello World!')
def print_text(text):
    return text.upper()
print(print_text('Hello'))
yell = print_text
print(yell('Hello'))

def main():
    greet()

main()
