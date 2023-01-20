class Person:
    greeting = 'Hello'
    def __repr__(self):
        return self.greeting

# Remember that in order to use the repr() or str() function, we must print them unless we are in the REPL
Sky = Person()
greet = Sky.__repr__()
print(greet)

