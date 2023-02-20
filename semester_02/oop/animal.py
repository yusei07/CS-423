# parent class
class animals:
    def __init__(self, n, a, s, h):
        self.__name = n
        self.__age = a
        self.__species = s
        self.__habitat = h

    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species

    @property
    def age(self):
        return self.__age

    @property
    def habitat(self):
        return self.__habitat

# additional method

    @property
    def eat(self):
        print(self.name, "is eating")

    @property
    def sleep(self):
        print("shhh", self.name, "is sleeping..")

    @property
    def make_sound(self):
        print(self.name, "is making a sound")

# child class


class bird(animals):
    def __init__(self, n, a, s, h, w, c):
        animals.__init__(self, n, a, s, h)
        self.__wingspan = w
        self.__can_fly = c

    @property
    def wingspan(self):
        return self.__wingspan

    @property
    def can_fly(self):
        return self.__can_fly

    @property
    def make_sound(self):
        print(self.name, "is chirping.")

    @property
    def fly(self):
        print(self.name, "is flying!!")

    @property
    def build_nest(self):
        print(self.name, "is busy building a nest.")

# child class


class fish(animals):
    def __init__(self, n, a, s, h, f, t):
        animals.__init__(self, n, a, s, h)
        self.__fins = f
        self.__water_type = t

    @property
    def swim(self):
        print(self.name, "is swimming")

    @property
    def breathe_underwater(self):
        print(self.name, "is breathing underwater")

    @property
    def make_sound(self):
        print(self.name, "is blooping")


# instantiations

eagle = bird("totoro", 7, "golden eagle", "mountain", 90, True)
# eagle.fly
# eagle.make_sound
# eagle.build_nest

trout = fish("ponyo", 9, "salmon", "pacific ocean", 8, "salt water")
# trout.swim
# trout.make_sound
# trout.breathe_underwater
