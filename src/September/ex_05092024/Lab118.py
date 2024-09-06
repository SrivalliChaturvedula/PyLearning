
# Multiple inheritance example

class A:
    def method(self):
        return "Method A"

class B:
    def method(self):
        return "Method B"

class C(B, A):    # output is B, because it is mentioned as first parameter here
    pass

c = C()
print(c.method())