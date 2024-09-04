# Constructor
# Special Function in class, __init__()
# It will be automatically called when you create an Object

class Dog:
    name = None    # instance variable
    age = None
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("I will be automatically called when an object is created.")
    def sleep(self):
        local_variable = 10
        print("sleeping")
        print("Who is sleeping", self.name, self.age)
        print(local_variable)

dog = Dog("chow", 12)
print(dog.name)
print(dog.age)
dog.sleep()
print(id(dog))

dog2 = Dog("mow", 10)
print(dog2.name)
print(dog2.age)
dog2.sleep()
print(id(dog2))

dog3 = Dog("Cow", 9)
print(dog3.name)
print(dog3.age)



