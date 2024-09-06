# Multiple Inheritance solver Diamond problem from multi level inheritance

class Father:
    key = "ABC"
    __password = "private"

    def __show_password(self):
        print(self.__password)

    def father_money(self):
        return 5

    def home(self):
        return "This is from Father"

    def show_everything(self):
        self.__show_password()

class Mother:
    def mother_money(self):
        return 2

    def home(self):
        return "This is from mother"

class Son1(Mother, Father):    # MRO : Method Resolution Order
    pass

class Son2(Father, Mother):
    pass

s1 = Son1()
print(s1.father_money())
print(s1.mother_money())
print(s1.home())
print(s1.key)
s1.show_everything()


s2 = Son2()
print(s2.home())



