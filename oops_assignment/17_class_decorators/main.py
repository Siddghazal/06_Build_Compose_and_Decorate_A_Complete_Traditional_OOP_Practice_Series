def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet  # Adding greet method to the class
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Usman")
print(person.greet())  # "Hello from Decorator!" will be returned
