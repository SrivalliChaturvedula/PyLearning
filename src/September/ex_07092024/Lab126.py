# Method overloading - Python doesnot support this - same method name with different behaviour which is not possible

# Every class has father of object whether you mention it or not
class Math(object):
    def add(self, a, b):
        return a + b

    def add(self, a, b, c=9):  # this is possible only if you give default value to c
        return a + b + c


math = Math()
op1 = math.add(1, 2)
print(op1)

op2 = math.add(1, 2)
print(op2)
