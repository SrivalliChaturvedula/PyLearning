# Pizza lovers

def make_pizza(*toppings):
    for topin in toppings:
        print(topin)


make_pizza("onion")
make_pizza("Tomato", "paneer", "sauce")
make_pizza("cheese", "paneer", "less sauce")

# Builtin functions
r = max(1, 2, 3, 4, 5)
print(r)
