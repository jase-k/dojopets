from pet import Pet

class Ninja:
# implement __init__( first_name , last_name , pet , treats , pet_food )
    def __init__(self, first_name, last_name, pet, treats, pet_food): 
        self.first_name = first_name
        self.last_name = last_name
        print(pet)
        self.pet = Pet(pet["name"], pet["type"], pet["tricks"])
        self.treats = treats
        self.pet_food = pet_food
    
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()

# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        
pet = {
    "name" : "Doc",
    "type" : "dog",
    "tricks" : ["sit", "lie down", "fetch", "pee on x"]
}

jase = Ninja("Jase", "Kraft", pet , ["Bones", "Bisquits"], "DogFood")

jase.bathe()