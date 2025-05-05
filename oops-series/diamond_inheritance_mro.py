class A:

    def show(self):

        print("Class A")

# Class B inherits from A and overrides show()

class B(A):

    def show(self):

        print("Class B")

# Class C also inherits from A and overrides show()

class C(A):

    def show(self):

        print("Class C")

# Class D inherits from both B and C (Diamond Inheritance)

class D(B, C):

    pass  # No show() method, so MRO will determine which parent method is called

# Create an object of class D

obj = D()

# Call show() method – MRO decides which one gets called

obj.show()

# Print the method resolution order

print("MRO:", [cls.__name__ for cls in D.__mro__])