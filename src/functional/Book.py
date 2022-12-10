from rating import rating
from datetime import date


class Book(object):

    def __init__(self, bookid: int, title: str, author: str, genre: str, publishingYear: int, borrowedDate: date, publisher: str) -> None:
        self.__bookid = bookid
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publishingYear = publishingYear
        self.__borrowedDate = borrowedDate #YYYY-MM-DD
        self.__publisher = publisher
        self.__ratings: rating = []
        self.__isBorrowed: bool = False

    def getbookid(self) -> int:
        return self.__bookid
    
    def setbookid(self, bookid: int) -> None:
        self.__bookid = bookid

    def getTitle(self) -> str:
        return self.__title

    def setTitle(self, title: str) -> None:
        self.__title = title

    def getAuthor(self) -> str:
        return self.__author

    def setAuthor(self, author: str) -> None:
        self.__author = author

    def getGenre(self) -> str:
        return self.__genre

    def setGenre(self, genre) -> None:
        self.__genre = genre

    def getPublishingYear(self) -> int:
        return self.__publishingYear

    def setPublishingYear(self, publishingYear: int) -> None:
        self.__publishingYear = publishingYear

    def getBorrowedDate(self) -> date:
        return self.__borrowedDate

    def setBorrowedDate(self, borrowedDate) -> None:
        self.__borrowedDate = borrowedDate

    def getPublisher(self) -> str:
        return self.__publisher

    def setPublisher(self, publisher: str) -> None:
        self.__publisher = publisher

    def getRatings(self) -> list:
        return self.__ratings

    def addRating(self, newRating: rating) -> None:
        self.__ratings.append(newRating)

    # get average rating of a book rounded to an int.
    def getAverageRating(self) -> int:
        sum = 0
        for rating in self.__ratings:
            sum += rating.getValue()
        return round(sum / len(self.__ratings))

    def isBorrowed(self) -> bool:
        return self.__isBorrowed
    
    def setBorrowed(self) -> None:
        self.__isBorrowed = True
    
    def setUnBorrowed(self) -> None:
        self.__isBorrowed = False

    def addBook(self) -> None:
        db = db.DataseHandler()

        helper = f"SELECT * FROM books WHERE name=?", (self.__title)
        result = db.parser(helper)
        if result:
            print(f"Book is already in the database. Please add a NEW book.")
            return;
        else:
            query = f"INSERT into books (bookid, title, author, genre) VALUES(?)", (self.__bookid, self.__title, self.__author, self.__genre)
            db.parser(query)
            print(f"Book has been added to the database")




book = Book("egal", "egal", 2001, "gal", "egal")
for i in range(0, 6):
    book.addRating(rating(i))
    print(book.getAverageRating())
    
book2 = Book(5000, "test", "tester", "NSFW", 1999, (2005,9,5), "stranz")
book2.addBook()


