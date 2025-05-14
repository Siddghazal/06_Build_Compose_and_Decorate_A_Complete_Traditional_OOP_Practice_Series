class Countdown:
    def __init__(self, start):
        self.start = start  # Starting number for countdown

    def __iter__(self):
        self.current = self.start  # Initialize the current count
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Stop the iteration once we reach 0
        else:
            self.current -= 1
            return self.current

countdown = Countdown(5)
for number in countdown:
    print(number)
