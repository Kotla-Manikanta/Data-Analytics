
def decorator(func):
    def wrapper():
        print('before calling')
        func()
        print('after calling')
    return wrapper

@decorator # greet=decorator(greet)
def greet():
    print('hello')
greet()

