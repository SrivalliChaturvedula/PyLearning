print("-----Start of the program----")

try:
    a = int(input("Enter num1: \n"))
    b = int(input("Enter num2: \n"))
    c = a / b
    print("Result Div is", c)
except Exception as e:   # as is alias, Exception is a class that contains multiple exception classes
    print(e)
    print("Please check your inputs, it should not be  string or zero")



print("----End of the program-----")