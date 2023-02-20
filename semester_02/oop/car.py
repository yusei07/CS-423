class Car:
    # def init = constructor
    def __init__(self, n, e):
        self.__VehicleID = n
        self.__Registration = ""
        self.__DateOfRegistration = None
        self.__EngineSize = e
        self.__PurchasePrice = 0.0

    def SetPurchasePrice(self, p):
        self.__PurchasePrice = p

    def SetRegistration(self, r):
        self.__Registration = r

    def SetDateOfRegistration(self, d):
        self.__DateOfRegistration = d

    def GetVehicleID(self):
        return self.__VehicleID

    def GetRegistration(self):
        return self.__Registration

    def GetDateOfRegistration(self):
        return self.__DateOfRegistration

    def GetEngineSize(self):
        return self.__EngineSize

    def GetPurchasePrice(self):
        return self.__PurchasePrice

# Instantiation of an object


Car1 = Car("MHK1234", 1200)

print(Car1.GetVehicleID())
print(Car1.GetEngineSize())
PurchasePrice = float(input("Enter your purchase price: "))
Car1.SetPurchasePrice(PurchasePrice)
print(Car1.GetPurchasePrice())
