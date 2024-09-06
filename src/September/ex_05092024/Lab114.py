# Single Inheritance

class Parent:
    gold = "2kg"

    def BHK2(self):
        print("2BHK")

class Child(Parent):
    def BHK3(self):
        print("3BHK")

child_obj = Child()
print(child_obj.gold)
child_obj.BHK3()
child_obj.BHK2()

parent_ref = Parent()
parent_ref.BHK2()
#  parent_ref.BHK3()  -> Not allowed
