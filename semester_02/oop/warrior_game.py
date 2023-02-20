class Character:
    # constructor
    def __init__(self, n):
        self.__name = n
        self.__health = 0
        self.__mana = 0

    # getter
    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @property
    def mana(self):
        return self.__mana

    # setter
    @mana.setter
    def mana(self, m):
        self.__mana = m

    @health.setter
    def health(self, h):
        self.__health = h

    def attack(self):
        pass

# child class I


class warrior(Character):
    # a is required to be declared so that agility is passed with the variable a
    def __init__(self, n, a):
        Character.__init__(self, n)  # to inherit everything in character
        self.__agility = a

    @property
    def agility(self):
        return self.__agility

# child class II


class mage(Character):
    def __init__(self, n, i):
        Character.__init__(self, n)
        self.__intelligence = i

    @property
    def intelligence(self):
        return self.__intelligence


# Instantiation
Thor = warrior("Thor", 45)
Gandalf = mage("Gandalf", 15)
Thor.mana = 100
Thor.health = 80
Gandalf.mana = 65
Gandalf.health = 100

print("Thor's health: ", Thor.health)
print("Gandalf's mana: ", Gandalf.mana)
