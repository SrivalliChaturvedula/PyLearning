# Hybrid Inheritance

# B inherits from A : Single Inheritance
# Both B and C inherits from A: Hierarchical inheritance
# D inherits both B and C : Multiple and Multilevel inheritance(MRO)


class A:
    def methodA(self):
        return "Method A"


class B(A):
    def methodB(self):
        return "Method B"


class C(A):
    def methodC(self):
        return "Method C"

class D(B, C):
    def methodD(self):
        return "Method D"

d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())