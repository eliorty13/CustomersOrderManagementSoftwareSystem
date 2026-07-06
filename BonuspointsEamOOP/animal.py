


from abc import ABC, abstractmethod


class Animal(ABC):

   def __init__(self, legs):
        self.legs = legs


   def walk(self):
       print(f"this animal walks with {self.legs} legs")

   @abstractmethod
   def eat(self):
     pass