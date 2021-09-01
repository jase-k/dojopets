class Pet:
# implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 80
        self.energy = 50
# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
# noise() - prints out the pet's sound
    def noise(self):
        print("Bark")

    def print(self):
        print(f"This pet {self.type}'s name is {self.name}. \nHere are a list of tricks he can do: ")
        for trick in self.tricks:
            print(trick)

doc = Pet("Doc", "dog", ["sit", "play dead", "lie down"])

doc.print()
