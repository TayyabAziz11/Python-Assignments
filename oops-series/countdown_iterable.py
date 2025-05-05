class Countdown:

    def __init__(self, start):

        self.current = start  # Start number for countdown

    def __iter__(self):

        return self  # Return the iterator object (self)

    def __next__(self):

        if self.current < 0:

            raise StopIteration  # End the loop when below 0
        
        else:

            num = self.current

            self.current -= 1

            return num  # Return current number, then decrement

# Create a Countdown object

countdown = Countdown(5)

# Use it in a for loop (thanks to __iter__ and __next__)

for number in countdown:
    
    print(number)