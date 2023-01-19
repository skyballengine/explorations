class Person:
    greeting = 'Hello'
    def __repr__(self):
        return self.greeting

Sky = Person()
greet = Sky.__repr__()
print(greet)

