def debug(func):
    def wrapper():
        print(f"Entering {func.__name__}")
        result = func()
        print(func())
        print(f"Exiting {func.__name__}")
        return result

    return wrapper


@debug
def state_case():
    return "Stating my case as a wizard"


print(state_case())
