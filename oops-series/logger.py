class Logger:

    # Constructor: called when object is created

    def __init__(self):

        print("Logger started: Object created.")

    # Destructor: called when object is destroyed

    def __del__(self):
        
        print("Logger ended: Object destroyed.")

# Create an object of Logger class
log = Logger()

# Deleting the object to trigger the destructor
del log