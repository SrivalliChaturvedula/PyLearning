# Every class has object as Father class that means single inheritance even if it is not mentioned.

# class - blueprint
# object - Instance of class
# Encapsulation - public, private, protected
# Inheritance - single, multiple, multilevel, heri, hybrid
# polymorphism - method overriding, overloading is not supported
# self, __init__, super
# Abstraction _ hide the details and show what is required


# For example: Car class -- with Attributes key:  __private we created, tyres -> public
# Car -> multiple classes -> Engine, gearbox
#  Car -> Driver -> multiple classes -> Engine, gearbox
# But driver don't need to know about these classes details

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Bark")



dog = Dog("pp")
dog.sound()


