# Create a program to sum of three numbers from userinput

a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
c = int(input("Enter number3: "))


def sum_of_three_numbers(num1, num2, num3):
    return a + b + c


result = sum_of_three_numbers(a, b, c)
result2 = sum_of_three_numbers(num1=a, num2=b, num3=c)
print(result)
print(result2)
