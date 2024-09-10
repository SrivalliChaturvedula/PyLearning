# Type of exceptions that has to be handled

a = int(input("Enter num1"))  # ValueError: invalid literal for int() with base 10: 'abc'
b = int(input("Enter num2"))
c = a / b  # ZeroDivisionError: division by zero
print("Result Div is", c)
