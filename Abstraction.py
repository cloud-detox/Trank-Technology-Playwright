from abc import ABC,abstractmethod

class Animal(ABC): # Abstract Class
    @abstractmethod
    def speak(self):
        pass # Must be defined in child class

class Dog(Animal):
    def speak(self):
        print("Woof")


dog=Dog()
dog.speak()