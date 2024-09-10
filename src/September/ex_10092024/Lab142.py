# try, except and finally

try:
    a = int(input("Enter num1: \n"))
    b = int(input("Enter num2: \n"))
    c = a / b
except ValueError as e:
    print(e)
    print("Value error, you have entered the string instead of int")
except ZeroDivisionError as e:
    print("Division error, zero should not be given")
else:
    print(f"Result is {c}")
finally:
    print("This code will be executed")

