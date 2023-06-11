class Library:
    def __init__(self, books):
        self.books = books

    def add_book(self, other):
        return self.books.append(other)

    def __str__(self):
        book_list = ""
        for i in self.books:
            book_list += str(i) + "\n"
        return book_list


class Book:
    def __init__(self, name, author, publication_year):
        self.name = name
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"{self.name} was written by {self.author} in {self.publication_year}"


library = Library([
    Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 1997),
    Book("Harry Potter and the Goblet of Fire", "J. K. Rowling", 2000),
    Book("Harry Potter and the Deathly Hallows", "J. K. Rowling", 2007)
])

print(library)

new_book = Book("Harry Potter and the Half-Blood Prince", "J. K. Rowling", 2005)
library.add_book(new_book)
print(library)
