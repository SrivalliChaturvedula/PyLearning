import math
try:
    output = math.exp(10)   # OverflowError: math range error
    print(output)
except Exception as x:
    print(x)
    print("Please try to use lower exponential value")



