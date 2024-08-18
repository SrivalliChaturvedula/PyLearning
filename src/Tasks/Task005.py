# Create a program that takes two numbers as input and
# prints whether the first number is greater than, less than, or equal to the second number.

num1 = int(input("Enter number1:"))
num2 = int(input("Enter number2:"))

if num1 < num2:
    print("Number1 is less than number2")
elif num1 > num2:
    print("Number1 is greater than number2")

# Using ternary operator
print("number1 is equal to number2" if num1 == num2 else "not equal")
