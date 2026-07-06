

from animal import Animal
from pet import Pet



class Fish(Animal, Pet):
    def __init__(self, name):
        Animal.__init__(self, 0)
        self.name = name

    def walk(self):
        print(f"{self.name} is a fish it cannot walk, it swims... :(")


    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def play(self):
        print(f"{self.name} is swimming around, playing amongst the corals :)")

    def eat(self):
        print(f"{self.name} eats fish food :)")