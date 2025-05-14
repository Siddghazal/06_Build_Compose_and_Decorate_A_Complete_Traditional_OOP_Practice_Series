class Dog:
    def __init__(self, name, breed):
        self.name = name      # instance variable
        self.breed = breed    # instance variable

    def bark(self):           # instance method
        print(self.name, "is barking!")

# Example usage
dog1 = Dog("Bruno", "Labrador")
dog1.bark()
