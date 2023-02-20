class Borrower:
    def __init__(self, n, e, i):
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


test = Borrower("Bayu", "usernamesaresohardtomake@gmail.com", 191817)
test.PrintDetails()
print()
test.UpdateItemsOnLoan(2)
test.PrintDetails()
