class MathUtils:

    # Static method that adds two numbers

    @staticmethod

    def add(a, b):

        return a + b

# Call the static method without creating an object

result = MathUtils.add(5, 7)

print("Sum is:", result)
