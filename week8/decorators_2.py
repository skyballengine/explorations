def generic_decorator(func):
    """Adds printing of generic messages to func"""

    def wrapper():
        print("additional behavior before the function call")
        result = func()
        print("additional behavior after the function call")
        return result
    
    return wrapper


@generic_decorator
def greeting():
    """Returns a greeting"""
    return "hello world"


print(greeting())