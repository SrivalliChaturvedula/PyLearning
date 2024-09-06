class InstanceVar:
    b = 10
    _c = 20
    __d = 30


obj = InstanceVar()
print(obj.b)
print(obj._c)
# print(obj.__d)
# This is not allowed as this is private instance variable which can be accessed only within class