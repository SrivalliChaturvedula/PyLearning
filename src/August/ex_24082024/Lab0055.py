# functions with arguments/parameters

def greet():
    print("Hello there")


def greet_by_name(name):  # name is a variable name which can be of any data type
    print("Hello", name)


greet_by_name("Valli")
greet_by_name(123)

"""
This will not return anything
result = greet_by_name("Sri")
print(result)
"""


def greet_by_name(name2):
    print("Hello", name2)


name_value = input("Enter name: ")

greet_by_name(name_value)
