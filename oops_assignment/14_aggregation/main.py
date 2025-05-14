class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: Department stores reference to Employee

    def display_department(self):
        print(f"Department: {self.department_name}")
        self.employee.display()  # Accessing Employee object via Department

# Example usage
emp = Employee("Ali", "Software Engineer")
dept = Department("IT", emp)
dept.display_department()
