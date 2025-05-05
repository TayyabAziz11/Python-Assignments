class Car:

    # Public variable

    brand = "BMW"

    # Public method

    def start(self):

        print(self.brand, "is starting...")

# Create an object of Car class

my_car = Car()

# Accessing public variable from outside the class

print("Car Brand:", my_car.brand)

# Accessing public method from outside the class

my_car.start()
