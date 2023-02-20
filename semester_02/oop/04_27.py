import datetime

# Base/Abstract class


class LibraryItem:
    def __init__(self, t, a, i):  # constructor / initialiser method
        self.__Title = t
        self.__Author__Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()

    @property
    def Title(self):
        return(self.__Title)

    @property
    def Author_Artist(self):
        return(self.__Author_Artist)

    @property
    def ItemID(self):
        return(self.__ItemID)

    @property
    def OnLoan(self):
        return(self.__OnLoan)

    @property
    def DueDate(self):
        return(self.__DueDate)

    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)

    def Returning(self):
        self.__OnLoan = False

    def PrintDetails(self):
        print(self.__Title, '; ', self.__Author__Artist, '; ', end='')
        print(self.__ItemID, '; ', self.__OnLoan, '; ', self.__DueDate)

# Subclass


class Book(LibraryItem):
    def __init__(self, t, a, i):  # initialiser method
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0

    @property
    def IsRequested(self):
        return(self.__IsRequested)

    @IsRequested.setter
    def IsRequested(self, b):
        self.__IsRequested = b

    def PrintDetails(self):
        print("Book Details")
        LibraryItem.PrintDetails(self)
        print(self.__IsRequested)

# Subclass


class CD(LibraryItem):
    def __init__(self, t, a, i):  # initialiser method
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""

    @property
    def Genre(self):
        return(self.__Genre)

    @Genre.setter
    def Genre(self, g):
        self.__Genre = g

    def PrintDetails(self):
        print("CD Details")
        LibraryItem.PrintDetails(self)
        print(self.__Genre)


book1 = Book("The Meditations", "Marcus Aurelius", 1)
book1.Borrowing()
# book1.IsRequested = True

cd1 = CD("Perfect Pair", "Beadadobee", 2)
cd1.Genre = "Pop"

book1.PrintDetails()
cd1.PrintDetails()
