class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def checkout(self):
        if self.available:
            self.available = False
            return True
        else:
            return False

    def return_book(self):
        self.available = True

    def display_info(self):
        if self.available:
            print(f"The book: {self.title} from {self.author} it's available")
        else:
            print(f"The book: {self.title} from {self.author} it's not available")


book1 = Book("Senhor dos anéis", "J.R Tolkien")
book2 = Book("Sítio do Pica-Pau Amarelo", "Monteiro Lobato")
book3 = Book("As Crônicas de Fogo e Gelo", "G Martin")


class Library:
    def __init__(self):
        self.books = []

    def display_books(self):
        for book in self.books:
            book.display_info()

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("O objeto deve pertencer a classe Book")

    def get_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
            else:
                return None


library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()
