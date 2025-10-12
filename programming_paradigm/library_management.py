class Book:
    def __init__(self, title, author):
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Check out the book if available"""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        """Return the book if it was checked out"""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self):
        """Check if the book is available"""
        return not self._is_checked_out

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, title, author):
        """Add a new book to the library"""
        book = Book(title, author)
        self._books.append(book)
        return f"Added {book}"

    def check_out_book(self, title):
        """Check out a book by title"""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"Successfully checked out '{title}'"
                else:
                    return f"'{title}' is already checked out"
        return f"Book '{title}' not found in library"

    def return_book(self, title):
        """Return a book by title"""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f"Successfully returned '{title}'"
                else:
                    return f"'{title}' was not checked out"
        return f"Book '{title}' not found in library"

    def list_available_books(self):
        """List all available books in the library"""
        available_books = [book for book in self._books if book.is_available()]

        if not available_books:
            return "No available books in the library"

        result = "Available books:\n"
        for i, book in enumerate(available_books, 1):
            result += f"{i}. {book}\n"
        return result
