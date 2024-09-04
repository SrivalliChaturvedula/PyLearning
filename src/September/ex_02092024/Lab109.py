# Encapsulation - bind data variables and methods
# Hide data members (class variables, instance variables)
# by using only methods

class Car:
    name = None
    password = 123

    def __init__(self):
        print("DC")

    def change_password(self):
        self.password = "pramod"


object_ref = Car()
print(object_ref.password)
