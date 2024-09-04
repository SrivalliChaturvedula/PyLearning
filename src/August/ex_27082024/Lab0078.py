import math


def give_me_power(num):
    return math.pow(num, 2)


give_pow = lambda : math.pow(int(input("Enter number: ")),  2)
print(give_pow())

