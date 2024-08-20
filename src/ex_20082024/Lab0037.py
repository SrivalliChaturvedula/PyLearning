# Problem to find max of two numbers

# logic building
# userinput: two int's and output: one int

num1 = float(input("Enter number1: \n"))
num2 = float(input("Enter number2: \n"))

if num1 > num2:
    print(f"Max is {num1}")
else:
    print("Max is", num2)
