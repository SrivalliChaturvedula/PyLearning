class Grandparent:
    key_gold = "1kg"
    def grand_parent_method(self):
        return "GrandParent's method"

class Parent(Grandparent):
    def parent_method(self):
        return "Parent's method"

class Child(Parent):
    mac_m3_apple = "M3 Max"

    def child_method(self):
        return "Child's Method"

child = Child()
print(child.grand_parent_method())