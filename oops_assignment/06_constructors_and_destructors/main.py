class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

# Example usage
log = Logger()

# Forcing deletion (optional, to see destructor message immediately)
del log
