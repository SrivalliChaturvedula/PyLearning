# Variables
# 1. Local variable (within function / block of code)
# 2. global variable (which is defined outside the class or function)
# 3. instance variable (within classes)
# 4. Static variable

a = 10   # global variable

class Person:
    b = 11     # instance variable which belongs to class

    def print_infor(self):
        global a
        a = "Hello"
        print(a)
        print(self.b)   # self is used only in case of instance variable that is nothing but my variable


object_ref = Person()
object_ref.print_infor()
print(a)




