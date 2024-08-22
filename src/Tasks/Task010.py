"""
Task 10 - Factorial
n = 5
5! -->5*4*3*2*1 -> 120
3! -> 3*2*1 -> 6
4! -> 4*3*2*1 -> 24

"""
import math

for i in range(1, 6):
    factorial = math.factorial(i)
    print(f"The factorial of the number {i} is: {factorial}")

