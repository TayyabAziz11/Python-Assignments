class Student:

    # Constructor method to initialize name and marks using 'self'

    def __init__(self, name, marks):

        self.name = name      # 'self.name' stores the student's name

        self.marks = marks    # 'self.marks' stores the student's marks

    # Method to display student details

    def display(self):

        print("Student Name:", self.name)

        print("Marks:", self.marks)

# Create an object of Student class and call display method

student1 = Student("Qasim", 88)

student1.display()
