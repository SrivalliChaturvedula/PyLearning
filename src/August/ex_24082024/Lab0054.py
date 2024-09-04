"""
Types of functions:
1. Built-in functions
2.User defined functions: def and call
"""
import math
"""
# Builtin functions
input()
type()
pow()
max()
min()
range()
math.factorial()
sorted()
bool()
int()
str.lower()
str.upper()
"""

def greet_to_all_of_you():
    print("Hello everyone")


def greet():
    print("Yes")
    greet_to_all_of_you()


greet()
greet_to_all_of_you()