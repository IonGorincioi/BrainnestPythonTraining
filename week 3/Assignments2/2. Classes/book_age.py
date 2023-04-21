# Create a class called Book that has attributes
# title, author, and publication_year. Add a method
# get_age that calculates how many years ago the book was published.
import datetime


class Book:
    current_time = datetime.datetime.now()

    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_age(self):
        book_age = self.current_time.year - self.publication_year
        return book_age


book1 = Book("Starting out with Python", "Tony Gaddis", 2020)
print(f'The book "{book1.title}", fifth edition, was published {book1.get_age()} years ago.')
