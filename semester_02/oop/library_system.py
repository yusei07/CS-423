import datetime

# Base/Abstract class


class LibraryItem:
    def __init__(self, t, a, i, b):  # constructor / initialiser method
        self.__Title = t
        self.__Author__Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()
        self.__BorrowerID = b

    @property
    def Title(self):
        return (self.__Title)

    @property
    def Author_Artist(self):
        return (self.__Author_Artist)

    @property
    def ItemID(self):
        return (self.__ItemID)

    @property
    def OnLoan(self):
        return (self.__OnLoan)

    @property
    def DueDate(self):
        return (self.__DueDate)

    def Borrowing(self):
        if self.__OnLoan:
            print("Item is already on loan.")
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)
        self.__Borrower.UpdateItemsOnLoan(1)

    def Returning(self):
        if not self.__OnLoan:
            print("Item is not on laon.")
        self.__OnLoan = False
        self.__Borrower.UpdateItemsOnLoan(-1)

    def PrintDetails(self):
        print(self.__Title, '; ', self.__Author__Artist, '; ', end='')
        print(self.__ItemID, '; ', self.__OnLoan, '; ', self.__DueDate)

# Subclass I


class Borrower:
    def __init__(self, n, e, i):
        LibraryItem.__init__(self, t, a, i)
        self.__BorrowerName = n
        self.__EmailAddress = e
        self.__BorrowerID = i
        self.__ItemsOnLoan = 0

    @property
    def BorrowerName(self):
        return self.__BorrowerName

    @property
    def EmailAddress(self):
        return self.__EmailAddress

    @property
    def BorrowerID(self):
        return self.__BorrowerID

    @property
    def ItemsOnLoan(self):
        return self.__ItemsOnLoan

    def UpdateItemsOnLoan(self, num):
        self.__ItemsOnLoan += num

    def PrintDetails(self):
        print('Name: ', self.__BorrowerName,
              '\nEmail Address: ', self.__EmailAddress,
              '\nID: ', self.__BorrowerID,
              '\nLoan Item: ', self.__ItemsOnLoan)


# Subclass II


class Book(LibraryItem):
    def __init__(self, t, a, i):  # initialiser method
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0

    @property
    def IsRequested(self):
        return (self.__IsRequested)

    @IsRequested.setter
    def IsRequested(self, b):
        self.__IsRequested = True
        self.__IsRequested = b

    def PrintDetails(self):
        print("Book Details")
        LibraryItem.PrintDetails(self)
        print(self.__IsRequested)

# Subclass III


class CD(LibraryItem):
    def __init__(self, t, a, i):  # initialiser method
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""

    @property def Genre(self):
        return (self.__Genre)

    @Genre.setter
    def Genre(self, g):
        self.__Genre = g

    def PrintDetails(self):
        print("CD Details")
        LibraryItem.PrintDetails(self)
        print(self.__Genre)


while True:
    menu = input("Welcome to Yu's Library!\n\n"
                 "1 - Add a new borrower\n"
                 "2 - Add a new book\n"
                 "3 - Add a new CD\n"
                 "4 - Borrow a book\n"
                 "5 - Return a book\n"
                 "6 - Borrow a Cd\n"
                 "7 - Return a CD\n"
                 "8 - Request a book\n"
                 "9 - Print all details\n\n"
                 "99 - Exit program\n")

    if menu == "1":
        name = input("Enter your name: ")
        email = input("Email: ")
        b_id = input("ID: ")
        borrower = Borrower(name, email, b_id)
        borrower.append(borrower)
        print("Borrower added successfully!")

    elif menu == "2":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        id = input("Enter book ID: ")
        book = Book(title, author, id)
        books.append(book)
        print("Book added successfully!")

    elif menu == "3":
        title = input("Enter CD title: ")
        artist = input("Enter CD artist: ")
        id = input("Enter CD ID: ")
        cd = CD(title, artist, id)
        cds.append(cd)
        print("CD added successfully!")

    elif menu == "4":
        item_id = input("Enter book ID to borrow: ")
        borrower_id = input("Enter borrower ID: ")
        book = find_item(books, item_id)
        borrower = find_item(borrowers, borrower_id)
        if book is None:
            print("Book not found. Please try again.")
        elif borrower is None:
            print("Borrower not found. Please try again.")
        else:
            book.Borrowing()
            book.BorrowerID = borrower.BorrowerID
            book.Borrower = borrower
            print("Book borrowed successfully!")

    elif menu == "5":
        item_id = input("Enter book ID to return: ")
        book = find_item(books, item_id)
        if book is None:
            print("Book not found. Please try again.")
        else:
            book.Returning()
            print("Book returned successfully!")

    elif menu == "6":
        item_id = input("Enter CD ID to borrow: ")
        borrower_id = input("Enter borrower ID: ")
        cd = find_item(cds, item_id)
        borrower = find_item(borrowers, borrower_id)
        if cd is None:
            print("CD not found. Please try again.")
        elif borrower is None:
            print("Borrower not found. Please try again.")
        else:
            cd.Borrowing()
            cd.BorrowerID = borrower.BorrowerID
            cd.Borrower = borrower
            print("CD borrowed successfully!")

    elif menu == "7":
        item_id = input("Enter CD ID to return: ")
        cd = find_item(cds, item_id)
        if cd is None:
            print("CD not found. Please try again.")
        else:
            cd.Returning()
            print("CD returned successfully!")
    else:
        print("Invalid menu. Please enter a valid option.")
        # test = Borrower("Bayu", "usernamesaresohardtomake@gmail.com", 191817)
        # test.PrintDetails()
        # print()
        # test.UpdateItemsOnLoan(2)
        # test.PrintDetails()

        # book1 = Book("The Meditations", "Marcus Aurelius", 1)
        # book1.Borrowing()
        # # book1.IsRequested = True
        #
        # cd1 = CD("Perfect Pair", "Beadadobee", 2)
        # cd1.Genre = "Pop"
        #
        # book1.PrintDetails()
        # cd1.PrintDetails()
