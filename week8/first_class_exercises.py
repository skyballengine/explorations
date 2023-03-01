def greeting(name):
    return f'Hello {name}'


print(greeting("Wanda"))


def shout(func, name):
    greet = func(name)
    return greet.upper()


print(shout(greeting, "Timo"))
