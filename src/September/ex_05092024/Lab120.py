# Hierarchical Inheritance

class Father:
    def BHK1(self):
        print("1BHK")

class Pramod(Father):
    def BHK2(self):
        print("2BHK")

class Lucky(Father):
    def BHK3(self):
        print("3BHK")

class Amith(Father):
    def no_house(self):
        return "no house"

pramod = Pramod()
pramod.BHK1()
pramod.BHK2()

amit = Amith()
amit.BHK1()
amit.no_house()

lucky = Lucky()
lucky.BHK1()
lucky.BHK3()