def log_function_call(func):

    def wrapper():

        print("Function is being called")

        return func()  # Call the original function
    
    return wrapper

# Apply the decorator to a function using @ syntax

@log_function_call

def say_hello():
    
    print(f"hey, I am a function!")

# Call the decorated function
say_hello()