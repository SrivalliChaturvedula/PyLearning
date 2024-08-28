# Function scope

global_b = 20  # almost works like global variable


def my_function():
    a = 10  # local variable within function
    print(a)
    print(global_b)


def f1():
    print(global_b)


# print(a) as a is a local variable within function it can not be used here.
my_function()
print(global_b)  # global variable so it can be used with in function and outside the function too.
f1()
