def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a // b

def mess(text):
    return text * 3


if __name__ == '__main__':
    a, b = 123, 256
    print(plus(a, b))
    print(minus(a, b))
    print(mul(a, b))
    print(div(a, b))
    text = 'Hello! '
    print(mess(text))