class Book:
    total_books = 0  # class variable

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()  # Increment count when a new book is added

# Example usage
book1 = Book("Python Programming")
book2 = Book("Data Structures")

print("Total books:", Book.total_books)
