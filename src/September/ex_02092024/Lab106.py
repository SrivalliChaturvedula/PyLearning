class Person:
    # name = "Amit"  # hardcoded value

    def __init__(self, name):
        self.name = name


    def walk(self, name):
        self.name = name
        print(self.name)


amit = Person("Amit")
print(amit.name)
pramod = Person("Pramod")
print(pramod.name)