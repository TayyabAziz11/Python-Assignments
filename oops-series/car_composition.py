class Engine:

    def start(self):
        print("Engine has started.")

# Define the Car class that uses composition (has-an Engine)

class Car:
    
    def __init__(self, engine):

        self.engine = engine  # Store the Engine object inside Car

    def start_car(self):

        print("Car is starting...")

        self.engine.start()  # Access method of Engine class

# Create an Engine object

my_engine = Engine()

# Pass Engine object to Car

my_car = Car(my_engine)

# Start the car (which starts the engine too)

my_car.start_car()