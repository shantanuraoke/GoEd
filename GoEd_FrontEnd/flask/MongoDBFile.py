import pymongo
import uuid
from bson.objectid import ObjectId
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myDB = myclient["Library2"]
db_names = myclient.list_database_names()
print(db_names)
if "Library" in db_names:
    # Do nothing
    print('Nothing')
else:
    print('Failed to create db')

users = myDB['users']
books = myDB['books']
library = myDB['lib']
borrowedBook = myDB['borrow']
orderHistory = myDB['orderHistory']
bookID = str(uuid.uuid4())

db_names_collection = myDB.list_collection_names()
bookBorrowedDict = {"bookID": bookID, "dateOfBorrow": "Sample",
                    "returnDate": "Sample", "counter": "0", "returnTime": "8","userID":"Sample"}
bookHistory = {"bookID": bookID, "Dateissue": "Sample Date"}
section = {
    "books": bookID
}
booksDict = {
    "bookID": bookID,
    "name": "Tejas",
    "author": "Sample",
    "location": "Bock B",
    "noOfPeople": "13",
    "isBorrowed": False,
    "borrowedUsers" : ["uuid1"]
}

libDict = {"Section 1": section, "Section 2 ": section}
uniqueID = str(uuid.uuid4())
userDict = {"userID": uniqueID, "booksBorrowed": "0"}

# x = users.insert_one(userDict)
# x1 = books.insert_one(booksDict)
# x2 = library.insert_one(libDict)

# y = users.find_one()
# print(y)
# y = books.find_one()
# print(y)
# y = library.find_one()
# print(y)
# if "users" in db_names_collection:
#     # Do nothing
#     print('Nothing')
# else:
#     print('Failed to create Collection')


def insertNewBook(bookName, author, location):
    bID = str(uuid.uuid4())
    bDict = {
        "bookID": bID,
        "name": bookName,
        "author": author,
        "location": location,
        "noOfPeople": "0",
        "isBorrowed": False

    }
    insertBook = books.insert_one(bDict)

def createUser():
    print("creating user")
    uid = str(uuid.uuid4())
    
    uDict = {
        "userID": uid,
        "booksBorrowed": "0",
    }
    users.insert_one(uDict)

def deleteBook(bookID):
    print(borrowedBook.find_one({"bookID": bookID}))
    if (borrowedBook.find_one({"bookID": bookID}) == None):
        books.delete_one({"bookID": bookID})
    else:
        print('Cannot remove')

    # bookBorrowedDict.remove({"bookID":bookID})


def borrowBook(userID, bookID, returnt, dateBorrow, dateRet):
    # increment borrowed books by 1
    borrowDict = {
        "bookID": bookID,
        "dateOfBorrow": dateBorrow,
        "returnDate": dateRet,
        "counter": "0",
        "returnTime": returnt,
        "userID": userID
    }
    bBook = borrowedBook.insert_one(borrowDict)
    books.update_one({"bookID": bookID}, {"$set": {"isBorrowed": True}})

def returnBook(bookID):
    # Get the userID from the borrowedBooks
    # Add it to the history
    # remove from borrow
    if (borrowedBook.find_one({"bookID":bookID}) != None):
        print("Exists")
        books.update_one({"bookID": bookID}, {"$set": {"isBorrowed": False}})
        borrowedBookDict =  borrowedBook.find_one({"bookID":bookID})
        uid = borrowedBookDict['userID']
        dateBorrow = borrowedBookDict['dateOfBorrow']
        returnDate = borrowedBookDict['returnDate']
        print("USER ID ")
        print(uid)
        borrowedBook.delete_one({"bookID":bookID})
        orderDict = {
            "userID": uid,
            "bookID": bookID,
            "dateOfBorrow": dateBorrow,
            "returnDate": returnDate
        }
        print(uid)
        print(bookID)
        print(dateBorrow)
        print(returnDate)
        print(orderDict)
        ordNo = orderHistory.insert_one(orderDict)
    print(returnBook)


# insertNewBook("Tintin","James","Block 2")
# print(books.find())
# borrowBook("User1","",5,"Jan 1","Jan 6")
# createUser()
# deleteBook("0e8e38fb-60f1-46c5-90d8-5018cdf63121")
# returnBook("bdd13709-fb69-4f63-832b-09e261d36910")
# users.delete_one({"_id" : ObjectId("5d0e7b2464d1c7d1f264b26b")})
# books.delete_one({"_id" : ObjectId("5d0e7b2464d1c7d1f264b26c")})
# borrowBook("aeda9c77-b476-4210-b8d6-40db2bb318ea","bdd13709-fb69-4f63-832b-09e261d36910",5,"Jan 2","Jan 7")