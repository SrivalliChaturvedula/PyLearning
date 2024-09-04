# @staticmethod
# @classmethod
# @property
# @functools.wraps
# These we will be using in oops concept

# We can add two decorators to the same function

def decorator(func):
    def wrapper():
        print("one decorator")
        func()
    return wrapper


def decorator2(func):
    def wrapper():
        print("second decorator")
        func()
    return wrapper


@decorator
@decorator2
def say_hello():
    print("Hello")

say_hello()