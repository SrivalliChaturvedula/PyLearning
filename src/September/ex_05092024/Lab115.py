# Multi level Inheritance
# GrandFather class can access only his own attributes and functions.
# Father can access all the attributes and methods from grandfather class and his own attributes and functions.
# Son can access all the attributes and methods from father, grandfather and his own.

class GrandFather():
    gold = "2kg"

    def bhk1(self):
        print("1BHK")


class Father(GrandFather):
    diamond = "22 Karat"

    def bhk2(self):
        print("2BHK")


class Son(Father):
    btc = "1BTC"

    def bhk3(self):
        print("3BHK")

s = Son()
f = Father()
gf = GrandFather()
