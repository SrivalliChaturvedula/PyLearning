# Only one argument is allowed with star that is first one.
# star cannot be second argument
def make_pizza(*toppings, base):
    print(toppings, base)


"""

This is not allowed multiple args of the second argument.

def make_pizza2(toppings, *base):
    print(base, toppings)
make_pizza("onion", "tomato", "mushroom", base="thin crust")

"""
