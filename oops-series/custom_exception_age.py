class InvalidAgeError(Exception):

    pass  # No special behavior; just a named exception

# Function to check age and raise custom exception

def check_age(age):

    if age < 18:

        raise InvalidAgeError("Age must be at least 18.")
    
    else:

        print("Age is valid!")

# Use try-except to handle the custom exception

try:

    age = int(input("Enter your age: "))

    check_age(age)

except InvalidAgeError as e:

    print("Custom Exception Caught:", e)

except ValueError:
    
    print("Please enter a valid number.")