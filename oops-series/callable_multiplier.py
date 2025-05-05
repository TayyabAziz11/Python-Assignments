class Multiplier:
    
    def __init__(self, factor):

        self.factor = factor  # Store the multiplication factor

    # Define the __call__ method so the object can be called like a function

    def __call__(self, value):

        return value * self.factor

# Create an object of Multiplier

double = Multiplier(2)

# Test with callable()

print("Is 'double' callable?", callable(double))  

# Call the object like a function

result = double(5)  # Equivalent to double.__call__(5)

print("Result:", result)  # Output: 10