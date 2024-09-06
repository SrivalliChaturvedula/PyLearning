# Inheritance - Acquire attributes and behaviour from another class

class Father:
    key = "2BHK"

    def car(self):
        print("Father Car: Alto Car", self.key)


class Son(Father):
    key_2 = "3BHK"

    def home(self):
        print("3BHK")

    def truck(self):
        print("Truck")


father_obj = Father()
father_obj.car()

son_obj = Son()
son_obj.car()
