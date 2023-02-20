class Car:
    # def init = constructor
    def __init__(self, n, e):
        self.__VehicleID = n
        self.__Registration = ""
        self.__DateOfRegistration = None
        self.__EngineSize = e
        self.__PurchasePrice = 0.0

    @property
    def VehicleID(self):
        return self.__VehicleID

    @property
    def Registration(self):
        return self.__Registration

    @property
    def DateOfRegistration(self):
        return self.__DateOfRegistration

    @property
    def EngineSize(self):
        return self.__EngineSize

    @property
    def PurchasePrice(self):
        return self.__PurchasePrice

    @PurchasePrice.setter
    def PurchasePrice(self, p):
        self.__PurchasePrice = p

    @Registration.setter
    def Registration(self, r):
        self.__Registration = r

    @DateOfRegistration.setter
    def DateOfRegistration(self, d):
        self.__DateOfRegistration = d

# Instantiation of an object (car)


Car1 = Car("MHK1234", 1200)
print(Car1.VehicleID)
Car1.PurchasePrice = 10000
print(Car1.PurchasePrice)
