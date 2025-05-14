class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Set the factor

    def __call__(self, value):
        return value * self.factor  # Multiply input by the factor

# Example usage
multiplier = Multiplier(5)

# Test using callable() function
print(callable(multiplier))  # Will print True because __call__ is defined

# Calling the object like a function
result = multiplier(10)  # Equivalent to multiplier.__call__(10)
print("Result of multiplication:", result)
