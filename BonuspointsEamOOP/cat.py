

from animal import Animal
from pet import Pet


class Cat(Animal,Pet):

    def __init__(self, name):
        Animal.__init__(self, 4)
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is playing :)")


    def eat(self):
        print(f"{self.name} is eating cat food :)")

