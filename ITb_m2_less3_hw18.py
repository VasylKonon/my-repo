class Book:
    def __init__(self, name, author, publication_year, number_of_pages):
        self.name = name
        self.author = author
        self.publication_year = publication_year
        self.number_of_pages = number_of_pages

    @staticmethod
    def return_amount(books_list, publication_year):
        amount = 0
        for book in books_list:
            if publication_year == book.publication_year:
                amount += 1
        return amount


books = [
    Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 1997, 200),
    Book("Harry Potter and the Goblet of Fire", "J. K. Rowling", 2000, 500),
    Book("Harry Potter and the Goblet of Fire1", "J. K. Rowling", 2000, 505),
    Book("Harry Potter and the Goblet of Fire2", "J. K. Rowling", 2000, 550),
    Book("Harry Potter and the Deathly Hallows", "J. K. Rowling", 2007, 400)
]

print(Book.return_amount(books, 2000))
