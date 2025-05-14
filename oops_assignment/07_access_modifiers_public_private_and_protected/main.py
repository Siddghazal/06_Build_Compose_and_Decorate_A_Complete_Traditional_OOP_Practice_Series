class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           # public
        self._salary = salary      # protected (by convention)
        self.__ssn = ssn           # private

# Example usage
emp = Employee("Ali", 50000, "123-45-6789")

# Accessing variables
print("Name (public):", emp.name)         # Accessible
print("Salary (protected):", emp._salary) # Accessible but should be treated as protected
try:
    print("SSN (private):", emp.__ssn)     # Will raise AttributeError
except AttributeError:
    print("Cannot access private variable __ssn directly.")

# Accessing private variable using name mangling (not recommended for regular use)
print("SSN (via name mangling):", emp._Employee__ssn)
