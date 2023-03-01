def generic_decorator(func):
    """Adds printing of generic messages to func"""

    def wrapper(*args, **kwargs):
        print("additional behavior before the function call")
        result = func(*args, **kwargs)
        print("additional behavior after the function call")
        return result

    return wrapper


@generic_decorator
def increment(num):
    """Increments num by 1"""
    return num + 1


@generic_decorator
def add_three(num_1, num_2, num_3):
    """Returns the sum of the three arguments"""
    return num_1 + num_2 + num_3


# testing functions
print(increment(3))
print(add_three(2, 3, 4))
help(add_three)

