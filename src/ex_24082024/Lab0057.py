# User defined
# 1. They can't return anything -> non-return
# No parameter/ argument and No return type - NRNP
def greet():
    print("Hello, world")


"""
result = greet()
print(result)
This returns None as the function does not return anything
"""
greet()


# 2. No return type with argument
def greet_by_name(name):
    print("Hello", name)


greet_by_name("Valli")


# 3. No return type with default argument

def say_hello_to_default_argument(name="Srivalli"):
    print("Hello", name.upper())


say_hello_to_default_argument()
say_hello_to_default_argument("Jyo")
say_hello_to_default_argument(name="Shanu")  # positional argument


# Multiple arguments
def multiple_args(name1="Arpita", name2="Amith", name3="Arun"):
    print("Multiple arguments: ", name1, name2, name3)


multiple_args()
multiple_args(name1="Sri", name2="Valli", name3="Chaturvedula")
multiple_args(name1="Jyo", name3="Shaanu")
multiple_args("a", "b", "c")


# 4. with argument and return type

def sum_of_two_numbers(num1, num2):
    return num1 + num2


result = sum_of_two_numbers(1, 2)
result2 = sum_of_two_numbers(num1=2, num2=3)
print(result)
print(result2)


def sum_of_two_numbers_with_default(n1=100, n2=200):
    return n1 + n2


output = sum_of_two_numbers_with_default()
print(output)


