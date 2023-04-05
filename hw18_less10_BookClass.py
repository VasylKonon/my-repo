class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.pages < other.pages


def print_separation():
    print("*" * 100)


book1 = Book("Harry Potter and the philosopher's stone", "J.K.Rowling", 300)
book2 = Book("Harry Potter and the goblet of fire", "J.K.Rowling", 500)
book3 = Book("Harry Potter and the Prisoner of Azkaban", "J.K.Rowling", 400)

books = [book1, book2, book3]

print_separation()

for book in books:
    print(book)

print_separation()

for book in books:
    print(len(book))

print_separation()

print(book1 == book2)

print_separation()

sorted_books = sorted(books)
for book in sorted_books:
    print(book)

print_separation()

print(book1 in books)

print_separation()

print(max(books))

print_separation()

print(min(books))
