class Product:

    def __init__(self, price):

        self._price = price  # Private attribute

    # Getter method using @property

    @property

    def price(self):

        return self._price

    # Setter method to update the price

    @price.setter

    def price(self, value):

        if value < 0:
            print("Price cannot be negative!")

        else:
            self._price = value

    # Deleter method to delete the price

    @price.deleter

    def price(self):
        print("Deleting price...")

        del self._price

# Create a Product object

item = Product(100)

# Access price using getter

print("Price:", item.price)

# Update price using setter

item.price = 150

print("Updated Price:", item.price)

# Try setting a negative price

item.price = -20  # Will show warning

# Delete price using deleter

del item.price