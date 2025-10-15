class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title},  {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size: str):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count


class Library:

    def __init__(self):
        self.book = []
        self.ebook = []
        self.print_book = []

    def add_book(self, book):
        if isinstance(book, EBook):
            self.ebook.append(book)
        elif isinstance(book, PrintBook):
            self.print_book.append(book)
        else:
            self.book.append(book)

    def list_books(self):
        print("=== LIBRARY COLLECTION ===")
        for zbook in self.book:
            print(f"{zbook}")
        for ebook in self.ebook:
            print(f"{ebook}")
        for pbook in self.print_book:
            print(f"{pbook}")
