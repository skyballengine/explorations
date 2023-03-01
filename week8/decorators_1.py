def generic_decorator(func):
    """Adds printing of generic messages to func"""

    def wrapper():
        print("additional behavior before the function call")
        func()
        print("additional behavior after the function call")

    return wrapper


def greeting():
    """Prints a greeting"""
    print("hello world")


greeting = generic_decorator(greeting)

greeting()