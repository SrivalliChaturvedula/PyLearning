# Static method
# A static method isa method that belongs to class rather than instance of the class.
class O:
    @staticmethod
    def sum(a, b):
        return a + b


class MathOperations:
    def div(self, a, b):
        return a / b

    @staticmethod  # it belongs to class no need of self to access attributes
    def sum(a, b):
        return a + b

    @staticmethod
    def mul(a, b):
        return a * b

    def sub(self, a, b):
        return a - b

# For non static methods, object creation is mandatory
mathOperation = MathOperations()
output = mathOperation.div(3, 4)
output2 = mathOperation.sub(4, 3)
print(output)
print(output2)

# Static methods can be called directly without creating an object
print(MathOperations.sum(3, 4))
print(MathOperations.mul(2, 3))
print(O.sum(3,4))
print(MathOperations.sum(5,6))