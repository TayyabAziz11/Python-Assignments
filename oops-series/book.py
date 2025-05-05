class Book:
    
    # Class variable to track the total number of books

    total_books = 0

    # Class method to increment the book count

    @classmethod

    def increment_book_count(cls):

        cls.total_books += 1

    # Constructor to create a new book and increment the count

    def __init__(self, title):

        self.title = title

        Book.increment_book_count()  # Increment book count when a new book is created

# Create books and see how total_books increases

book1 = Book("The Great Gatsby")

book2 = Book("1984")

book3 = Book("To Kill a Mockingbird")

# Display the total number of books created

print("Total books:", Book.total_books)


