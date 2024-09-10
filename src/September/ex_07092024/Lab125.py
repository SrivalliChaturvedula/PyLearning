# Method overriding - SAme name in parent and child
# Child always override the parent functions
# super means call my parent function
class GrandFather:
    x = 20

    def home(self):
        print("No house")


class Father(GrandFather):
    a = 10

    def home(self):
        print("1BHK")
        print(self.a)
        print(super().x)
        super().home()


class Son(Father):
    def home(self):
        print(super().a)
        super().home()
        print("3BHK")


son1 = Son()
son1.home()

print(son1.x)

# self means my variable and methods in class,
# super keyword used to access parent class methods and attributes.
