# Task #2
#
# Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
maximum = max(num1, num2)
print("Maximum of numbers is: ", maximum)

power = pow(num1, num2)
print("Power of numbers is: ", power)

addition = num1 + num2
print("Addition of numbers is: ", addition)

subtraction = num1 - num2
print("Subtraction of numbers is: ", subtraction)

multiplication = num1 * num2
print("Multiplication of numbers is: ", multiplication)

division = num1 / num2
print("Division of numbers is: ", division)

print("Formatted number1 is:", f"{num1: .3f}")
print("Formatted number2 is:", f"{num2: .3f}")

