import functools

"""In general decorators are very useful for adding behavior to a function that isn't really part of its primary 
purpose, and which you might want to apply to a number of different functions. Other examples include printing 
information about a function for debugging purposes, making authentication checks, doing input validation, 
etc. It's helpful to be able to add the extra behavior, but keep the definition of that behavior separate from the 
functions' definitions, since copy-pasting the code for the additional behavior into a bunch of different functions 
would clutter up their definitions and also be rather tedious. And if you want to update the added behavior, 
you only need to do it in one place instead of across many functions."""

def func_args_print(func):
    """Prints out the values of the parameters"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            print(arg)
        result = func(*args, **kwargs)
        return result

    return wrapper


@func_args_print
def add(num_1, num_2):
    return num_1 + num_2


print(add(7, 3))