def log_function_call(func):
    def wrapper():
        print("\nFunction is being called")
        func()  # Calling the original function
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()
