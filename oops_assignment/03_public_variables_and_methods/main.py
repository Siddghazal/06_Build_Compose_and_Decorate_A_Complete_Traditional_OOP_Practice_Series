class Car:
    def __init__(self, brand):
        self.brand = brand  # public variable

    def start(self):  # public method
        print(self.brand, "car is starting...")

# Example usage
my_car = Car("Honda")
print("Car Brand:", my_car.brand)  # accessing public variable
my_car.start()  # calling public method

