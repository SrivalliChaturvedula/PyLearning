def sum_three(a=1, b=2, c=3):
    return a + b + c


result = sum_three()
print(result)

result2 = sum_three(2, 2)
print(result2)

result3 = sum_three(b=4, c=10, a=10)  # Even if the args are not in same order result does not get effected
print(result3)

