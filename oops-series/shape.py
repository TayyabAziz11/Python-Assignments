from abc import ABC, abstractmethod

# Define an abstract base class Shape

class Shape(ABC):

    # Abstract method (no body)

    @abstractmethod

    def area(self):
        pass

# Rectangle inherits from Shape and implements area()

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implementing the abstract method

    def area(self):
        return self.width * self.height

# Create an object of Rectangle and call area()

rect = Rectangle(5, 10)

print("Area of rectangle:", rect.area())