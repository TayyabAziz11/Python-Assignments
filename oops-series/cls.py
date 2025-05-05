class Counter:

    # Class variable to keep track of object count
    
    count = 0

    # Constructor method increases count every time an object is created

    def __init__(self):

        Counter.count += 1

    # Class method to display how many objects were created

    @classmethod

    def display_count(cls):

        print("Total objects created:", cls.count)

# Creating multiple objects

obj1 = Counter()

obj2 = Counter()

obj3 = Counter()

# Calling class method to display the count

Counter.display_count()
