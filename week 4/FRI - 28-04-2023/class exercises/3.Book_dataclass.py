# Create a dataclass called Book with the following attributes:
# title (str), author (str), year (int), pages (int), rating (float),
# publisher (str), and genres (list of strings). Write a method called
# has_genre that takes a genre string as input and returns a boolean
# indicating whether the book belongs to that genre. Write a second
# method called to_dict that returns a dictionary of the book's attributes.
# Instantiate several objects of Book with different attributes
# and test your has_genre and to_dict methods.

from dataclasses import dataclass


@dataclass()
class Book:
    title: str
    author: str
    year: int
    pages: int
    rating: float
    publisher: str
    genres: list

    def has_genre(self, genre):
        if genre in self.genres:
            return True
        return False

    def to_dict(self):
        books_dictionary = {}
        books_dictionary["Title"] = self.title
        books_dictionary["Author"] = self.author
        books_dictionary["Year"] = self.year
        books_dictionary["Pages"] = self.pages
        books_dictionary["Raiting"] = self.rating
        books_dictionary["Publisher"] = self.publisher
        books_dictionary["Genres"] = self.genres

        return books_dictionary


book1 = Book("The Girl on the Train", "Paula Hawkins", 2015, 317, 8.7, "Riverhead, US",
             ['Novel', 'Thriller', 'Mistery'])


print(book1.has_genre("Novel"))
book_details = book1.has_genre('science fiction')
print(book_details)
print(book1.to_dict())
