class Employee:

    def __init__(self, name, salary, ssn):

        self.name = name        # Public variable

        self._salary = salary   # Protected variable (convention)

        self._Employee__ssn = ssn        # Private variable (name mangled)

# Create an object of Employee class

emp = Employee("Tayyab", 500000, "123-45-6789")

# Accessing public variable - works fine

print("Name (Public):", emp.name)

# Accessing protected variable - works, but not recommended from outside

print("Salary (Protected):", emp._salary)

# Accessing private variable - will raise an error

try:

    print("SSN (Private):", emp._Employee__ssn)  # Accessing private variable using name mangling

except AttributeError:

    print("SSN (Private): Cannot access directly!")

# Correct way to access private variable (name mangling)

print("SSN (Private, using name mangling):", emp._Employee__ssn)