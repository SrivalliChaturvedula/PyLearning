print("Start of the program")


a = int(input("Enter num1"))  # ValueError: invalid literal for int() with base 10: 'abc'
b = int(input("Enter num2"))   # ValueError: invalid literal for int() with base 10: 'cd'
c = a / b  # ZeroDivisionError: division by zero
print("Result Div is", c)

print("End of the program")  # this statement is not printed if it is not handled
