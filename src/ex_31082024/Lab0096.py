class Dog:  # class name will always start with capital letter
    # A
    name = None
    breed = None
    color = None

    # B

    def sleep(self):
        print("Sleeping")

    def bark(self):
        print("Barking")

    def eat(self, food):
        print(food)


dog1 = Dog()
print(dog1.name)
dog1.name = "Chow"
print(dog1.name)
dog1.sleep()

print("__________________")

dog2 = Dog()
print(dog2.name)  # this will return None until we allot a value
dog2.name = "Mow"
print(dog2.name)
dog2.sleep()

dog3 = dog1

