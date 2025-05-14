class Engine:
    def start(self):
        print("Engine is starting...")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine object

    def start_car(self):
        self.engine.start()  # Accessing Engine's method via Car

# Example usage
engine = Engine()
car = Car(engine)
car.start_car()
