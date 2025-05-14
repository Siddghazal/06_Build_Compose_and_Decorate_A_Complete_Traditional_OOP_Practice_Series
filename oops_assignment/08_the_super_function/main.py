class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # calling base class constructor
        self.subject = subject

    def display(self):
       
        print("Name:", self.name)
        print("Subject:", self.subject)

# Example usage
t1 = Teacher("Miss Sara", "Math")
t1.display()

