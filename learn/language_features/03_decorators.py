"""
Python decorators are functions that modify the behavior of another function or class.
They are a powerful tool for code reuse and separation of concerns, such as logging, access control, or caching.
"""


def my_decorator(func):
    def wrapper():
        print("Something before.")
        func()
        print("Something after.")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


# Usage
say_hello()
