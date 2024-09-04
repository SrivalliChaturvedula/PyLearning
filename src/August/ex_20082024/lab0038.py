# To find maximum of three numbers

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

if num1 > num2 and num1 > num3:
    print("Maximum of numbers is:", num1)
elif num2 > num1 and num2 > num3:
    print("Maximum of numbers is:", num2)
else:
    print("Maximum of numbers is", num3)
