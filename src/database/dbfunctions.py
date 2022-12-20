import sys
sys.path.insert(0, "src//")
from database.dbconnect import DatabaseHandler
from functional.book import Book
from functional.account import Account

def userLogin(user) -> bool:
    return DatabaseHandler().parser(f"SELECT login('{user.email}','{user.password}')")[0][0]
   
def registerUser(user):
    DatabaseHandler().insert(f"INSERT INTO credentials (firstname, lastname, phonenumber, email, password) VALUES ('{user.firstname}','{user.lastname}','{user.phonenumber}','{user.email}','{user.password}');")

def getUser(email: str):
    try:
        if(email):
            return Account(*DatabaseHandler().parser(f"SELECT firstname, lastname, phonenumber, email FROM public.user WHERE email='{email}';")[0])
        else:
            raise AttributeError
    except (IndexError, AttributeError):
        print("Email nicht in der DB vorhanden")
    
def fetchBook(bookId) -> Book:
    return Book(*DatabaseHandler().parser(f"SELECT * FROM books WHERE bookid={bookId};")[0])

def fetchAllBookIds() -> list:
    return DatabaseHandler().parser(f"SELECT bookid FROM books;")[0][0]
           
def addToDatabase(book:Book) -> None:
    DatabaseHandler().insert(f"INSERT INTO books (bookid, title, author, genre, publishingyear, borroweddate, publisher, rating, isborrowed, picture) VALUES ({book.getID()}, '{book.getTitle()}', '{book.getAuthor()}', '{book.getGenre()}', {book.getPublishingYear()}, '{book.getBorrowedDate()}', '{book.getPublisher()}', {book.getAverageRating()}, {book.getIsBorrowed()}, '{book.getPicture()}');")
 
def updateBorrowedTable(borrowedId:int, userId:int, book:Book) -> None:
    query = f"INSERT INTO isborrowed (borrowedid, bookid, userid, booktitle) VALUES ({borrowedId}, {book.getID()}, {userId}, '{book.getTitle()}');"
    DatabaseHandler().insert(query)
    
def updateBooksTable() -> None:
    DatabaseHandler()