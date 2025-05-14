class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    else:
        print("Age is valid.")

# Example usage
try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e}")
