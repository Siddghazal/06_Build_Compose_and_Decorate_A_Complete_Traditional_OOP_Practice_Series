class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price


product = Product(100)

# Get price
print("Price:", product.price)

# Set price using setter
product.price = 120
print("Updated Price:", product.price)

# Delete price
del product.price
