class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Example usage
student1 = Student("Ali", 85)
student1.display()

student2 = Student("Ahmad", 90)
student2.display()
