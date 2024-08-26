"""
Task 10 - Factorial
n = 5
5! -->5*4*3*2*1 -> 120
3! -> 3*2*1 -> 6
4! -> 4*3*2*1 -> 24

"""
import math

# import math
#
# for i in range(1, 6):
#     factorial = math.factorial(i)
#     print(f"The factorial of the number {i} is: {factorial}")

# n = int(input("Enter number: "))
# if n < 0:
#     print("Factorial is not defined for negative numbers")
# elif n == 0 == 1:
#     print("Factorial is: 1")
# else:
#     print(math.factorial(n))

n = int(input("Enter number: "))
fact = 1
if n == 0 == 1:
    fact = 1
    print("Factorial is: ", 1)

else:
    for i in range(1, n+1, 1):
        fact = fact * i

    # i = 1
    # while(i <= n):
    #     fact = fact * i
    #     i = i + 1

print(f"Factorial of number is: {fact}")