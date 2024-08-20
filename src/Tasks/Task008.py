"""
Triangle Classifier:

Write a program that classifies a triangle based on its side lengths.

Given three input values representing the lengths of the sides,

determine if the triangle is equilateral (all sides are equal),


isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle

"""

a = int(input("Enter length of first side: "))
b = int(input("Enter length of second side: "))
c = int(input("Enter length of third side: "))

if a == b and a == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
